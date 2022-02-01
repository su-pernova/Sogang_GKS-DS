#coding:utf-8

#'According to Unicode plate order')
# 'Jaeum:'
CONSONANTs = ['ㄱ','ㄲ','ㄴ','ㄷ', 'ㄸ','ㄹ','ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ','ㅈ','ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# Moeum:
VOWELs = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ','ㅚ','ㅛ','ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# Jaeum for final
CONSONANTs_Ending = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ','ㄻ','ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ','ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

if __name__ == "__main__":
    print("Contemporary Hangeul letters(Jamo)")
    print('Jaeum for first:', CONSONANTs)
    print('Moeum for middle:', VOWELs)
    print('Jaeum for last:', CONSONANTs_Ending)
    print(len(CONSONANTs), len(VOWELs), len(CONSONANTs_Ending))
