SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`
cd $SH
python3 -m virtualenv .venv
#       -m            name of your virtual env of your python app aka within this folder
