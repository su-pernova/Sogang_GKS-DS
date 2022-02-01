#learnt2
#must include : read(), write(), split(), join(), extend()
fp = open("new_file.txt",'w')
fp.write("I like python")
fp.close()

fp = open('new_file.txt','r')
f = fp.read()
print(f)

f_words = f.split()
print('~'.join(f_words))

very = ['~','!','~','!']
f_words.extend(very)
print('~'.join(f_words))
