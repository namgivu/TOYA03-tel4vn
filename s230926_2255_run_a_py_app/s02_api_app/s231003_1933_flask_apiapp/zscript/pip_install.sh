SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`  # SH aka SCRIPT_HOME
AH=`cd "$SH/.." && pwd`  # AH aka APP_HOME

cd $AH

# prepare .venv
python -V
python -m pip install --upgrade pip
python -m pip install --upgrade virtualenv
python -m virtualenv .venv

echo

# install packages
./.venv/bin/pip install -r requirements.txt

echo
./.venv/bin/pip freeze | grep -E 'Flask|requests|gunicorn|python-dotenv'
