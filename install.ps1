
$ErrorActionPreference = "Stop"

$repo = "https://github.com/husitao/liang_wen_what.git"

Write-Host "Installing ds-now..." -ForegroundColor Cyan

# 1. Check uv
$uv = Get-Command uv -ErrorAction SilentlyContinue

if (-not $uv) {
    Write-Host "uv not found. Installing uv..."

    irm https://astral.sh/uv/install.ps1 | iex

    # Refresh PATH for current session
    $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"

    $uv = Get-Command uv -ErrorAction SilentlyContinue

    if (-not $uv) {
        throw "uv installation failed. Please reopen PowerShell and retry."
    }
}

# 2. Install CLI from GitHub
Write-Host "Installing ds-now from GitHub..."

uv tool install --force "git+$repo"

# 3. Configure executable PATH
uv tool update-shell

Write-Host ""
Write-Host "Installation completed!" -ForegroundColor Green
Write-Host "Run: ds-now or liang-wen-what"
Write-Host "If command is not found, restart your terminal."
Write-Host "Interesting! Enjoy."
