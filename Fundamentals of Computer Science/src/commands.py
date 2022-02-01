import os
os.system('date')
filename='out.txt'
os.system('ls -al %s' %filename)
input('%s is created/written in this moment. preass any key\n' %filename)
os.system('cat %s' %filename)
input('\nI saw the file content')
