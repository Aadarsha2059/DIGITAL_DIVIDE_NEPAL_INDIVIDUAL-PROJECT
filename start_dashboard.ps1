#!/usr/bin/env pwsh
# PowerShell script to start the Digital Divide Dashboard

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Digital Divide Nepal Dashboard" -ForegroundColor Green
Write-Host "  Starting Application..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if streamlit is installed
$streamlitCheck = python -m streamlit --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Streamlit is not installed!" -ForegroundColor Red
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    python -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to install packages. Please run: pip install -r requirements.txt" -ForegroundColor Red
        exit 1
    }
}

Write-Host "✅ Starting dashboard..." -ForegroundColor Green
Write-Host "📊 The dashboard will open in your browser at http://localhost:8501" -ForegroundColor Cyan
Write-Host ""

# Run streamlit
python -m streamlit run digital_divide_dashboard.py

Write-Host ""
Write-Host "Dashboard stopped." -ForegroundColor Yellow
