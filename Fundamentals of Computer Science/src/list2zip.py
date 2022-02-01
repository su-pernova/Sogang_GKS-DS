#coding:utf-8

a_list = ['apple', 'orange', '*berry']
b_list = ['사과', '오렌지', '장과']

ab_list = [(pre, post) for pre, post in zip(a_list, b_list)]
ab_dict = dict(zip(a_list, b_list))

print('ab_dict = ', ab_dict)
print('ab_list = ', ab_list)



