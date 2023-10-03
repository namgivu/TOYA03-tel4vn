SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`  # SH aka SCRIPT_HOME
AH=`cd "$SH/../.." && pwd`  # AH aka APP_HOME

cd $AH
  # ref https://stackoverflow.com/a/41940807/248616
  ./.venv/bin/gunicorn -b 0.0.0.0:${PORT:-3000}  src.app:app
  #                    -b                               :app app=Flask() instance in module src.app
