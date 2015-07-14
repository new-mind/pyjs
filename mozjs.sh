URL=https://people.mozilla.org/~sstangl/mozjs-31.2.0.rc0.tar.bz2
TEMP=temp
CWD=`pwd`
INSTALL_PATH=$CWD/$TEMP/build

function download () {
    mkdir -p $TEMP
    cd $TEMP
    wget -N $URL -O mozjs.tar.bz2 --verbose
}

function extract () {
    mkdir -p $1
    tar -xvf mozjs.tar.bz2 -C $1 --strip-components=1 && cd ..
}

function build () {
    cd $TEMP/js/js/src/
    ./configure --prefix=$INSTALL_PATH

    jobs=`cat /proc/cpuinfo | grep 'processor' | wc | awk '{print $1}'`
    jobs=$(($jobs+1))
    make -j$jobs
    cd $CWD
}

function install () {
    cd $TEMP/js/js/src
    make install
    cd $CWD
}

for i in $@; do
    case $i in
        --install)
            install
            exit 0
            ;;
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

