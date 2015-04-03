URL=https://people.mozilla.org/~sstangl/mozjs-31.2.0.rc0.tar.bz2
TEMP=temp
CWD=`pwd`

jobs=`cat /proc/cpuinfo | grep 'processor' | wc | awk '{print $1}'`
jobs=$(($jobs+1))

function download {
    mkdir -p $TEMP
    cd $TEMP
    set -x
    wget -N $URL -O mozjs.tar.bz2 --verbose
    set +x
}

function build {
    mkdir -p $1
    set -x
    tar -xvf mozjs.tar.bz2 -C $1 --strip-components=1 && cd ..
    set +x
}

for i in $@; do
    case $in in
        *)
            ;;
    esac
done;

download
build js
