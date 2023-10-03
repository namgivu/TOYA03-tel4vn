SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
AH=`cd "$SH/.." && pwd`
cd $AH
  # prepare .venv
  python3 -m pip install --upgrade pip
  python3 -m pip install virtualenv
  python3 -m             virtualenv .venv

  echo

  # install pkg
  ./.venv/bin/pip install -r ./requirements.txt

  echo
  ./.venv/bin/pip freeze
