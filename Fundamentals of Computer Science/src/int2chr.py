# from computer view to human view
print(chr(0x3131), chr(12593))
assert(chr(0x3131) == 'ㄱ')
print(chr(0x314f))
print(chr(0xac00))
print(chr(0xd7a3), chr(55203))
print(chr(0xd7a3) == chr(55203))
assert chr(0xd7a3) == chr(55203), 'Both are same integer'

# from human view to computer view
print()
print(hex(ord('ㄱ')), ord('ㄱ'))
print(hex(ord('ㅏ')))
print(hex(ord('가')), ord('가'))
print(int(hex(ord('가')),16))
print(hex(ord('힣')), ord('힣'))
print(int(hex(ord('힣')),16))
