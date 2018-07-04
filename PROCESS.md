# Research process to achieve successful compilation and packaging

## Step 1 - Commit 8180d914c8a211ce051104b78114af542e81b5f3

Fails with the following message:

```
LINK : error LNK2001: unresolved external symbol PyInit___init__
build\temp.win-amd64-3.5\Release\build\mypkg\__init__.cp35-win_amd64.lib : fatal error LNK1120: 1 unresolved externals
```

Apparently, that's because I am trying to compile `__init__.py` files.

NEXT : Modifying the setup_all to remove them.

## Step 2 - Commit 3d0da8c2eb9e23b95e49e8a40e1aed3e78c3c433

By using the `glob` package, and removing the `__init__.py` files from the build process, a wheel archive could be successfully generated.

However, two surprising things:

  - Running `python test.py` after installing the wheel works, although only `mypkg.main` ended up in the list of files to compile
  - Inside the wheel file, there are only three files:

![./screens/screen_1.PNG](./screens/screen_1.PNG)

Yet, here is what happens when running `python test.py`:

```
$ python test.py
mypkg_fn called
mysubpkg1_fn called
mysubpkg2_fn called
```

Each module is properly called. It looks like the submodules were properly compiled. WEIRD.

NEXT : Modifying package code to determine if running from python or compiled sources
