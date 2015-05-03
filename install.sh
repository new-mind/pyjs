URL=https://people.mozilla.org/~sstangl/mozjs-31.2.0.rc0.tar.bz2
TEMP=temp
CWD=`pwd`

function download {
    mkdir -p $TEMP
    cd $TEMP
    set -x
    wget -N $URL -O mozjs.tar.bz2 --verbose
    set +x;
}

function extract {
    mkdir -p $1
    set -x
    tar -xvf mozjs.tar.bz2 -C $1 --strip-components=1 && cd ..
    set +x;
}

function build {
    cd $TEMP/js/js/src/
    PYTHON=python2.7.5 ./configure

    jobs=`cat /proc/cpuinfo | grep 'processor' | wc | awk '{print $1}'`
    jobs=$(($jobs+1))
    make -j$jobs
    cd $CWD
}

for i in $@; do
    case $i in
        --build)
            build
            exit 0
            ;;
        --download)
            download
            extract js
            exit 0
            ;;
        *)
            ;;
    esac
done;

