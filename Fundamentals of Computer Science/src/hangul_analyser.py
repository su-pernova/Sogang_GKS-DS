#coding:utf-8
from Hangul_jaso import *
NUM_CHOSUNGS = len(CONSONANTs)
NUM_JOONGSUNGS = len(VOWELs)
NUM_JONGSUNGS = len(CONSONANTs_Ending)

FIRST_HANGUL_UNICODE = 0xAC00
LAST_HANGUL_UNICODE = 0xD7A3

def compose(chosung, joongsung, jongsung=''):
   if jongsung is None: jongsung = ''
   try:
      chosung_index = CONSONANTs.index(chosung)
      joongsung_index = VOWELs.index(joongsung)
      jongsung_index = CONSONANTs_Ending.index(jongsung)
   except Exception as e:
      print(e)
    
   return chr(0xAC00 + chosung_index * NUM_JOONGSUNGS * NUM_JONGSUNGS + joongsung_index * NUM_JONGSUNGS + jongsung_index)

def decompose(hangul_sylla):
   code = ord(hangul_sylla) - FIRST_HANGUL_UNICODE
   jongsung_index = int(code % NUM_JONGSUNGS)
   code /= NUM_JONGSUNGS
   joongsung_index = int(code % NUM_JOONGSUNGS)
   code /= NUM_JOONGSUNGS
   chosung_index = int(code)
   try:
      return(CONSONANTs[chosung_index], VOWELs[joongsung_index], CONSONANTs_Ending[jongsung_index])
   except Exception as e:
      print('input:', hangul_sylla, e)
	
if __name__ == "__main__":
   try:
      print(compose('ㄱ', 'ㅏ', 'ㄱ'))
      print(compose('ㄱ', 'ㅏ', ''))
      print(compose('ㅎ', 'ㅣ', 'ㅎ'))
      print(decompose('힣'))
      print(decompose('가'))
      print(decompose('각'))
   except Exception as e:
      print(e)
