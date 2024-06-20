# 1.pymysql创建表(表名为自己名字)
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
            print('查询指令执行成功,提交数据库')
            results = self.c1.fetchall()
            for result in results:
                result_list.append(result)
            return result_list
        except Exception as e:
            print(f'错误(ERROR):{e}')
            self.con.rollback()
            print('查询指令执行失败,回滚数据!')
            
    def excute_sql(self,sql):# 执行增删改功能SQL语句,不返回数据
        try:
            self.c1.execute(sql)
            self.con.commit()
            print('非查询指令执行成功,提交数据库')
        except Exception as e:
            print(f'错误(ERROR):{e}')
            self.con.rollback()
            print('非查询指令执行失败,数据回滚!')
    
testecs = Database()
sql1 = """
-- 1.实现创建表,表名为自己的名字
CREATE TABLE lishuo\
(id TINYINT PRIMARY KEY AUTO_INCREMENT,\
sname VARCHAR(20) NOT NULL,\
score DECIMAL(4,2),\
age TINYINT NOT NULL,\
gender ENUM('男', '女', '未知') DEFAULT '男',\
class VARCHAR(5) NOT NULL);
"""
testecs.excute_sql(sql1)

sql2 = """
-- 2.向表中添加数据
INSERT INTO lishuo VALUES\
(1, '黑小熊', 56.98, 18, '男','B班'),\
(0, '大白', 99.99, 16, '女', 'C班'),\
(0, '蓝多多', 80.50, 23, '女', 'B班'),\
(0, '老红', 45.00, 24, '男', 'A班'),\
(0, '小老刘', 68.00, 35, '男', 'A班'),\
(0, '小红', 80.50, 19, '未知', 'B班');
"""
testecs.excute_sql(sql2)

sql3 = """
-- 3.pymysql实现模糊查询,名字中含有小的信息
SELECT * FROM lishuo WHERE sname LIKE '%小%';
"""
print(f'3.模糊查询名字中含有小的信息为:{testecs.select_sql(sql3)}')

sql4 = """
-- 4.正则查询,名字中含有小的信息
SELECT * FROM lishuo WHERE sname RLIKE '^.*小.*$'
"""
print(f'4.正则查询,名字中含有小的信息为:{testecs.select_sql(sql4)}')

sql5 = """
-- 5.正则查询名字是三个字的信息
SELECT * FROM lishuo WHERE sname RLIKE '^...$'
"""
print(f'5.正则查询名字是三个字的信息为:{testecs.select_sql(sql5)}')

sql6_1 = """
-- 6.查询id为2、3、4的人的信息(三种方法)
SELECT * FROM lishuo WHERE id = 2 or id = 3 or id = 4;
"""
print(f'6_1.查询id为2、3、4的人的信息(三种方法)为:{testecs.select_sql(sql6_1)}')

sql6_2 = """
SELECT * FROM lishuo WHERE id IN (2,3,4);
"""
print(f'6_2.查询id为2、3、4的人的信息(三种方法)为:{testecs.select_sql(sql6_2)}')

sql6_3 = """
SELECT * FROM lishuo WHERE id BETWEEN 2 and 4;
"""
print(f'6_3.查询id为2、3、4的人的信息(三种方法)为:{testecs.select_sql(sql6_3)}')

sql7 = """
-- 7.查询成绩及格的人的信息
SELECT * FROM lishuo WHERE score >= 60;
"""
print(f'7.查询成绩及格的人的信息为:{testecs.select_sql(sql7)}')

sql8 = """
-- 8.查询成绩不及格并且为男生的信息
SELECT * FROM lishuo WHERE score < 60 AND gender = '男';
"""
print(f'8.查询成绩不及格并且为男生的信息为:{testecs.select_sql(sql8)}')

sql9 = """
-- 9.查询所有人的平均年龄
SELECT AVG(age) FROM lishuo;
"""
print(f'9.所有人的平均年龄为:{testecs.select_sql(sql9)}')

sql10 = """
-- 10.查询所有人的平均分数,保留两位输出
SELECT ROUND(AVG(score), 2) FROM lishuo; 
"""
print(f'10.所有人的平均分数保留2位输出为:{testecs.select_sql(sql10)}')

sql11 = """
-- 11.统计不同性别分别的名字和分数
SELECT gender, GROUP_CONCAT(sname, '-', score) FROM lishuo GROUP BY gender;
"""
print(f'11.统计不同性别分别的名字和分数为:{testecs.select_sql(sql11)}')

sql12 = """
-- 12.对所有人按照分数由高到低进行排序，如果分数相同则按照年龄从小到大排序
SELECT * FROM lishuo ORDER BY score DESC, age ASC;
"""
print(f'12.对所有人按照分数由高到低排序为:{testecs.select_sql(sql12)}')

sql13 = """
-- 13.统计不同班级的人数、平均分数、平均年龄
SELECT class, COUNT(*), AVG(score), AVG(age) FROM lishuo GROUP BY class;
"""
print(f'13.统计不同班级的人数、平均分数、平均年龄为:{testecs.select_sql(sql13)}')

sql14 = """
-- 14.查询人数大于等于两人的班级及该班级的人数
SELECT class, COUNT(*) FROM lishuo GROUP BY class HAVING COUNT(*) >= 2;
"""
print(f'14.查询人数大于等于两人的班级及该班级的人数为:{testecs.select_sql(sql14)}')

sql15 = """
-- 15.对数据进行分页,每一页存放3条数据,查询第二页的数据
SELECT * FROM lishuo LIMIT 3,3;
"""
print(f'15.对数据进行分页,每一页存放3条数据,查询第二页的数据为:{testecs.select_sql(sql15)}')

sql16 = """
-- 16.统计男生的个数及姓名
SELECT COUNT(*), GROUP_CONCAT(sname) FROM lishuo WHERE gender = '男';
"""
print(f"16.男生的个数及姓名为:{testecs.select_sql(sql16)}")

sql17 = """
-- 17.给表中增加字段is_delete,默认值为0
ALTER TABLE lishuo ADD is_delete ENUM('0', '1') DEFAULT '0';
"""
testecs.excute_sql(sql17)

sql18 = """
-- 18.给表中字段gender修改字段名为sex
ALTER TABLE lishuo CHANGE gender sex ENUM('男', '女', '未知') DEFAULT '男';
"""
testecs.excute_sql(sql18)

sql19 = """
-- 19.给表中score字段增加非空约束
ALTER TABLE lishuo MODIFY score DECIMAL(4,2) NOT NULL;
"""
testecs.excute_sql(sql19)

sql20 = """
-- 20.给表中sname字段增加唯一约束
ALTER TABLE lishuo MODIFY sname VARCHAR(20) NOT NULL UNIQUE;
"""
testecs.excute_sql(sql20)

sql21 = """
-- 21.删除表中is_delete字段
ALTER TABLE lishuo DROP COLUMN is_delete;
"""
testecs.excute_sql(sql21)