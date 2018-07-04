from mypkg.mysubpkg1.main import *
from mypkg.mysubpkg2.main import *

def mypkg_fn():
    print('mypkg_fn called')
    mysubpkg1_fn()
    mysubpkg2_fn()

if __name__ == '__main__':
    mypkg_fn()
