infile = open('input.txt', 'r')
outfile = open('korea_pos_freq.txt', 'w')
lines = infile.read()

freq = 0
for i, w in enumerate(lines.split()):
    if w.lower().find('korea') != -1 :
        freq = freq + 1
        outfile.write(str(i) + ':' + str(w) + '\n')

outfile.write(str(freq))
infile.close()
outfile.close()
