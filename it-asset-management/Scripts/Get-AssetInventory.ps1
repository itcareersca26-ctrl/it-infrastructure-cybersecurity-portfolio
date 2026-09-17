$ComputerSystem = Get-CimInstance Win32_ComputerSystem
$OperatingSystem = Get-CimInstance Win32_OperatingSystem
$Processor = Get-CimInstance Win32_Processor

$RAMGB = [math]::Round($ComputerSystem.TotalPhysicalMemory / 1GB, 0)

$Asset = [PSCustomObject]@{
    "Asset ID"         = "AUTO-$($ComputerSystem.Name)"
    "Computer Name"    = $ComputerSystem.Name
    "Manufacturer"     = $ComputerSystem.Manufacturer
    "Model"            = $ComputerSystem.Model
    "Serial Number"    = "REDACTED"
    "Assigned User"    = $env:USERNAME
    "Operating System" = $OperatingSystem.Caption
    "Architecture"     = $OperatingSystem.OSArchitecture
    "CPU"              = $Processor.Name
    "RAM"              = "$RAMGB GB"
    "Status"           = "Active"
    "Location"         = "Home Lab"
}

$Asset | Format-List