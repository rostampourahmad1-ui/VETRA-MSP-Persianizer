[CmdletBinding()]
param(
    [string]$InstallRoot = "$env:ProgramFiles\VETRA\MSP Persianizer",
    [switch]$SkipPythonInstall,
    [switch]$SkipPywin32,
    [switch]$WhatIf
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Write-Step([string]$Message) { Write-Host "[VETRA] $Message" -ForegroundColor Cyan }
function Fail([string]$Message) { throw "VETRA installation failed: $Message" }
function Invoke-Checked([string]$File, [string[]]$Arguments) {
    & $File @Arguments
    if ($LASTEXITCODE -ne 0) { Fail "$File exited with code $LASTEXITCODE" }
}

if ($WhatIf) { Write-Step "Dry-run mode: no files or registry settings will be changed." }
if ($env:OS -ne 'Windows_NT') { Fail "This installer must run on Windows." }
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Fail "Run PowerShell as Administrator."
}

Write-Step "Detecting Microsoft Project 2024..."
$projectKeys = @(
    'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*',
    'HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*'
)
$project = Get-ItemProperty $projectKeys -ErrorAction SilentlyContinue |
    Where-Object { $_.DisplayName -match 'Microsoft Project' -and $_.DisplayVersion -match '^2024|^24\.' } |
    Select-Object -First 1
if (-not $project) { Fail 'Microsoft Project 2024 was not detected.' }
Write-Step "Detected $($project.DisplayName) $($project.DisplayVersion)"

$python = Get-Command python.exe -ErrorAction SilentlyContinue
if (-not $python -and -not $SkipPythonInstall) {
    $winget = Get-Command winget.exe -ErrorAction SilentlyContinue
    if (-not $winget) { Fail 'Python 3.10+ is missing and winget is unavailable. Install Python, then retry.' }
    Write-Step 'Installing Python 3.11 through winget...'
    Invoke-Checked $winget.Source @('install','--id','Python.Python.3.11','--exact','--scope','machine','--silent','--accept-package-agreements','--accept-source-agreements')
    $python = Get-Command python.exe -ErrorAction SilentlyContinue
}
if (-not $python) { Fail 'Python 3.10+ is required.' }
$pythonVersion = & $python.Source --version
Write-Step "Using $pythonVersion"

$sourceRoot = Split-Path -Parent $PSScriptRoot
$backupRoot = Join-Path $env:ProgramData 'VETRA\Backups'
if (-not $WhatIf) {
    New-Item -ItemType Directory -Force -Path $InstallRoot, $backupRoot | Out-Null
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $backup = Join-Path $backupRoot $stamp
    New-Item -ItemType Directory -Force -Path $backup | Out-Null
    if (Test-Path $InstallRoot) { Copy-Item $InstallRoot (Join-Path $backup 'previous-install') -Recurse -Force -ErrorAction SilentlyContinue }
    if (([IO.Path]::GetFullPath($sourceRoot).TrimEnd('\') -ne [IO.Path]::GetFullPath($InstallRoot).TrimEnd('\'))) {
        Copy-Item (Join-Path $sourceRoot 'src') $InstallRoot -Recurse -Force
        Copy-Item (Join-Path $sourceRoot 'pyproject.toml') $InstallRoot -Force
        Copy-Item (Join-Path $sourceRoot 'docs') $InstallRoot -Recurse -Force
    }
}

if (-not $SkipPywin32 -and -not $WhatIf) {
    Write-Step 'Installing pywin32 for the Windows COM adapter...'
    Invoke-Checked $python.Source @('-m','pip','install','--upgrade','pywin32')
}

$envFile = Join-Path $InstallRoot 'vetra-env.ps1'
if (-not $WhatIf) {
    @"
`$env:PYTHONPATH = '$InstallRoot\src'
"@ | Set-Content $envFile -Encoding UTF8
    Write-Step "Installed to $InstallRoot"
    Write-Step "Run: . '$envFile'; python -m vetra_core.cli diagnostics"
}
Write-Step 'Installation completed. Existing MPP files were not modified.'
