#learnt1
#must include : =, %, !=, str(), int(), find()
Apple = 1234
Banana = 4321
print("\nApple = %d" %(Apple))
print("Banana = %d\n" %(Banana))

if(Apple != Banana):
    print("Apple = %d, Banana = %d" %(Apple, Banana))
    print("Apple and Banana are different.\n")
    Apple = str(Apple)
    Banana = str(Banana)
else: print("Apple and Banana are same.\n")

Apple = str(Apple)
Banana = str(Banana)
if(-1<Apple.find('1')): print('Apple has 1.')
if(-1<Banana.find('1')): print('Banana has 1.\n')
if(-1<Apple.find('1') and -1<Banana.find('1')):
    print('Apple and Banana both have 1.')
    Apple = int(Apple)
    Banana = int(Banana)
    if(Apple != Banana): print('But they are not same.\n')
