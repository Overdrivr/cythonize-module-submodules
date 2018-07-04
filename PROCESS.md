# Research process to achieve successful compilation and packaging

## Step 1 - Commit 8180d914c8a211ce051104b78114af542e81b5f3

Fails with the following message:

```
LINK : error LNK2001: unresolved external symbol PyInit___init__
build\temp.win-amd64-3.5\Release\build\mypkg\__init__.cp35-win_amd64.lib : fatal error LNK1120: 1 unresolved externals
```

Apparently, that's because I am trying to compile `__init__.py` files.
Modifying the setup_all to remove them.
