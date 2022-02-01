import glob
from collections import Counter
import matplotlib.pyplot as plt

def wc_from_file(file_list):
   data = []
   for f in file_list:
      ifile = open(f, 'r', encoding='utf-8')
      data += ifile.read().split()
      ifile.close()
   
   wc_list = Counter(data).most_common(10)
   w_list = [w for w,_ in wc_list]
   c_list = [c for _,c in wc_list]

   return w_list, c_list

f_list = glob.glob('news_data/*.txt')
w_list, c_list = wc_from_file(f_list)

def draw_bar(w_list, c_list):
   plt.bar(w_list, c_list, width = 0.5)
   plt.ylabel('counts')
   plt.show()

draw_bar(w_list, c_list)
