[CmdletBinding(SupportsShouldProcess)]
param([string]$InstallRoot = "$env:ProgramFiles\VETRA\MSP Persianizer")
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
if ($env:OS -ne 'Windows_NT') { throw 'This uninstaller must run on Windows.' }
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) { throw 'Run PowerShell as Administrator.' }
$backupRoot = Join-Path $env:ProgramData 'VETRA\Backups'
if (Test-Path $InstallRoot) {
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $uninstallBackup = Join-Path $backupRoot "uninstall-$stamp"
    New-Item -ItemType Directory -Force -Path $uninstallBackup | Out-Null
    Copy-Item $InstallRoot $uninstallBackup -Recurse -Force
    if ($PSCmdlet.ShouldProcess($InstallRoot, 'Remove VETRA installation')) { Remove-Item $InstallRoot -Recurse -Force }
}
Write-Host 'VETRA removed. Microsoft Project and .MPP files were not deleted.' -ForegroundColor Green
