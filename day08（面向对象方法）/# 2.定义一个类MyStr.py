# 2、 定义一个类MyStr在这个类里编写5个实例方法：
# 1)show_dict_len()
# 	定义一个字典dict1 = {“name”:”张三丰”,”phone”:”120”,”address”:”上海虹桥”}
#   整合字典，判断字典的值长度是否大于2，如果大于2则仅保留前两位并重新赋值给原来的键，返回整合后的字典
# 2)func()
# 	将字符串str3 = “xcfjvdhdnaohbead”当做参数传入，将字符串中的个单个字符作为字典的键存入
#   字典的值为该字符在整个字符串中出现的次数
# 3)func1()
# 	将字符串str4 = “hello python,inner outer,student beautiful”当作参数传入，获取字符串中的长度最长的单词及该单词的长度
# 4)func2()
# 	a = "4567iuytreaAsmr3idd4bgs7Dlsf9eAF" 可以打印出该字符串中所有数字的个数以及数字的和，字母的个数
# 5)func3()
# 	str2 = ‘i am a student，123456789’ 输出‘12346789 student a am i’，注意是单词位置颠倒，而不是字母位置颠倒

class MyStr:
    def __init__(self, str):
        self.str = str
        
    def ShowDictLen(self): # (1)
        new_dict = {}
        for k, v in self.str.items():
            if len(v) > 2:
                new_dict[k] = v[:2]
        return f'1.重新整合后的字典为:{new_dict}'
    
    def func(self): # (2)
        str_dict = {}
        for char in self.str:
            str_dict[char] = self.str.count(char)
        return f'2.重新整合后的字典为:{str_dict}'
    
    def func1(self): # (3)
        word_list = []
        max_word_list = []
        str_repalce = self.str.replace(',',' ')
        for char in str_repalce.strip().split(' '):
            word_list.append(char)
        for max_word in word_list:
            max_word_list.append(len(max_word))
        if len(char) == max(max_word_list):
            print(f'3.字符串:{self.str}中最长的单词为:{char}, 长度为:{len(char)}')
            
    def func2(self): # (4)
        num_list = []
        alpha_list = []
        for char in self.str:
            if char.isdigit():
                num_list.append(int(char))
            elif char.isalpha():
                alpha_list.append(char)
        print(f'4.字符串{self.str}中,数字的个数为:{len(num_list)} 个,所有的数字和为:{sum(num_list)},字母的个数为:{len(alpha_list)}个')
    
    def func3(self): # (5)
        char_list = []
        str_replace = self.str.replace(',',' ')
        for char in str_replace.strip().split(' '):
            char_list.append(char)
        str5 = ' '.join(char_list[::-1])
        print(f'5.字符串{self.str} 单词位置颠倒后输出为:{str5}')


# 调用
# (1)
dict1 = {'name':'张三丰','phone':'120','address':'上海虹桥'}
ShowDictLen = MyStr(dict1)
print(ShowDictLen.ShowDictLen())

# (2)
str3 = 'xcfjvdhdnaohbead'
Func = MyStr(str3)
print(Func.func())

# (3)
str4 = 'hello python,inner outer,student beautiful'
Func1 = MyStr(str4)
Func1.func1()

# (4)
a = '4567iuytreaAsmr3idd4bgs7Dlsf9eAF'
Func2 = MyStr(a)
Func2.func2()

# (5)
str2 = 'i am a student,123456789'
Func3 = MyStr(str2)
Func3.func3()