# Cythonizing (Compiling like C code) a package and/or its submodules

The goal of this repository is to test cythonizing a package and/or its submodules,
to make it harder to reverse engineer the codebase and eventually make it run faster.
Indeed, after compiling it with cython, the generated archive no-longer contains
python code, and requires a tedious deassembly step that will make it marginally
harder to figure out what it is doing.

The requirements was to setup a build process that does not need to change the
python codebase.

See [PROCESS.md](./PROCESS.md) for details about how I came to the final version of the setup.py

Greatly inspired by [this article](https://bucharjan.cz/blog/using-cython-to-protect-a-python-codebase.html) from Jan Buchar 

# Utilisation

It is recommended to test this in a virtual environment.
We will be using anaconda to manage the virtual env (simply called `cython`).
Create the environment (only once):
```
conda create -n cython python=3.5
```

Activate it (everytime you want to test this repo):
```
activate cython
```

Install cython in environment (only once):
```
pip install cython
```

## Building the code

For cythonizing the entire package and subpackages:
```
python setup_all.py bdist_wheel
```

## Testing it

```
pip install dist/mypkg-0.1.0-cp35-cp35m-win_amd64.whl
python test/test.py
```
