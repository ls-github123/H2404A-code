# python-project 简易计算器
# 需求：让用户输入两个数以及运算符，输出这两个数运算的结果

def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    
    if y == 0 :
        return "除数不能为0"
    else:
        return x / y

if __name__ == "__main__": #常见的Python编程习惯，使得脚本既可以作为独立的可执行程序运行，也可以作为模块被导入到其他程序中使用
    try:
        num1 = float ( input ("请输入第一个数："))
        num2 = float ( input ("请输入第二个数："))
        operator = input ("请输入运算符（+、-、*、/）：")

        if operator == "+":
            result = add (num1, num2)
        
        elif operator == "-":
            result = subtract (num1, num2)
        
        elif operator == "*":
            result = multiply (num1, num2)
        
        elif operator == "/":
            result = divide (num1, num2)
        
        else:
            result = "无效的运算符"

        print("运算结果：", result)
    
    except ValueError:
        print("输入错误：请输入有效的数字")