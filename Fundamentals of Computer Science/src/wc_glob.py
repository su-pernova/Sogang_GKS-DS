import glob

def read_all(file_list):
   data = []
   for f in file_list:
      ifile = open(f, 'r', encoding='utf-8')
      data += ifile.read().split()
      ifile.close()
   return data

f_list = glob.glob('txt/*.txt')
all_data = read_all(f_list)
print(all_data)
