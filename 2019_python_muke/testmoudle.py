# import mymoudle01
# import mymoudle02.mymoudle02
# print(mymoudle01.modulea)
# print(mymoudle02.mymoudle02.moduleb) # packagename.modulename.varname
from mymoudle01 import modulea
from mymoudle02.mymoudle02 import moduleb
import mymoudle02  # excute init.py

print(modulea)
print(moduleb)
print(mymoudle02.sys.path)


