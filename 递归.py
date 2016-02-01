#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#antuor:Alan

###############非递归的函数,实现阶乘###################
# def df(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#
#     return result
#
# number = int((input('请输入一个正数:')))
# result = df(number)
# print(('%d的阶乘是: %d') % (number,result))

##############递归求阶乘##############################

# def df1(n):
#     if n == 1:
#         return 1
#     else:
#         return n*df1(n-1)
# number = int((input('请输入一个正数:')))
# result = df1(number)
# print(('%d的阶乘是: %d') % (number,result))

##############分解###################################
#df1(5) =5*df1(4)
    #df1(4) =4*df1(3)
        #df1(3) = 3*df1(2)
            #df1(2) = 2*df1(1)
                #df1(1) = return


###############递归算法###############分治算法#######
"""注意如果n数字过大,那么计算时间很长,
效率很慢,吃内存,35以上就很慢了"""

# def fab(n):
#     if n<1:
#         print('输入有误!')
#         return -1
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
#
# mon = int(input('请输入整数月份:'))
# result =  fab(mon)
# if result != -1:
#     print('总共有 %d 对兔子' % result)



######汉诺塔游戏######
def hanuo(n,x,y,z):
    if n==1:
        print(x ,'--->' ,z)
    else:
        hanuo(n-1,x,z,y) #将前n-1个盘子从x移动到y上
        print(x,'--->',z) #将最底下的的最后一个盘子从x移动到z上
        hanuo(n-1,y,x,z)#将y上的n-1个盘子移动到z上

n = int(input('请输入整数:'))
hanuo(n,'x','y','z')







