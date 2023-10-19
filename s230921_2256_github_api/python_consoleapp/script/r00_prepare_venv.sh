# execute at :python_consoleapp folder
SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
python_consoleapp=`cd "$SH/../../python_consoleapp" && pwd`
cd $python_consoleapp

# optional upgrade pip
python3 -m pip install --upgrade pip

# create .venv fr -m virtualenv under :python_consoleapp folder
python3 -m pip install virtualenv
python3 -m             virtualenv .venv

echo ; ls -l .venv
echo ; ./.venv/bin/python3 --version
echo ; ./.venv/bin/pip     --version
