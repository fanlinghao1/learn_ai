
"""
函数的学习
1, 函数的定义
def 函数名称（参数）：
    函数体
    return[结果]

2，调用函数，使用函数名称（） 的方式调用

3，匿名函数 lambda,使用，lambda x:x+1
4、形参、实参（定义函数的参数是形参，调用函数的时候传的函数为实参）
5、参数的设置：
    位置参数（固定位置，根据位置来输出参数）
    指定参数（指定参数的名称，通过名称来复制参数，而和位置没有关系）
    默认参数（在定义参数的时候，直接默认给个参数，如果没有赋值，则直接使用默认参数）
    默认参数后面的参数必须也是默认参数，具有默认参数的值
6、不定长参数：
    不定长参数分为位置函数以及变量分参数，其中位置参数使用*，自定义参数使用**
    例如：
    def address_book(name,*telephone,alice_name,**customer):

7、函数的内省功能，通过dir(函数名) 的方法来获得
8、 函数的返回，函数的返回使用return 进行返回，return 返回可以返回变量，函数、等值
    函数在调用自己的时候就会就行递归，算法一般是有、判断、循环、递归 组成的复杂算法

9、函数的作用域
LEGB原则
L  Local  本地变量
E  Enclosed 闭包变量
G  Global 全局变量
B  Builtin  内置变量

闭包：函数内 再次定义一个函数，就是闭包
"""
"""
#简单定义一个函数，并使用匿名函数形成相对应的功能
def foo(x):
    x +=1
    return x

print(foo(100))

add_1 = lambda x:x+1
print(add_1(100))


#使用位置参数、默认参数，以及指定参数来定义一个函数

def fun2(a1_name,a2_name=34,a3_name=45):
    print(a1_name)
    print(a2_name)
    print(a3_name)

#调用函数
fun2(12,3)


#不定长参数的使用

def address_book(name,*telphone,alices='no',**customer):
    '''
    这个函数主要用于对不定长参数的测试
    :param name:
    :param telphone:
    :param alices:
    :param customer:
    :return:
  '''
    print(f"name:{name},telphone:{telphone},alices:{alices},customer:{customer}")

address_book('we',123,345,hone='dasda',alices='er')

print(address_book.__doc__)


## -----------------------函数return 返回————————————————————————


def foo2():
    return  'das'

def foo3():
    return foo2()

var = foo3()
print(var)

## 例如递归的形式函数
def test(num):
    if num ==1 or num==0 :
        return 1
    return num*test(num-1)

vre = test(5)
print(vre)
"""

# 闭包
def fun_out():
    var_out = 1
    def fun_in():
        return var_out
    return fun_in

print(fun_out()())

#装饰器：装饰器就是将函数使用闭包的形式来调用

import time
##python 自带装饰器

from functools import wraps

def time_it(func):
    #调用系统自带的装饰器 wraps 方式参数的函数名称被改变
    @wraps(func)
    def wrapper():
        start_time = time.time()
        print('开始执行func函数')
        func()
        print('结束执行func函数')
        end_time = time.time()
        print(f'函数一共执行了{int(end_time - start_time)}s')
    return wrapper


@time_it  # 这个方式就是将函数time_it作为装饰器的形式
# 就是在这个函数的基础上装饰上以上函数
def work():
    print('开始执行时间测试')
    time.sleep(1)
    print('结束执行时间测试')

print(work.__name__)
