# PS-001 - Service Desk System Information
# Collects basic system information for troubleshooting.

$Output = "$env:USERPROFILE\Desktop\ServiceDesk-SystemInfo.txt"

"========================================" | Out-File $Output
"SERVICE DESK SYSTEM INFORMATION" | Out-File $Output -Append
"========================================" | Out-File $Output -Append
"Date: $(Get-Date)" | Out-File $Output -Append

"`nCOMPUTER INFORMATION" | Out-File $Output -Append
Get-CimInstance Win32_ComputerSystem |
    Select-Object Name, Manufacturer, Model |
    Format-List | Out-File $Output -Append

"`nOPERATING SYSTEM" | Out-File $Output -Append
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, OSArchitecture |
    Format-List | Out-File $Output -Append

"`nNETWORK CONFIGURATION" | Out-File $Output -Append
Get-NetIPConfiguration |
    Select-Object InterfaceAlias, IPv4Address, IPv4DefaultGateway, DNSServer |
    Format-List | Out-File $Output -Append

"`nIMPORTANT SERVICES" | Out-File $Output -Append
Get-Service |
    Where-Object {$_.Status -eq "Running"} |
    Select-Object -First 20 Name,DisplayName,Status |
    Format-Table -AutoSize | Out-File $Output -Append

"`nSYSTEM INFORMATION COLLECTION COMPLETE" | Out-File $Output -Append

Write-Host "System information collected." -ForegroundColor Green
Write-Host "Output: $Output" -ForegroundColor Cyan
