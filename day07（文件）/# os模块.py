# os模块  -- 对文件操作
import os
# 对文件的操作
# rename() -- os.rename(old, new) 修改指定文件名 或 文件路径变更
   # os.rename('uiser_file.txt','user_file.txt')
# remove()  -- 删除指定文件
  # os.remove('user_account.txt')

# 创建文件夹
# os.midir() -- 创建单级空目录
  # os.mkdir('user_dict/黄子/媛子')

# makedirs() -- 创建多级空目录
# os.makedirs()
  # os.makedirs('张buff的鱼塘/(杜佳琪/王馨瑶/范思悦/刘思莹/刘佳丽/周佳琪/黄子)')

# rmdir() -- 删除单级空目录
# os.rmdir()
 # os.rmdir('user_dict/黄子/媛子')

# removedirs() -- 删除多级空目录
# os.removedirs()
# os.removedirs('../2024.6.5（文件）/张buff的鱼塘/杜佳琪/王馨瑶/范思悦/刘思莹/刘佳丽/周佳琪/黄子')


# listdir()  os.listdir(要罗列的目录路径)
# 不指定参数，默认获取当前文件所在的父级目录下所有的文件
# 获取指定目录中所有的文件(包括隐藏文件)
 # print(os.listdir('../'))

# getcwd()
# 语法:os.getcwd()
# 作用：获取当前文件所有的父级路径(从盘符开始)
# print(os.getcwd())