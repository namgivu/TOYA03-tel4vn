# execute at :python_consoleapp folder
SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
python_consoleapp=`cd "$SH/../../python_consoleapp" && pwd`
cd $python_consoleapp


echo -e "\n--- before" ; ./.venv/bin/pip freeze

# install :requests
echo
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/pip install requests

echo -e "\n--- after" ; ./.venv/bin/pip freeze
