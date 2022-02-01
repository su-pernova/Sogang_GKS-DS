#coding:utf-8

infile = open('out.txt','r')
lines = infile.readlines()
for line in lines:
    if '*' in line: continue
    if '\n' == line: continue
    print(line.strip())

infile.close()
