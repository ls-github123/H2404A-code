# 2.创建一个雇员表employ
import pymysql
class Database:
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host = '',
                port = 3306,
                user = 'root',
                password = '',
                database = 'H2404A',
                charset = 'utf8'
                )
            print('数据库连接成功')
        except Exception as e:
            print(f'数据库连接失败!错误信息:{e}')
        else:
            self.c1 = self.con.cursor()
            print('游标对象建立成功')
    def select_sql(self,sql): # 执行查询功能SQL语句,返回相关数据
        result_list = []
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'查询指令({sql})执行成功,提交数据库')
            results = self.c1.fetchall()
            for result in results:
                result_list.append(result)
            return result_list
        except Exception as e:
            print(f'错误(ERROR):{e}')
            self.con.rollback()
            print(f'查询指令({sql})执行失败,回滚数据!')
            
    def excute_sql(self,sql):# 执行增删改功能SQL语句,不返回数据
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'非查询指令({sql})执行成功,提交数据库')
        except Exception as e:
            print(f'错误(ERROR):{e}')
            self.con.rollback()
            print(f'非查询指令({sql})执行失败,数据回滚!')
    
data = Database()
sql1 = """
-- 1.创建一个雇员表employ
CREATE TABLE employ\
(id SMALLINT PRIMARY KEY AUTO_INCREMENT,\
name VARCHAR(5) UNIQUE,\
sex ENUM('男', '女', '保密') DEFAULT '男',\
s_name ENUM('高级工程师', '助工', '工程师') NOT NULL,\
birthday DATE NOT NULL,\
money SMALLINT NOT NULL);
"""
data.excute_sql(sql1)

sql2 = """
-- 2.向表中添加数据
INSERT INTO employ VALUES\
(1001, '张三', '男', '高级工程师', '1975-10-17', 13000),\
(0, '李小四', '女', '助工', '1985-01-26', 6600),\
(0, '王五', '男', '工程师', '1978-02-13', 9500),\
(0, '赵六子', '男', '工程师', '1979-12-14', 8000),\
(0, '田七', '保密', '工程师', '1977-09-16', 10000),\
(0, '胡八', '女', '助工', '1988-06-06', 5000);
"""
data.excute_sql(sql2)

sql3 = """
-- 3.查询不同性别的平均工资、最高薪资
SELECT sex, ROUND(AVG(money), 2), MAX(money) FROM employ GROUP BY sex;
"""
print(f'3.查询不同性别的平均工资、最高薪资为:{data.select_sql(sql3)}')

sql4 = """
-- 4.查询不同性别的人数及对应的名字
SELECT sex, COUNT(*), GROUP_CONCAT(name) FROM employ GROUP BY sex;
"""
print(f'4.查询不同性别的人数及对应的名字为:{data.select_sql(sql4)}')

sql5 = """
-- 5.查询人数大于等于2人的性别,及该性别人员的工资总和
SELECT sex, SUM(money) FROM employ GROUP BY sex HAVING COUNT(*) >= 2;
"""
print(f'5.查询人数大于等于2人的性别,及该性别人员的工资总和为:{data.select_sql(sql5)}')

sql6 = """
-- 6.查询不同岗位的人数、平均薪资、最高薪资及人员名字
SELECT s_name, COUNT(*), ROUND(AVG(money), 2), MAX(money), GROUP_CONCAT(name) FROM employ GROUP BY s_name;
"""
print(f'6.查询不同岗位的人数、平均薪资、最高薪资及人员名字为:{data.select_sql(sql6)}')

sql7 = """
-- 7.统计80年以前出生的所有人的工资总和
SELECT SUM(money) FROM employ WHERE birthday < '1980-01-01';
"""
print(f'7.统计80年以前出生的所有人的工资总和为:{data.select_sql(sql7)}')

sql8 = """
-- 8.查询表中姓名和性别，要求字段名以中文的形式展示
SELECT name AS 姓名, sex AS 性别 FROM employ; 
"""
print(f'8.查询表中姓名和性别，要求字段名以中文的形式展示为:{data.select_sql(sql8)}')

sql9 = """
-- 9.查询出表中所有的工程师
SELECT * FROM employ WHERE s_name = '工程师';
"""
print(f'9.查询出表中所有的工程师为:{data.select_sql(sql9)}')

sql10 = """
-- 10.查询出表中197几年出生的所有人的姓名
SELECT name FROM employ WHERE birthday LIKE '197%';
"""
print(f'10.查询出表中197几年出生的所有人的姓名为:{data.select_sql(sql10)}')

sql11 = """
-- 11.正则查询姓王的人的职位
SELECT name, s_name FROM employ WHERE name RLIKE '^王.*$';
"""
print(f'11.正则查询姓王的人的职位为:{data.select_sql(sql11)}')

sql12 = """
-- 12.查询出工资高于6000的人的姓名和职位以及对应工资
SELECT name, s_name, money FROM employ WHERE money > 6000;
"""
print(f'12.查询出工资高于6000的人的姓名和职位以及对应工资为:{data.select_sql(sql12)}')

sql13_1 = """
-- 13_1.去重查询所有性别
SELECT DISTINCT sex FROM employ;
"""
print(f'13_1.去重查询所有性别为:{data.select_sql(sql13_1)}')

sql13_2 = """
-- 13_2.分组查询所有性别
SELECT sex FROM employ GROUP BY sex;
"""
print(f'13_2.分组查询所有性别为:{data.select_sql(sql13_2)}')