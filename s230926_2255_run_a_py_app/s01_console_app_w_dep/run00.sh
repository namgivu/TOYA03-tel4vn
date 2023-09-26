SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
python3 "$SH/app.py"

consoleoutput="
ModuleNotFoundError: No module named 'requests'
"
