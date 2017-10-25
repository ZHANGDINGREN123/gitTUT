# coding=utf-8

from functools import wraps


# 1.装饰器的使用是通过@符号,放在函数上面
# 2.装饰器中定义的函数要使用*args, **kwargs的组合,并且在这个函数中执行原始函数的时候也要把*args, **kwargs传进去
# 3.需要使用functools.wraps在装饰器的函数上，把传进来的函数进行一个包裹，这样就不会丢失原来的函数__name__属性

# 装饰器实际上就是一个函数,它有两个特别之处：
    #1.参数是一个函数
    #2.返回值是一个函数

# 需求1；在打印run之前先打印一个hello world
# 需求2：在所有函数执行之前先打印一个hello world


def run():
    # 解决需求1
    print 'hello world'
    print 'run'

# 解决需求2
def my_log(func):
    @wraps(func)#解决装饰器偷换函数名称的代码(可通过注释观察print add.__name__的输出)
    def wrapper(*args, **kwargs):
        print 'hello world'
        func(*args, **kwargs)
    return wrapper
    # return wrapper()
    # 上行代码区别在于最后是否加()，如果加括号返回wrapper函数执行之后的结果，如果不加括号返回wrapper这个函数体。

# 加上@编译器就会把my_log当成装饰器来使用
@my_log
def run():
    print 'run'

# run => my_log(run):return wrapper => 即wrapper先执行 ：wrapper先执行print 'hello world'，再执行func, 而func代表的是run()函数：run函数执行print 'run'
# 因此运行run() 实际上就是运行wrapper()
run()




@my_log
def add(a, b):
    c = a + b
    print u'结果是:%s' % c

# add = my_log2(add) = wrapper
# 所以运行add(1, 2)就是运行wrapper(1, 2),但wrapper()无参数，若加上了参数run()运行就会出错，
# 因此这样操作wrapper(*args, **kwargs)：*args, **kwargs可以表示任何参数
add(1, 2)


# 将def add(a, b)上一行的@my_log注释掉，输出的是add这个函数的名称
# 不将def add(a, b)上一行的@my_log注释掉，输出的是wrapper这个函数的名称----->即add的名称被装饰器换成了wrapper，解决办法在第20行@wraps(func)
print add.__name__

