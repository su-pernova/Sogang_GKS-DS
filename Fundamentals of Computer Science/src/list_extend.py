#coding:utf-8
filename='outlines.txt'
infile=open(filename, 'r', encoding='utf-8')
lines = infile.readlines()
inflie.close()
input('Readlines()... \n%s\n' %lines)
tokens = []
for l in lines:
   l = l.strip()
   print('stripped: ', l)
   splitted = l.strip().split('.')
   print('split with .: ', splitted)
   tokens.extend(splitted)
   input('next')

print('All tokens are extended.', tokens)
