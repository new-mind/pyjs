# Script for download, building and installing mozjs
URL=https://people.mozilla.org/~sstangl/mozjs-31.5.0.tar.bz2
TEMP=temp
CWD=`pwd`
INSTALL_PATH=`pwd $CWD/$TEMP/build`
set -x

function download () {
    echo ">> Download"
    mkdir -p $TEMP
    cd $TEMP
    wget -N $URL -O mozjs.tar.bz2 --verbose
}

function extract () {
    echo ">> Extract"
    mkdir -p $1
    tar -xf mozjs.tar.bz2 -C $1 --strip-components=1 && cd ..
}

function build () {
    echo ">> Configure"
    cd $TEMP/js/js/src/
    ./configure --prefix=$INSTALL_PATH --enable-debug
    if [ $? -ne 0 ]; then
        exit 1;
    fi

    # related issues
    # https://bugzilla.mozilla.org/show_bug.cgi?id=1006275
    #jobs=`cat /proc/cpuinfo | grep 'processor' | wc | awk '{print $1}'`
    #jobs=$(($jobs+1))
    #make -j$jobs
    echo ">> Make"
    make -j1
    cd $CWD
}

function install () {
    echo ">> Install"
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
        --path)
            echo $PATH:$INSTALL_PATH/bin
            exit 0
            ;;
        *)
            ;;
    esac
done;

