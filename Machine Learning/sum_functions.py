def sum_list(v):
    c=0
    for i in v:
        c=i+c
    return c

def sum_lists(list1,list2):
    gen_list=[]
    for i in range(len(list1)):
       gen_list.append(list1[i]+list2[i])
    return gen_list

def product_of_lists(list1,list2):
    gen_list=[]
    for i in range(len(list1)):
       gen_list.append(list1[i]*list2[i])
    return gen_list


def get_list_of_squares(v):
    square_list=[]
    for i in v:
        square_list.append(i**2)
    return square_list

# print(sum_list([1,2,3,20]))
# print(sum_lists([4,5,6],[7,8,9]))

