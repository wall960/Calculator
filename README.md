#Calculator lab project
##How to run it
How to run it

Activate the SCCM4910 virtual environment with:
source /opt/python-venv.sccm-4910/bin.activate

and check with
python3 -m pytest --version

Once complete:
Run: python3 calculator.py
Operations: + - * / (two numbers)
Run with ./run.sh

Perform a test check with ./check.sh
The test should return 5 different tests with an exit
status of 0 and a QUALITY GATE PASSED message

Stop the calculator interface with Ctrl + C