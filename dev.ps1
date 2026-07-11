# Start Backend Server in a new window
Write-Host "Starting Django Backend Server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Write-Host '--- DJANGO BACKEND ---' -ForegroundColor Green; cd backend; .venv\Scripts\python.exe manage.py runserver"

# Start Frontend Server in a new window
Write-Host "Starting Next.js Frontend Server..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Write-Host '--- NEXT.JS FRONTEND ---' -ForegroundColor Cyan; cd frontend; npm run dev"

Write-Host "Concurrently spawning dev servers. Keep coding!" -ForegroundColor Gold
