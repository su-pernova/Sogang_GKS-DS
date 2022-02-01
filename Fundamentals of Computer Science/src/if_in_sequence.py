#coding:utf-8

b_list = ['apple','orange','*berry']
b_dict = {'apple':'사과','orange':'오렌지','*berry':'장과'}
b_tuple = ('apple','orange','*berry')

def have_all(w1, w2, sequence):
    if (w1 in sequence) and (w2 in sequence):
        return True
    else:
        return False

def have_one(w1,w2,sequence):
    if w1 in sequence:
        return True
    if w2 in sequence:
        return True
    return False

print('apple' in b_list)
print('melon' not in b_list)
print('사과' in b_dict)
print(have_all('apple','melon',b_list))
print(have_all('apple','orange',b_list))
print(have_one('apple','melon',b_tuple))

