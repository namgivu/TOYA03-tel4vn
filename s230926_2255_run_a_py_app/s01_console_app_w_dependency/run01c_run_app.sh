SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
cd $SH
$SH/.venv/bin/python3 "$SH/app.py"
