#coding:utf-8
filename='outlines.txt'
infile=open(filename, 'r', encoding='utf-8')
lines = infile.readlines()
infile.close()
input('Readlines()...\n%s\n' %lines)
for l in lines:
   print('before:', 1) #linefeed is in the end
   l = l.strip()
   print('stripped:', l)
   print('split with .: ', l.split('.'))
   print('split with tab: ', l.split('\t'))
   print('split with ,: ', l.split(','))
   input('next')
