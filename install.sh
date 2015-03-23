URL=https://people.mozilla.org/~sstangl/mozjs-31.2.0.rc0.tar.bz2
TEMP=temp
CWD=`pwd`

jobs=`cat /proc/cpuinfo | grep 'processor' | wc | awk '{print $1}'`
jobs=$(($jobs+1))

function download {
    mkdir -p $TEMP
    cd $TEMP
    wget -N $URL -o mozjs.tar.bz2
}

function build {
    tar -xjvf mozjs.tar.bs2 -C $1 --strip-components=1 && cd $1
    ./configure && make -j$jobs
}

for i in $@; do
    case $in in
        *)
            ;;
    esac
done;

download
build js
