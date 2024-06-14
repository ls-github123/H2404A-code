# 异常捕获与处理
# 异常 -- 一个事件,在程序执行过程中发生,影响程序的正常执行
# python无法正常处理时就会发生异常
# list1 = []
# list1.add(123) # error: attribute

# list2 = [1,2,3]
# print(list2[4]) # error: index out of range

# 简单异常处理 --不影响后续程序的正常执行
# 语法 try:(可能会出现问题的代码)   except 出现的异常类型:(如果出现当前异常错误，则需要执行的代码块)
try:
    print(a)
except NameError:
    print('跟name有关')
print('其他程序正常执行')


# 多个异常处理(获取异常的信息描述)
# 第一种方式
try:
    list1 = [1,2,3]
    print(list1[20])
except IndexError:
    print('跟索引有关')
except NameError:
    print('跟name有关')
    
# 第二种方式
try:
    print(list2)
except (IndexError, NameError): # 缺点:处理比较局限
    print('检查输入数据')
    
# 获取异常错误信息
try:
    print(list2)
except (IndexError, NameError) as e: # 缺点:处理比较局限
    print(e) # 变量e为具体错误信息
    print('检查输入数据')
    

# 万能异常处理(捕获所有异常)
# Exception -->常规异常的基类 --> 包含所有的常规异常
# 语法格式: try: 可能会出现问题的代码  except Exception as e: print(e)

list1 = [1, 2, 3]
dict1 = {}
try:
    print(list1[2])
    print(dict1['name'])
    print('hhhhhh')
except Exception as e:
    print(e)
    
# 搭配else使用
list1 = [1 ,2, 3]
try:
    print(list1[2]) # 可能出现错误的代码
except Exception as e:
    print(e) # 代码运行中出现错误则执行except
else:
    print('hhhhh') # 执行正常则打印'hhhhh'


# 搭配finally使用
# (可与try单独搭配使用，但没有意义)
# 无论代码是否出现问题，都会在最后执行finally中的代码
# 一般用于处理必须执行的操作(如从文件中读取数据，无论数据读取是否成功，都必须执行关闭操作)
list1 = [1 ,2, 3]
try:
    print(list1[2]) # 可能出现错误的代码
except Exception as e:
    print(e) # 代码运行中出现错误则执行except
else:
    print('代码没有问题') # 执行正常则打印'代码没有问题'
finally:
    print('hhhhhhh') # 无论代码执行是否出现问题，都打印'hhhhhhh'


# try嵌套
# 嵌套：一层try异常处理中再嵌套另外一层try处理
import time
try:
    f = open('test.txt')
    try:
        content = f.readline()
        time.sleep(2)
        print(content)
    except Exception as e:
        print(e)
        print('读取文件出错')
    else:
        print('正常读取文件结束')
    finally:
        f.close()
        print('关闭文件')
except Exception as e:
    print(e)
    print('文件不存在')