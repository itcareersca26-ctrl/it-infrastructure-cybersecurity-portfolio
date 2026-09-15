#!/usr/bin/env python3

import subprocess
import time
from datetime import datetime
from pathlib import Path


# ==========================================
# HOME LAB SOC - HOST MONITOR v1
# ==========================================

HOSTS = {
    "DC01": "10.10.10.10",
    "HOME-DC01": "10.10.10.11",
    "HOME-FILE01": "10.10.10.12",
    "HOME-TEST01": "10.10.10.13",
}

INTERVAL = 10

BASE_DIR = Path.home() / "Home-Lab-SOC-Project"
LOG_DIR = BASE_DIR / "06-Monitoring" / "Logs"
LOG_FILE = LOG_DIR / "host-monitor.log"


# ==========================================
# CREATE LOG DIRECTORY
# ==========================================

LOG_DIR.mkdir(parents=True, exist_ok=True)


# ==========================================
# CHECK HOST
# ==========================================

def check_host(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


# ==========================================
# HEADER
# ==========================================

print("=" * 55)
print("        HOME LAB SOC - HOST MONITOR v1")
print("=" * 55)
print("Monitoring authorized laboratory systems")
print("Interval:", INTERVAL, "seconds")
print("Log file:", LOG_FILE)
print()
print("Press Ctrl+C to stop.")
print()


# ==========================================
# MONITORING LOOP
# ==========================================

try:

    while True:

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for hostname, ip in HOSTS.items():

            if check_host(ip):
                status = "UP"
            else:
                status = "DOWN"

            line = (
                f"{timestamp} | "
                f"{hostname:<15} | "
                f"{ip:<15} | "
                f"{status}"
            )

            print(line)

            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(line + "\n")

        print("-" * 70)

        time.sleep(INTERVAL)


# ==========================================
# CLEAN EXIT
# ==========================================

except KeyboardInterrupt:

    print()
    print("=" * 55)
    print("Monitoring stopped.")
    print("=" * 55)
    print("Log saved to:")
    print(LOG_FILE)
