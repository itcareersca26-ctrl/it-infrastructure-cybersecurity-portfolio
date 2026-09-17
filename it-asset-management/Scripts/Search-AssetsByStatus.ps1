$LifecycleFile = "C:\Tedman-SaaS-Lab\01-Asset-Management\Lifecycle\Asset-Lifecycle.csv"

$Lifecycle = Import-Csv $LifecycleFile

$LatestAssets = $Lifecycle |
    Group-Object "Asset ID" |
    ForEach-Object {
        $_.Group | Select-Object -Last 1
    }

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "       TEDMAN SOLUTIONS" -ForegroundColor Cyan
Write-Host "       SEARCH ASSETS BY STATUS" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

$Status = Read-Host "Enter Status (Active, Repair, In Stock, Assigned, Retired)"

$Results = @(
    $LatestAssets | Where-Object { $_.Status -eq $Status }
)

if ($Results.Count -eq 0) {

    Write-Host ""
    Write-Host "No assets found with status: $Status" -ForegroundColor Red

}
else {

    Write-Host ""
    Write-Host "Assets with status: $Status" -ForegroundColor Green
    Write-Host ""

    $Results |
        Select-Object "Asset ID", Status, "Assigned User", Department, Location |
        Format-Table -AutoSize
}