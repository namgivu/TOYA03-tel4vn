SH=`cd $(dirname ${BASH_SOURCE:-$0}) && pwd`

cd $SH
docker build \
    -t mypython_i \
    .

echo
docker image ls | grep -E 'mypython_i|TAG'

echo
docker run mypython_i
