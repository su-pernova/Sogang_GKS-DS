#coding: utf-8
filename='outlines.txt'
infile=open(filename, 'r', encoding='uft-8')
data = infile.read()
infile.close() #after reading, it can be closed
input('Read()... \n%s\npress any key ' %data)
splitted = data.split()
input('Split() with space.... \n%s \n press any key ' %splitted)
joined = '\t'.join(splitted) #'\t' is tab character
input('Join() with tab ... \n%s\npress any key ' %joined)
