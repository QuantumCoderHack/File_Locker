@echo off
set /p file=Enter file name: 
set /p pass=Enter password: 

python file_security.py lock %file% %pass%

pause