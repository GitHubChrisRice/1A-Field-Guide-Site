$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Venv = Join-Path $RepoRoot ".venv-preview"
$Python = Join-Path $Venv "Scripts\python.exe"
$Requirements = Join-Path $PSScriptRoot "requirements.txt"

if (-not (Test-Path $Python)) {
    Write-Host "Creating local preview environment..."
    if (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3 -m venv $Venv
    }
    elseif (Get-Command python -ErrorAction SilentlyContinue) {
        & python -m venv $Venv
    }
    else {
        throw "Python 3 was not found. Install Python 3, then run this script again."
    }
}

Write-Host "Checking preview dependencies..."
& $Python -m pip install --disable-pip-version-check -r $Requirements

Write-Host ""
Write-Host "California 1A Field Guide preview"
Write-Host "Open http://127.0.0.1:8000/ if your browser does not open automatically."
Write-Host "Press Ctrl+C here to stop the preview server."
Write-Host ""

Set-Location $RepoRoot

# Open the browser after the local server has had a moment to start.
$OpenBrowser = "Start-Sleep -Seconds 2; Start-Process 'http://127.0.0.1:8000/'"
Start-Process powershell.exe -WindowStyle Hidden -ArgumentList "-NoProfile", "-Command", $OpenBrowser

& $Python -m mkdocs serve --dev-addr 127.0.0.1:8000
