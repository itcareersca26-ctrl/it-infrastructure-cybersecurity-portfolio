$LifecycleFile = "C:\Tedman-SaaS-Lab\01-Asset-Management\Lifecycle\Asset-Lifecycle.csv"

$Lifecycle = Import-Csv $LifecycleFile

$LatestAssets = $Lifecycle |
    Group-Object "Asset ID" |
    ForEach-Object {
        $_.Group | Select-Object -Last 1
    }

$TotalAssets = @($LatestAssets).Count
$ActiveAssets = @($LatestAssets | Where-Object { $_.Status -eq "Active" }).Count
$RepairAssets = @($LatestAssets | Where-Object { $_.Status -eq "Repair" }).Count
$StockAssets = @($LatestAssets | Where-Object { $_.Status -eq "In Stock" }).Count
$AssignedAssets = @($LatestAssets | Where-Object { $_.Status -eq "Assigned" }).Count
$RetiredAssets = @($LatestAssets | Where-Object { $_.Status -eq "Retired" }).Count

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "       TEDMAN SOLUTIONS" -ForegroundColor Cyan
Write-Host "       ASSET MANAGEMENT REPORT" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Total Assets:     $TotalAssets"
Write-Host "Active:           $ActiveAssets"
Write-Host "In Repair:        $RepairAssets"
Write-Host "In Stock:         $StockAssets"
Write-Host "Assigned:         $AssignedAssets"
Write-Host "Retired:          $RetiredAssets"

Write-Host ""
Write-Host "CURRENT ASSET STATUS" -ForegroundColor Yellow
Write-Host "-----------------------------------------"

$LatestAssets |
    Select-Object "Asset ID", Status, "Assigned User", Department, Location |
    Format-Table -AutoSize