SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
cd $SH
$SH/.venv/bin/python3 -m pip install requests
#                     -m pip         package name

echo

$SH/.venv/bin/python3 -m pip freeze
