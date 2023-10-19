# execute at :python_consoleapp folder
SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
flask_apiapp=`cd "$SH/../../s231003_1934_flask_apiapp" && pwd`
cd $flask_apiapp


echo -e "\n--- before" ; ./.venv/bin/pip freeze

# install :requests
echo
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/pip install flask

echo -e "\n--- after" ; ./.venv/bin/pip freeze
