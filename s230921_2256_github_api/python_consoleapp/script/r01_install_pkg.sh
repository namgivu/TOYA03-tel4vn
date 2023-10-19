# execute at :python_consoleapp folder
SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
python_consoleapp=`cd "$SH/../../python_consoleapp" && pwd`
cd $python_consoleapp


echo '--- before'; ./.venv/bin/pip freeze

# install :requests
./.venv/bin/pip install requests

echo '--- after' ; ./.venv/bin/pip freeze
