@echo off
title Running Main Async Program
color a
REM Menjalankan script Python dari direktori saat ini
python "%~dp0main_async.py"
REM Menunggu input dari pengguna agar window tidak langsung tertutup
pause