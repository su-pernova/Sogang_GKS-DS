import glob
from collections import Counter
import matplotlib.pyplot as plt
import mpl_han_fonts
mpl_han_fonts.set_Han_font()

def read_all(file_list):
   data = []
   for f in file_list:
      ifile = open(f, 'r', encoding='utf-8')
      data += ifile.read().split()
      ifile.close()
   return data

def draw_bar(w_list, c_list, img_fn = 'bar_of_han_words.png'):
   plt.bar(w_list, c_list, width=0.5)
   plt.ylabel('counts')
   plt.title('# of w(i)')
   plt.savefig(img_fn)
   plt.show()

f_list = glob.glob('news_data/*.txt')
all_data = read_all(f_list)
han_data = []
pure_han_data = []
from hangul_analyser import is_hangul_chr
for word in all_data:
   temp = 0
   for sylla in word:
      if is_hangul_chr(sylla):
         temp = 1
   if temp == 1:
      han_data.append(word)

#bar_of_han_words.png
w_c_list = Counter(han_data).most_common(10)
w_list = [w for w, _ in w_c_list]
c_list = [c for _, c in w_c_list]
draw_bar(w_list, c_list, 'bar_of_han_words.png')

for word in han_data:
   temp = 0
   for sylla in word:
      if is_hangul_chr(sylla):
         temp = 1
      else:
         temp = 0
         break
   if temp == 1:      
      pure_han_data.append(word)

#bar_of_pur_han_words.png
w_c_list = Counter(pure_han_data).most_common(10)
w_list = [w for w, _ in w_c_list]
c_list = [c for _, c in w_c_list]
draw_bar(w_list, c_list, 'bar_of_pur_han_words.png')
