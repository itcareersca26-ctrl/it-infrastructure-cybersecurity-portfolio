$LifecycleFile = "C:\Tedman-SaaS-Lab\01-Asset-Management\Lifecycle\Asset-Lifecycle.csv"

$Lifecycle = Import-Csv $LifecycleFile

$AssetID = Read-Host "Enter Asset ID"

$AssetHistory = $Lifecycle | Where-Object { $_."Asset ID" -eq $AssetID }

if ($null -eq $AssetHistory) {

    Write-Host ""
    Write-Host "Asset not found." -ForegroundColor Red
    Write-Host "Asset ID: $AssetID"

}
else {

    $CurrentAsset = $AssetHistory | Select-Object -Last 1

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host "          ASSET SEARCH RESULT" -ForegroundColor Cyan
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Asset Found" -ForegroundColor Green
    Write-Host "-----------"

    Write-Host "Asset ID:        $($CurrentAsset.'Asset ID')"
    Write-Host "Current Status:  $($CurrentAsset.Status)"
    Write-Host "Assigned User:   $($CurrentAsset.'Assigned User')"
    Write-Host "Department:      $($CurrentAsset.Department)"
    Write-Host "Location:        $($CurrentAsset.Location)"
    Write-Host "Status Date:     $($CurrentAsset.'Status Date')"

    Write-Host ""
    Write-Host "LIFECYCLE HISTORY" -ForegroundColor Yellow
    Write-Host "-----------------"

    $AssetHistory |
        Select-Object "Status Date", Status, "Assigned User", Location, Notes |
        Format-Table -AutoSize
}