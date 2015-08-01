# Script for download, building and installing mozjs
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

    # related issues
    # https://bugzilla.mozilla.org/show_bug.cgi?id=1006275
    #jobs=`cat /proc/cpuinfo | grep 'processor' | wc | awk '{print $1}'`
    #jobs=$(($jobs+1))
    #make -j$jobs
    make -j1
    cd $CWD
}

function install () {
    cd $TEMP/js/js/src
    make install
    cp -v dist/include/js-config.h $INSTALL_PATH/include/mozjs-31/
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

