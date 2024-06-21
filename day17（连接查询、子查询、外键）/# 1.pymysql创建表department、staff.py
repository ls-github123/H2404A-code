# 1.pymysql创建表department、staff
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
            print(f'数据库连接{self.con}建立成功')
        except Exception as e:
            print(f'数据库连接失败,错误信息:{e}')
        else:
            self.c1 = self.con。cursor()
            print(f'游标对象{self.c1}建立成功')
    
    def excute_sql(self, sql): # sql单向执行语句,不返回查询数据
        try:
            self.c1。execute(sql)
            self.con。commit()
            print(f'非查询指令({sql})执行成功')
        except Exception as e:
            print(f'错误(Error):{e}')
            self.con。rollback()
            print(f'非查询指令{sql}执行失败,数据回滚!')
    
    def select_sql(self, sql): # sql查询语句,返回查询数据
        SelectList = [] # 定义一个空列表，存放查询返回的数据
        try:
            self.c1。execute(sql)
            self.con。commit()
            print(f'查询指令({sql})执行成功,提交数据库')
            results = self.c1。fetchall() # 返回查询到的全部数据
            for result in results:
                SelectList.append(result) # 将回传的数据依次存入列表
            return SelectList # 输出列表数据
        except Exception as e:
            print(f'错误(Error):{e}')
            self.con。rollback()
            print(f'查询指令({sql})执行失败,数据回滚!')

data = Database()
sql1 = """
-- 1.创建部门表department
CREATE TABLE department(
    id TINYINT PRIMARY KEY AUTO_INCREMENT,
    name CHAR(3) NOT NULL UNIQUE);
"""
data.excute_sql(sql1)

sql2 = """
-- 2.为部门表添加数据
INSERT INTO department VALUES\
(1, '开发部'),
(2, '市场部'),
(3, '财务部'),
(4, '公关部');
"""
data.excute_sql(sql2)

sql3 = """
-- 3.创建员工表staff,并给字段dept_id设置外键约束
CREATE TABLE staff(
    id TINYINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(3) NOT NULL,
    gender ENUM('男', '女') DEFAULT '男' NOT NULL,
    salary DECIMAL(4,0) NOT NULL,
    join_date DATE NOT NULL,
    dept_id TINYINT NOT NULL,
    FOREIGN KEY(dept_id) REFERENCES department(id));
"""
data.excute_sql(sql3)

sql4 = """
-- 4.为员工表添加数据
INSERT INTO staff VALUES\
(1, '高胜寒', '男', 7200, '2013-02-24', 1),\
(0, '齐眉', '男', 3600, '2010-12-02', 2),\
(0, '程松柏', '男', 9000, '2008-02-02', 2),\
(0, '谭宁', '女', 5000, '2015-10-07', 3),\
(0, '许子乡', '女', 4500, '2011-03-14', 1),\
(0, '周青辰', '男', 6000, '2012-07-14', 2);
"""
data.excute_sql(sql4)

sql5 = """
SELECT d.name, s.* FROM staff AS s INNER JOIN department AS d ON s.dept_id = d.id HAVING s.name LIKE '___';
"""
print(f'5.查询名字是三个字的员工的信息为:{data.select_sql(sql5)}')

sql6 = """
SELECT * FROM staff WHERE join_date >= '2012-01-01';
"""
print(f'6.查询2012年以及以后入职的员工的信息为:{data.select_sql(sql6)}')

sql7 = """
SELECT gender, COUNT(*), GROUP_CONCAT(name) FROM staff GROUP BY gender;
"""
print(f'7.查询不同性别的人数及人的名称为:{data.select_sql(sql7)}')

sql8 = """
SELECT d.name, ROUND(AVG(s.salary), 2) FROM staff AS s INNER JOIN department AS d ON s.dept_id = d.id GROUP BY d.name HAVING AVG(s.salary) >= 6000;
"""
print(f'8.查询平均薪资大于等于6000的部门名称和平均薪资为:{data.select_sql(sql8)}')

sql9 = """
SELECT d.name, s.* FROM staff AS s INNER JOIN department AS d ON s.dept_id = d.id HAVING s.salary > (SELECT AVG(salary) FROM staff);
"""
print(f'9.查询薪资高于平均薪资的人的信息(包括部门名称)为:{data.select_sql(sql9)}')

sql10 = """
SELECT d.name, s.* FROM staff AS s INNER JOIN department AS d ON s.dept_id = d.id HAVING s.salary = (SELECT MAX(salary) FROM staff);
"""
print(f'10.查询薪资最高的人的信息为:{data.select_sql(sql10)}')

sql11 = """
SELECT d.name FROM department AS d LEFT JOIN staff AS s ON d.id = s.dept_id WHERE s.dept_id IS NULL;
"""
print(f'11.查询没有员工的部门为:{data.select_sql(sql11)}')

sql12 = """
SELECT d.name, COUNT(*) FROM department AS d INNER JOIN staff AS s ON d.id = s.dept_id GROUP BY d.name;
"""
print(f'12.查询有员工的部门并统计每个部门人数为:{data.select_sql(sql12)}')

sql13 = """
SELECT name, TIMESTAMPDIFF(YEAR, join_date, CURDATE()) FROM staff;
"""
print(f'13.查询所有员工的名称及入职时长为:{data.select_sql(sql13)}')
