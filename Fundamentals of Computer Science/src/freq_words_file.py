
def get_freq(infilename, outfilename):
    infile = open(infilename,'r')
    outfile = open(outfilename, 'w')
    lines = infile.read()
    freq_w = {'program':0,'is':0,'better':0}
    #You should fill out below.
    for w in lines.split():
        if ('program' == w): freq_w['program'] += 1
        if ('is' == w): freq_w['is'] += 1
        if('better' == w): freq_w['better'] += 1

    for k in freq_w:
        #outfile.write('%s:%s\n' %(k,str(freq_w[k])))
        outfile.write('%s:%d\n' %(k,(freq_w[k])))

    infile.close()
    outfile.close()

#You should fill out below.
get_freq("out3.txt","out3.txt.wc")



