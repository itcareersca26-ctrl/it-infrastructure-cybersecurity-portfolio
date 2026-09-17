# IT Asset Management & PowerShell Automation Lab

## Project Overview

This project demonstrates a basic IT asset-management system developed with PowerShell and CSV-based data storage.

The lab provides hands-on experience with hardware inventory, automated system discovery, asset lifecycle tracking, equipment status management, repair tracking, reporting, searching, and administrative automation.

All work was completed in an authorized personal home-lab environment.

> Personal identities, serial numbers, credentials, and other unnecessary sensitive information have been sanitized in the public portfolio version.

---

## Project Structure

- `Inventory/` — Manual and automatically discovered asset records
- `Lifecycle/` — Asset lifecycle history and repair records
- `Scripts/` — PowerShell automation tools

---

## Asset Inventory

The inventory tracks information including:

- Asset ID
- Asset type
- Manufacturer and model
- Operating system
- CPU and RAM
- Architecture
- Assigned user
- Department
- Status
- Location

Hardware serial numbers are redacted from the public version.

---

## Automated Hardware Discovery

`Get-AssetInventory.ps1` uses Windows CIM classes to collect system information automatically.

The script uses:

- `Win32_ComputerSystem`
- `Win32_OperatingSystem`
- `Win32_Processor`

It collects the computer name, manufacturer, model, operating system, architecture, processor, RAM, Windows user, status, and location.

This demonstrates automated IT asset discovery using PowerShell.

---

## Asset Lifecycle Management

`Asset-Lifecycle.csv` maintains historical asset status records.

Lifecycle states used by the project include:

- In Stock
- Assigned
- Active
- Repair
- Returned
- Retired

New lifecycle events are appended instead of simply replacing previous records, providing a basic history of asset changes.

---

## PowerShell Automation

Five PowerShell scripts were developed for the project.

### Get-AssetInventory.ps1

Automatically discovers Windows hardware and operating-system information using CIM.

### Get-AssetReport.ps1

Generates an asset-management summary showing total assets and current statuses such as Active, Repair, In Stock, Assigned, and Retired.

### Search-Asset.ps1

Searches for an individual Asset ID and displays its current information and lifecycle history.

### Search-AssetsByStatus.ps1

Filters assets according to their latest lifecycle status.

### Update-AssetStatus.ps1

Updates an asset's lifecycle status and appends the change to the lifecycle dataset.

The script uses `ValidateSet` to restrict status values to approved lifecycle states.

---

## Repair Tracking

The project includes a repair report for assets placed into repair status.

Repair records contain information such as:

- Asset ID
- Status
- Status date
- Department
- Location
- Notes

This demonstrates basic equipment maintenance and repair tracking.

---

## Technologies Used

- Windows 11
- PowerShell
- CIM / WMI
- CSV
- Git
- GitHub

---

## Skills Demonstrated

- IT asset management
- Hardware inventory
- Asset lifecycle management
- Windows administration
- PowerShell scripting
- CIM hardware discovery
- CSV data management
- Asset reporting
- Asset searching and filtering
- Repair tracking
- Parameter validation
- Administrative automation
- Technical documentation

---

## Security and Privacy

The public project has been sanitized.

Personal user identities and hardware serial numbers are excluded or replaced where appropriate. Credentials and authentication secrets are not stored in the public project.

---

## Related Portfolio Projects

This project complements:

- Managed IT Support & Service Desk
- Windows Server & Active Directory
- Windows File Server & SMB
- PowerShell Automation
- Microsoft 365 / SaaS Administration

---

## Project Status

**Status: Completed Lab Project**

The project contains verified inventory data, lifecycle records, repair tracking, and five PowerShell scripts for asset discovery, reporting, searching, filtering, and lifecycle management.
