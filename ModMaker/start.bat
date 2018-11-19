@echo off
cls
set /p pip_updated=<pip_updated.txt

if %pip_updated% == true (
	echo PIP seems to already be updated!
)
else %pip_updated% == false (
	echo updating PIP...
	python -m pip install --upgrade pip
	pip updated!
	echo true > pip_updated.txt
)
py Main.py
pause