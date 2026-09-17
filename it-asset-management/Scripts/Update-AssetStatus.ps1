param(
    [Parameter(Mandatory=$true)]
    [string]$AssetID,

    [Parameter(Mandatory=$true)]
    [ValidateSet("In Stock","Assigned","Active","Repair","Returned","Retired")]
    [string]$Status
)

$LifecycleFile = "C:\Tedman-SaaS-Lab\01-Asset-Management\Lifecycle\Asset-Lifecycle.csv"

$Assets = Import-Csv $LifecycleFile

$Asset = $Assets | Where-Object { $_."Asset ID" -eq $AssetID } | Select-Object -Last 1

if (-not $Asset) {
    Write-Host "Asset $AssetID was not found." -ForegroundColor Red
    exit
}

$NewRecord = [PSCustomObject]@{
    "Asset ID"       = $AssetID
    "Status"         = $Status
    "Status Date"    = (Get-Date -Format "yyyy-MM-dd")
    "Assigned User"  = $Asset."Assigned User"
    "Department"     = $Asset.Department
    "Location"       = $Asset.Location
    "Notes"          = "Status changed from $($Asset.Status) to $Status"
}

$NewRecord | Export-Csv $LifecycleFile -Append -NoTypeInformation

Write-Host ""
Write-Host "Asset status updated successfully." -ForegroundColor Green
Write-Host "Asset ID: $AssetID"
Write-Host "Previous Status: $($Asset.Status)"
Write-Host "New Status: $Status"