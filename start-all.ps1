# PowerShell Startup Script for Open Sousveillance Studio
# This script activates the virtual environment, upgrades pip, installs requirements,
# and launches the backend (FastAPI) and frontend (Streamlit) in separate terminals.

# Set project root
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $projectRoot

# Activate virtual environment
$venvPath = ".venv/Scripts/Activate.ps1"
if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment..."
    . $venvPath
} else {
    Write-Host "Virtual environment not found. Please create it first."
    exit 1
}

# Upgrade pip
Write-Host "Upgrading pip..."
pip install --upgrade pip

# Install requirements only if not already satisfied
if (Test-Path "requirements.txt") {
    Write-Host "Checking Python requirements..."
    $missing = pip install --dry-run -r requirements.txt 2>&1 | Select-String 'would be installed' | Measure-Object | Select-Object -ExpandProperty Count
    if ($missing -gt 0) {
        Write-Host "Installing missing requirements..."
        pip install -r requirements.txt
    } else {
        Write-Host "All requirements already satisfied."
    }
} else {
    Write-Host "requirements.txt not found!"
    exit 1
}

# Start FastAPI backend in new terminal
Write-Host "Starting FastAPI backend in new terminal..."
Start-Process powershell -ArgumentList '-NoExit', '-Command', "cd '$projectRoot'; . .venv/Scripts/Activate.ps1; uvicorn src.app:app --reload --port 8000"

# Start Streamlit frontend in new terminal (will open browser)
Write-Host "Starting Streamlit frontend in new terminal..."
Start-Process powershell -ArgumentList '-NoExit', '-Command', "cd '$projectRoot'; . .venv/Scripts/Activate.ps1; streamlit run src/ui/app.py"

Write-Host "All services started. Backend: http://localhost:8000  |  Frontend: http://localhost:8501"
