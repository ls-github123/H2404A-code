# 6.面向对象方法实现pymysql
import pymysql
class Database:
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host = '182.92.217.5',
                port = 3306,
                user = 'guest',
                password = 'guest_123456',
                database = 'H2404A_guest',
                charset = 'utf8'
                )
            print(f'数据库连接{self.con}建立成功')
        except Exception as e:
            print('数据库连接建立失败!')
            print(f'错误信息:{e}')
        else:
            self.c1 = self.con.cursor()
            print(f'游标对象{self.c1}建立成功!')
            
    def excute_sql(self,sql):
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'非查询指令({sql})执行成功')
        except Exception as e:
            self.con.rollback()
            print(f'非查询指令({sql})执行失败,数据回滚! 错误信息:{e}')
    
    def select_sql(self,sql):
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'查询指令({sql})执行成功,上传服务器')
            results = self.c1.fetchall()
            return results
        except Exception as e:
            self.con.rollback()
            print(f'查询指令({sql})执行失败,数据回滚! 错误信息:{e}')
            
data = Database()

# sql1 = """
# -- 1.创建表class
# CREATE TABLE class(
#     cid TINYINT PRIMARY KEY AUTO_INCREMENT,
#     cname CHAR(3) NOT NULL
# );
# """
# data.excute_sql(sql1)

# sql2 = """
# -- 2.向表class添加中数据
# INSERT INTO class VALUES
# (1, '三一班'),
# (0, '三二班'),
# (0, '三三班');
# """
# data.excute_sql(sql2)

# sql3 = """
# -- 3.创建表student
# CREATE TABLE student(
#     stuid INT PRIMARY KEY AUTO_INCREMENT,
#     sname VARCHAR(5) NOT NULL,
#     sage TINYINT NOT NULL,
#     gender ENUM('男', '女') DEFAULT '男' NOT NULL,
#     score DECIMAL(3,0) NOT NULL,
#     c_id TINYINT NOT NULL,
#     FOREIGN KEY(c_id) REFERENCES class(cid)
# );
# """
# data.excute_sql(sql3)

# sql4 = """
# INSERT INTO student VALUES
# (1, '张三', 15, '男', 90, 2),
# (0, '王丽丽', 18, '女', 85, 2),
# (0, '李萌萌', 15, '女', 100, 1),
# (0, '曹操', 20, '男', 95, 3),
# (0, '刘贝贝', 15, '女', 85, 2),
# (0, '李芳芳', 16, '女', 100, 3);
# """
# data.excute_sql(sql4)

sql5 = """
SELECT c.cname, s.* FROM student AS s INNER JOIN class AS c ON s.c_id = c.cid WHERE s.sname LIKE '__'; 
"""
print(f'1.查询名字只要两个字的学生所有信息包括班级名称为:{data.select_sql(sql5)}')

sql6 = """
SELECT c.cname, COUNT(*), GROUP_CONCAT(s.sname) FROM class AS c INNER JOIN student AS s ON s.c_id = c.cid GROUP BY c.cname;
"""
print(f'2.查询不同班级的学生人数及学生名称为:{data.select_sql(sql6)}')

sql7 = """
SELECT c.cname, GROUP_CONCAT(s.sname) FROM class AS c INNER JOIN student AS s ON c.cid = s.c_id GROUP BY c.cname HAVING COUNT(*) >= 2;
"""
print(f'3.查询班级人数大于等于2人的班级名称及班级中学生名称为:{data.select_sql(sql7)}')

sql8 = """
SELECT s.*, c.cname FROM student AS s INNER JOIN class AS c ON s.c_id = c.cid HAVING s.sage > (SELECT AVG(sage) FROM student);
"""
print(f'4.查询年龄大于平均年龄的学生的所有信息包括学生的班级名称为:{data.select_sql(sql8)}')

sql9 = """
SELECT c.cname, s.* FROM student AS s INNER JOIN class AS c ON s.c_id = c.cid WHERE s.sage = (SELECT MAX(sage) FROM student);
"""
print(f'5.查询分数最高的学生的信息包括学生班级名称为:{data.select_sql(sql9)}')

sql10 = """
SELECT gender, COUNT(*), GROUP_CONCAT(sname) FROM student GROUP BY gender;
"""
print(f'6.统计不同性别中对应的人数及人名为:{data.select_sql(sql10)}')

sql11 = """
SELECT gender, ROUND(AVG(sage),2), ROUND(AVG(score),2) FROM student GROUP BY gender;
"""
print(f'7.统计不同性别的平均年龄以及平均成绩 结果保留两位小数为:{data.select_sql(sql11)}')

sql12 = """
SELECT c.*, s.* FROM student AS s INNER JOIN class AS c ON s.c_id = c.cid LIMIT 3,3;
"""
print(f'8.一页存放3条数据,查询第二页的数据为:{data.select_sql(sql12)}')

sql13 = """
UPDATE student SET score = 95 WHERE sname = '李芳芳';
"""
print(f'9.修改李芳芳的成绩为95:{data.excute_sql(sql13)}')

sql14 = """
ALTER TABLE student CHANGE gender sex ENUM('男', '女') DEFAULT '男' NOT NULL;
"""
print(f'10.将字段gender名称改为sex:{data.excute_sql(sql14)}')

sql15 = """
SELECT c.*, s.* FROM student AS s INNER JOIN class AS c ON s.c_id = c.cid ORDER BY s.sage ASC, s.score DESC;
"""
print(f'11.按照sage升序,score降序进行排列为:{data.select_sql(sql15)}')