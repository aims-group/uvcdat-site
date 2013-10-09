##Installing UVCDAT from the Source

Building UV-CDAT with CMake is supported on Max OSX and Linux platforms. The only prerequisites are downloading and instaling CMake 2.8.8 or later. You can get CMake from [http://cmake.org/cmake/resources/software.html](http://cmake.org/cmake/resources/software.html).

####To build CMake with the gui do:

    tar xvf cmake-2.8.9.tar.gz
    cd cmake-2.8.9
    ./configure --prefix=/install/directory/cmake-2.8.9 --qt-gui
    gmake install

####Prerequisites and Install Tips

See UV-CDAT [Requirements](https://github.com/UV-CDAT/uvcdat/wiki/System-Requirements)

If you do not install QT in a standard location, don't forget to setup the "QT_QMAKE_EXECUTABLE" in the ccmake step bellow.

####Getting Started

Once you have CMake installed on your system you can begin configuring UVCDAT with CMake. To do this you first need to get the source using git by running the following:


    git clone git://github.com/UV-CDAT/uvcdat.git
    
    or
    
    git clone https://github.com/UV-CDAT/uvcdat.git
    
    or if you have a github account
    
    git clone git@github.com:UV-CDAT/uvcdat.git
    
    Alternatively you can download a zip file of the repo from:
    
    https://github.com/UV-CDAT/uvcdat


Adjacent to your source checkout you should make a build directory. From within the build directory we invoke either ccmake which uses an ncurses interface (great when you only have terminal acces) or cmake-gui which launches CMake's Qt gui interface:

    mkdir build-uvcdat
    cd build-uvcdat
    cmake-gui ../uvcdat

Alternatively you can use the command line only configuration:

    ccmake ../uvcdat

The cmake-gui window (or a text version of it if you used ccmake) will appear. Press the **Configure** button (or C if you're using ccmake). If you are behind a firewall in which the git:// protocol is blocked, you should set **GIT_PROTOCOL** CMake variable to use [http://]() instead. CMake will checkout all dependencies during this step and this might take a while. Make sure you have an internet connection during the Configure and Building process. The window will look like this:

![alt text](http://uvcdat.llnl.gov/media/images/uv-cdat_cmake_gui1.png)

The CMake interface provides you with a number of options, particularly telling the build system to build a particular package or to use a system versions. The safest bet it to not adjust any option. CMake will install uv-cdat in an **install** directory adjacent to the source and build directories.

Press **Configure** again (or c if you're using ccmake) until you don't see anymore "red highlighte dlines" (or "starred lines" if using ccmake) and then **Generate** (or g if you're using ccmake). Close the cmake-gui window (or press Q if you're using ccmake). Go back to your terminal and run make. It should start building.

    make

After the process finishes, you have to setup your environment. Under bash:

    source /path/to/cmake/install/bin/setup_cdat.sh

Or if you are using (t)csh:

    source /path/to/cmake/install/bin/setup_cdat.csh


####Special Builds

During the ccmake step there are a few options you might want to tune for easier/faster build.

* **CDAT_BUILD_ESGF**: turning this ON will be a SUPER light weight version of UV-CDAT w/o GUI or Graphics, and almost no packages, it is the equivalent of the old --cdms-only, or the (independently maintained) CDATLite
* **CDAT_BUILD_GRAPHICS**: turning this OFF will disable building anything graphics related (including GUI)
* **CDAT_BUILD_GUI**: turning this off will turn off anything gui related (TKinter, Vistrails, UVCDAT GUI, Paraview, VisIT)
* **CDAT_BUILD_PARALLEL**: turning this off will disable openmpi/mpi4py features

####Testing matplotlib

Make sure matplotlib was installed by running python (make sure you have set the PATH variable to point to UV-CDAT python) and import matplotlib:

    python
    import matplotlib
    import pylab

If the comands above didn't raise any errors, proceed to the "Running UV-CDAT" section. Else, install matplotlib:

    mkdir matplotlib_git
    cd matplotlib_git
    git clone git://github.com/matplotlib/matplotlib.git #or https://github.com/matplotlib/matplotlib.git
    cd matplotlib
    python setup.py install

####Running UV-CDAT

After sourcing the setup_cdat.sh as mentioned above:

    uvcdat

All packages should be loaded automatically and you should see the window below:

![alt text](http://uvcdat.llnl.gov/media/images/uv-cdat_new_window.png) 
