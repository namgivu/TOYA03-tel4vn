SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`  # SH aka SCRIPT_HOME
AH=`cd "$SH/../.." && pwd`  # AH aka APP_HOME

cd $AH
  FLASK_APP='src.app' ./.venv/bin/flask run  -p${PORT:-5000}
  #        =                      flask run  -p custom port  ref https://stackoverflow.com/a/41940807/248616
