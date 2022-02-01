#2020.06
#writer: Kim Sumi

import platform
print(platform.uname())
print(platform.uname().system)

import psutil
print(psutil.virtual_memory())
print(str(psutil.virtual_memory().total/1024.0**3) + 'GB')
