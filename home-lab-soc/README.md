Home Lab SOC Monitoring & Security Detection

A hands-on Security Operations Center (SOC) project built to monitor a Windows-based home lab environment, identify security and availability events, document incidents, and validate detection capabilities through structured testing.

Project Overview

This project demonstrates practical experience with:

SOC monitoring
Windows security event monitoring
Authentication failure detection
Event ID 4625 analysis
Host availability monitoring
ICMP monitoring
SMB activity monitoring
Security detection rules
Incident documentation
Security testing
Python-based monitoring scripts
SOC dashboard development

The environment combines Windows systems with a Kali Linux monitoring system to provide centralized visibility into infrastructure health and selected security events.

Monitoring Architecture

The SOC monitoring environment includes:

Component	Purpose
Windows Domain Controller	Active Directory and DNS services
Windows File Server	File sharing and SMB activity
Windows Test System	Monitoring and security testing
Application/Test Server	Planned infrastructure expansion
Kali Linux	SOC monitoring and dashboard system
Python Scripts	Host and event monitoring
SOC Dashboard	Central monitoring interface

The public files in this repository use sanitized example network information for security and privacy.

Monitoring Capabilities
Host Availability Monitoring

The monitoring system checks whether lab systems are reachable and records availability changes.

This provides visibility into:

Systems going offline
Systems returning online
Connectivity problems
Availability incidents
Windows Security Event Monitoring

The project includes monitoring and analysis of Windows security events.

One of the primary detections is:

Event ID 4625 — An account failed to log on

This type of event can indicate:

Incorrect credentials
Repeated authentication failures
Potential account misuse
Configuration or authentication problems

The project demonstrates how security events can be identified, documented, and investigated.

SMB Monitoring

The project also considers SMB-related activity within the Windows lab environment.

SMB monitoring can provide visibility into:

File-sharing activity
Windows file-server communications
Potential access problems
Network activity involving file services
Security Detection

Detection rules are documented separately from incident reports.

The project currently includes an ICMP availability detection rule used to identify host availability changes.

Security detection documentation includes:

Detection purpose
Detection conditions
Expected behavior
Testing requirements
Detection results
Incident Documentation

The project uses structured reports to document monitoring events.

Example incident documentation includes:

Incident identification
Affected system
Detection information
Observed behavior
Investigation notes
Resolution/testing information

This demonstrates a basic SOC workflow from detection → investigation → documentation → validation.

Testing & Validation

Testing is an important part of the project.

The SOC system includes:

Test plans
Test cases
Expected results
Actual results
Detection validation
Monitoring validation

The purpose is to verify that monitoring components operate as expected rather than simply assuming that a detection works.

Project Files
07-Security-Detection

Contains security detection rules and detection reports.

09-Testing

Contains SOC testing documentation, including test plans and test results.

Documentation

Contains design and technical documentation for the monitoring dashboard.

Reports

Contains incident and monitoring reports.

Scripts

Contains monitoring automation scripts.

dashboard.py

Python-based SOC dashboard application used to present monitoring information.

Technologies
Kali Linux
Windows Server
Windows client systems
Active Directory
DNS
SMB
Python
PowerShell
Microsoft Hyper-V
TCP/IP networking
ICMP
Windows Security Events
JSON event data
Skills Demonstrated

This project demonstrates practical skills in:

Security Operations

Security event monitoring
Detection analysis
Incident documentation
Detection testing
Basic alert investigation

Systems Administration

Windows infrastructure
Active Directory
DNS
Windows file services
System troubleshooting

Networking

IPv4 networking
ICMP
Host availability
Network connectivity
SMB communications

Automation & Development

Python scripting
PowerShell
Monitoring automation
Dashboard development
Structured event data

Documentation

Technical documentation
Incident reports
Detection reports
Test plans
Test results
Security & Privacy

This repository is a sanitized portfolio version of the home lab.

Private information, credentials, passwords, personal information, and real home-network addressing are intentionally excluded from the public project.

Network addresses shown in public code and documentation are example addresses and should not be treated as the live lab configuration.

Project Objective

The objective of this project is to develop practical experience with the processes used in a small SOC environment:

Monitor → Detect → Investigate → Document → Test → Improve

The project will continue to expand as additional infrastructure, security detections, monitoring capabilities, and documentation are developed.
