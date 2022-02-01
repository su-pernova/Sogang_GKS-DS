#coding:utf-8
from Hangul_jaso import *

print('한글 자소의 index를 봅시다.')
print('첫소리:초성')
for i, each in enumerate(CONSONANTs):
    print(CONSONANTs.index(each), CONSONANTs[i])
input('가운뎃소리:중성')
for i, each in enumerate(VOWELs):
    print(VOWELs.index(each), VOWELs[i])
input('끝소리:종성')
for i, each in enumerate(CONSONANTs_Ending):
    print(CONSONANTs_Ending.index(each), CONSONANTs_Ending[i])
