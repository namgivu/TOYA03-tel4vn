SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
AH=`cd "$SH/../.." && pwd`
cd $AH
  ./.venv/bin/python3 ./src/app.py
