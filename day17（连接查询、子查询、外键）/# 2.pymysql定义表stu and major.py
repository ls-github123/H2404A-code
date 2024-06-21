# 2.pymysql定义表stu and major
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
            self.c1 = self.con.cursor()
            print(f'游标对象{self.c1}建立成功')
    
    def excute_sql(self, sql): # sql单向执行语句,不返回查询数据
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'非查询指令({sql})执行成功')
        except Exception as e:
            print(f'错误(Error):{e}')
            self.con.rollback()
            print(f'非查询指令{sql}执行失败,数据回滚!')
    
    def select_sql(self, sql): # sql查询语句,返回查询数据
        SelectList = [] # 定义一个空列表，存放查询返回的数据
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'查询指令({sql})执行成功,提交数据库')
            results = self.c1.fetchall() # 返回查询到的全部数据
            for result in results:
                SelectList.append(result) # 将回传的数据依次存入列表
            return SelectList # 返回列表
        except Exception as e:
            print(f'错误(Error):{e}')
            self.con.rollback()
            print(f'查询指令({sql})执行失败,数据回滚!')

data = Database()
SqlMajor = """
-- 创建表major
CREATE TABLE major(
    mid TINYINT PRIMARY KEY AUTO_INCREMENT,
    mname CHAR(2) NOT NULL);
"""
data.excute_sql(SqlMajor)

InsertMajor = """
INSERT INTO major VALUES
(1, '英语'),
(0, '数学'),
(0, '语文'),
(0, '哲学');
"""
data.excute_sql(InsertMajor)

SqlStu = """
CREATE TABLE stu(
    sid SMALLINT PRIMARY KEY AUTO_INCREMENT,
    sname VARCHAR(3) NOT NULL,
    age TINYINT NOT NULL,
    gender ENUM('男','女','保密') DEFAULT '保密' NOT NULL,
    score DECIMAL(2,0) NOT NULL,
    joindate DATE NOT NULL,
    mid TINYINT NOT NULL,
    FOREIGN KEY(mid) REFERENCES major(mid));
"""
data.excute_sql(SqlStu)

InsertStu = """
INSERT INTO stu VALUES\
(1001, '张三', 18, '男', 96, '2016-11-11', 1),\
(0, '李小四', 16, '女', 75, '2018-11-10', 1),\
(0, '王五', 26, '男', 34, '2020-11-13', 3),\
(0, '赵六子', 34, '女', 62, '2016-06-14', 2),\
(0, '老七', 38, '男', 99, '2018-11-16', 1),\
(0, '小老八', 26, default, 62, '2016-11-17', 2);
"""
data.excute_sql(InsertStu)

sql1 = """
SELECT gender, count(*), GROUP_CONCAT(sname) FROM stu GROUP BY gender;
"""
print(f'1.查询不同性别的性别名称、人数及人名为:{data.select_sql(sql1)}')

sql2 = """
SELECT gender, GROUP_CONCAT(sname) FROM stu GROUP BY gender HAVING COUNT(*) >= 2;
"""
print(f'2.查询人数大于等于2人的性别及人名为:{data.select_sql(sql2)}')

sql3 = """
SELECT m.mname, COUNT(*), GROUP_CONCAT(s.sname) FROM major AS m INNER JOIN stu AS s ON m.mid = s.mid GROUP BY m.mname;
"""
print(f'3.查询不同专业的专业名称、人数及人名为:{data.select_sql(sql3)}')

sql4 = """
SELECT m.mname, ROUND(AVG(s.score),2) FROM major AS m INNER JOIN stu AS s ON m.mid = s.mid GROUP BY m.mname HAVING COUNT(*) >= 2;
"""
print(f'4.查询人数大于等于2人的专业名称及平均分数为:{data.select_sql(sql4)}')

sql5 = """
SELECT m.mname, COUNT(*) FROM major AS m INNER JOIN stu AS s ON m.mid = s.mid GROUP BY m.mname HAVING AVG(s.score) >=50;
"""
print(f'5.查询平均分数大于等于50分的专业名称及专业人数为:{data.select_sql(sql5)}')

sql6 = """
SELECT m.mname ,s.* FROM stu AS s INNER JOIN major AS m ON m.mid = s.mid WHERE score = (select MAX(score) FROM stu);
"""
print(f'6.查询最高分数的人的信息包括所属专业为:{data.select_sql(sql6)}')

sql7 = """
SELECT * FROM stu WHERE joindate > '2017-01-01';
"""
print(f'7.查询2017年以后加入学校的人的信息为为:{data.select_sql(sql7)}')

sql8 = """
SELECT m.mname, s.* FROM stu AS s INNER JOIN major AS m ON m.mid = s.mid WHERE s.sname LIKE '%小%';
"""
print(f'8.查询名字中含有小的人的信息(包括所属专业)为:{data.select_sql(sql8)}')

sql9 = """
SELECT m.mname FROM major AS m LEFT JOIN stu AS s ON m.mid = s.mid WHERE s.sname IS NULL;
"""
print(f'9.查询没有学生的专业名称为:{data.select_sql(sql9)}')

sql10 = """
-- 10.实现修改小老八的性别为男
UPDATE stu SET gender = '男' WHERE sname = '小老八';
"""
data.excute_sql(sql10)

sql11 = """
-- 11.实现删除王五的信息
DELETE FROM stu WHERE sname = '王五';
"""
data.excute_sql(sql11)

sql12 = """
SELECT m.mname, s.* FROM stu AS s INNER JOIN major AS m ON m.mid = s.mid HAVING s.score > (select AVG(score) FROM stu);
"""
print(f'12.查询分数高于平均分数的人的信息(包括所属专业)为:{data.select_sql(sql12)}')
