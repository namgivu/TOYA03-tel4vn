SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`  # SH aka SCRIPT_HOME
AH=`cd "$SH/../.." && pwd`  # AH aka APP_HOME

cd $AH
  PORT=${PORT:-3000} ./.venv/bin/python "$AH/src/app.py"
