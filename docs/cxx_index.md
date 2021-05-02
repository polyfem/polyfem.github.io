C++ Library
===========

![Build](https://github.com/polyfem/polyfem/workflows/Build/badge.svg)


PolyFEM in C++ uses modern CMake and is it cross-platform.

Compilation
-----------

All the C++ dependencies required to build the code are included. It should work on Windows, macOS and Linux, and it should build out of the box with CMake:

```sh
mkdir build
cd build
cmake ..
make -j4
```

On Linux `zenity` is required for the file dialog window to work. On macOS and Windows the native windows are used directly.


### Optional
The formula for higher order bases are optionally computed at CMake time using an external python script. Consequently, PolyFEM might requires a working installation of Python and some additional packages in order to build correctly:

- `numpy` and `sympy` (optional)
- `quadpy` (optional)

Usage
-----

The main executable, `./PolyFEM_bin`, can be called with a GUI or through a command-line interface. Simply run:

```sh
./PolyFEM_bin
```

A more detailed documentation can be found on the [tutorial](tutorial.md).
