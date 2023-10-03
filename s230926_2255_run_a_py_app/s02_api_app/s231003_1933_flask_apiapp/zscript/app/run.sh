SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`  # SH aka SCRIPT_HOME
AH=`cd "$SH/../.." && pwd`  # AH aka APP_HOME

cd $AH
  FLASK_APP=src.app  ./.venv/bin/flask run
