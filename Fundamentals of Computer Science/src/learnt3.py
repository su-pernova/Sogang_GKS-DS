#learnt3
#must include : udf, list comprehension, zip(), enumerate()
def making_list(size):
    new_list = [i for i in range(size)]
    return new_list

new_list_1 = making_list(5)
new_list_2 = making_list(5)
print("\nnew_list_1 : ", new_list_1)
print("new_list_2 : ", new_list_2,"\n")

for a, b in enumerate(zip(new_list_1, new_list_2)):
    print("Index : %d" %a)
    print(">> values of (new_list_1, new_list_2) = ", b, "\n")
