# C++ Library

![Build](https://github.com/polyfem/polyfem/workflows/Build/badge.svg)

PolyFEM in C++ uses modern CMake and is cross-platform.

## Compilation

All the C++ dependencies required to build the code are automatically downloaded through CMake. We test PolyFEM on macOS, Linux, and Windows, and it should build out-of-the-box with CMake:

```sh
mkdir build
cd build
cmake ..
make -j4
```

### Optional

Optionally, the formulas for higher-order bases can be computed at CMake time using a Python script. If you choose to do so, PolyFEM requires a working installation of Python and some additional packages to build correctly:

- `numpy` and `sympy` (optional)
- `quadpy` (optional)

## Usage

The main executable, `./PolyFEM_bin`, can as command-line interface. Simply run:

```sh
./PolyFEM_bin --help
```

More detailed documentation can be found in the [tutorial](tutorials/getting_started.md).
