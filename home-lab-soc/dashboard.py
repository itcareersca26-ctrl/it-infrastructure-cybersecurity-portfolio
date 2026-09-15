from flask import Flask, render_template_string
from datetime import datetime
import subprocess
import time
from pathlib import Path
import json

app = Flask(__name__)

HOSTS = {
    "HOME-DC01": "10.10.10.11",
    "HOME-FILE01": "10.10.10.12",
    "HOME-TEST01": "10.10.10.13",
    "DC01": "10.10.10.10",
}

REFRESH_SECONDS = 10

PROJECT_ROOT = Path.home() / "Home-Lab-SOC-Project"
EVENT_LOG = PROJECT_ROOT / "06-Monitoring" / "Logs" / "dashboard-events.log"

SECURITY_EVENT_FILES = {
    "HOME-TEST01": Path("/mnt/soc-events/security-events.json"),
    "HOME-DC01": Path("/mnt/soc-events-dc01/security-events.json"),
    "HOME-FILE01": Path("/mnt/soc-events-file01/security-events.json"),
    "DC01": Path("/mnt/soc-events-host/security-events.json"),
}

previous_status = {}


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>HOME LAB SOC Dashboard V3.1</title>

    <meta http-equiv="refresh" content="{{ refresh }}">

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 30px;
            background: #080c12;
            color: #f1f5f9;
            font-family: Arial, sans-serif;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
        }

        h1 {
            margin: 0;
            font-size: 30px;
        }

        .subtitle {
            color: #94a3b8;
            margin-top: 6px;
        }

        .live {
            color: #22c55e;
            font-weight: bold;
        }

        .summary {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-bottom: 25px;
        }

        .summary-card {
            background: #111827;
            border: 1px solid #263244;
            border-radius: 12px;
            padding: 20px;
        }

        .summary-title {
            color: #94a3b8;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .summary-value {
            font-size: 30px;
            font-weight: bold;
            margin-top: 8px;
        }

        .up-value {
            color: #22c55e;
        }

        .down-value {
            color: #ef4444;
        }

        .event-value {
            color: #f59e0b;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }

        .host-card {
            background: #111827;
            border: 1px solid #263244;
            border-radius: 14px;
            padding: 22px;
        }

        .host-name {
            font-size: 21px;
            font-weight: bold;
        }

        .ip {
            color: #64748b;
            margin-top: 5px;
            font-family: monospace;
        }

        .status {
            margin-top: 20px;
            font-size: 19px;
            font-weight: bold;
        }

        .up {
            color: #22c55e;
        }

        .down {
            color: #ef4444;
        }

        .unknown {
            color: #f59e0b;
        }

        .details {
            margin-top: 18px;
            border-top: 1px solid #263244;
            padding-top: 15px;
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.8;
        }

        .value {
            color: #e2e8f0;
            font-weight: bold;
        }

        .events {
            margin-top: 30px;
            background: #111827;
            border: 1px solid #263244;
            border-radius: 14px;
            padding: 22px;
        }

        .events h2 {
            margin-top: 0;
        }

        .event {
            border-top: 1px solid #263244;
            padding: 12px 0;
            font-family: monospace;
            font-size: 13px;
        }

        .high {
            color: #ef4444;
            font-weight: bold;
        }

        .medium {
            color: #f59e0b;
            font-weight: bold;
        }

        .footer {
            margin-top: 30px;
            color: #64748b;
            font-size: 13px;
        }

    </style>

</head>

<body>

<div class="header">

    <div>

        <h1>HOME LAB SOC</h1>

        <div class="subtitle">
            Security Operations Center Dashboard V3.1
        </div>

    </div>

    <div class="live">
        ● LIVE MONITORING
    </div>

</div>


<div class="summary">

    <div class="summary-card">

        <div class="summary-title">
            Monitored Hosts
        </div>

        <div class="summary-value">
            {{ total }}
        </div>

    </div>


    <div class="summary-card">

        <div class="summary-title">
            Hosts UP
        </div>

        <div class="summary-value up-value">
            {{ up }}
        </div>

    </div>


    <div class="summary-card">

        <div class="summary-title">
            Hosts DOWN
        </div>

        <div class="summary-value down-value">
            {{ down }}
        </div>

    </div>


    <div class="summary-card">

        <div class="summary-title">
            Events
        </div>

        <div class="summary-value event-value">
            {{ events|length + security_events|length }}
        </div>

    </div>

</div>


<div class="grid">

{% for hostname, data in results.items() %}

<div class="host-card">

    <div class="host-name">
        {{ hostname }}
    </div>

    <div class="ip">
        {{ data.ip }}
    </div>


    {% if data.status == "UP" %}

        <div class="status up">
            ● UP
        </div>

    {% elif data.status == "DOWN" %}

        <div class="status down">
            ● DOWN
        </div>

    {% else %}

        <div class="status unknown">
            ● UNKNOWN
        </div>

    {% endif %}


    <div class="details">

        Response:
        <span class="value">
            {{ data.response }}
        </span>

        <br>

        Last live check:
        <span class="value">
            {{ data.timestamp }}
        </span>

    </div>

</div>

{% endfor %}

</div>


<div class="events">

    <h2>
        Recent Security & Monitoring Events
    </h2>


    {% if events %}

        {% for event in events %}

        <div class="event">
            {{ event }}
        </div>

        {% endfor %}

    {% else %}

        <div class="event">
            No monitoring events recorded.
        </div>

    {% endif %}

</div>


<div class="events">

    <h2>
        Windows Security Alerts — Event ID 4625
    </h2>

    {% if security_events %}

        {% for event in security_events %}

        <div class="event">

            <strong>{{ event.Endpoint }}</strong>
            |
            {{ event.IPAddress }}
            |
            {{ event.Detection }}
            |
            Event ID: {{ event.EventID }}
            |
            Severity:
            <span class="high">
                {{ event.Severity }}
            </span>
            |
            {{ event.TimeCreated }}

        </div>

        {% endfor %}

    {% else %}

        <div class="event">
            No Windows 4625 security events detected.
        </div>

    {% endif %}

</div>


<div class="footer">

    Authorized Home Lab Monitoring |
    Refresh interval: {{ refresh }} seconds |
    Dashboard: 10.10.10.14:5000

</div>


</body>
</html>
"""


def check_host(ip):

    start = time.perf_counter()

    try:

        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=2
        )

        elapsed = (time.perf_counter() - start) * 1000

        if result.returncode == 0:

            return {
                "status": "UP",
                "response": f"{elapsed:.1f} ms"
            }

        return {
            "status": "DOWN",
            "response": "No response"
        }

    except Exception:

        return {
            "status": "UNKNOWN",
            "response": "Check failed"
        }


def log_event(hostname, old_status, new_status):

    if old_status == new_status:
        return

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    if new_status == "DOWN":

        severity = "HIGH"

    elif new_status == "UP" and old_status == "DOWN":

        severity = "HIGH"

    else:

        severity = "MEDIUM"

    event = (
        f"{timestamp} | "
        f"{hostname} | "
        f"{old_status} -> {new_status} | "
        f"{severity}"
    )

    EVENT_LOG.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with EVENT_LOG.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(event + "\n")


def get_live_status():

    results = {}

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    for hostname, ip in HOSTS.items():

        result = check_host(ip)

        current_status = result["status"]

        if hostname in previous_status:

            log_event(
                hostname,
                previous_status[hostname],
                current_status
            )

        previous_status[hostname] = current_status

        results[hostname] = {
            "ip": ip,
            "status": current_status,
            "response": result["response"],
            "timestamp": timestamp
        }

    return results


def get_security_events():

    all_events = []

    for endpoint, event_file in SECURITY_EVENT_FILES.items():

        if not event_file.exists():
            continue

        try:

            data = json.loads(
                event_file.read_text(
                    encoding="utf-8"
                )
            )

            if isinstance(data, dict):
                data = [data]

            for event in data:

                if not isinstance(event, dict):
                    continue

                event["Endpoint"] = event.get(
                    "Endpoint",
                    endpoint
                )

                event["IPAddress"] = event.get(
                    "IPAddress",
                    HOSTS.get(endpoint, "Unknown")
                )

                all_events.append(event)

        except Exception:
            continue

    def event_time(event):

        try:
            return datetime.strptime(
                event.get("TimeCreated", ""),
                "%Y-%m-%d %H:%M:%S"
            )

        except Exception:
            return datetime.min

    all_events.sort(
        key=event_time,
        reverse=True
    )

    return all_events[:20]


def get_recent_events():

    if not EVENT_LOG.exists():

        return []

    try:

        lines = EVENT_LOG.read_text(
            encoding="utf-8"
        ).splitlines()

        return lines[-10:][::-1]

    except Exception:

        return []


@app.route("/")
def dashboard():

    results = get_live_status()

    up = sum(
        1
        for data in results.values()
        if data["status"] == "UP"
    )

    down = sum(
        1
        for data in results.values()
        if data["status"] == "DOWN"
    )

    events = get_recent_events()

    security_events = get_security_events()

    return render_template_string(
        HTML,
        results=results,
        total=len(results),
        up=up,
        down=down,
        events=events,
        security_events=security_events,
        refresh=REFRESH_SECONDS
    )


if __name__ == "__main__":

    print("=" * 60)

    print(
        "              HOME LAB SOC DASHBOARD V3.1"
    )

    print("=" * 60)

    print(
        "Monitoring authorized laboratory systems"
    )

    print(
        "Dashboard: http://10.10.10.14:5000"
    )

    print(
        "Live monitoring enabled"
    )

    print(
        "Event logging enabled"
    )

    print(
        "Windows Event ID 4625 monitoring enabled"
    )

    print(
        "Monitoring 4 Windows security event feeds"
    )

    print(
        "Refresh interval: 10 seconds"
    )

    print(
        "Press Ctrl+C to stop."
    )

    print()

    app.run(
        host="10.10.10.14",
        port=5000,
        debug=False
    )
