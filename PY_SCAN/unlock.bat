@echo off
set /p file=Enter locked file: 
set /p pass=Enter password: 

python file_security.py unlock %file% %pass%

pause