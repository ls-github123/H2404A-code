# pymysql
import pymysql
con = pymysql.connect(
                host = 'rm-cn-j4g3qnten00037ao.rwlb.rds.aliyuncs.com',
                port = 3306,
                user = 'ali_root_ls',
                password = '',
                database = 'H2404A',
                charset = 'utf8'
                )

c1 = con.cursor() # 获取游标对象

sql = """
CREATE TABLE book2\
(id TINYINT PRIMARY KEY AUTO_INCREMENT,\
name VARCHAR(10) UNIQUE,\
price DECIMAL(5,2) NOT NULL,\
author VARCHAR(5) DEFAULT '神秘人');
"""

try:
    c1.execute(sql) # execute() 方法
    con.commit()
    print('执行成功,数据提交数据库')
except Exception as e:
    con.rollback() # 回滚数据
    print('数据提交失败,回滚数据!')

c1.close() #关闭游标
con.close() # 关闭数据库连接

# pumysql操作数据
con = pymysql.connect(
                host = 'rm-cn-j4g3qnten00037ao.rwlb.rds.aliyuncs.com',
                port = 3306,
                user = 'ali_root_ls',
                password = '',
                database = 'H2404A',
                charset = 'utf8'
                )

c1 = con.cursor() # 获取游标对象

sql = """
UPDATE stu SET IS_SAVE = '是' WHER IS_SAVE IS NULL;
"""

# sql = """
# UPDATE stu SET IS_SAVE = '否' WHERE name = '赵六';
# """

# sql = """
# ALTER TABLE stu CHANGE is_delete IS_SAVE ENUM('是','否');
# """

# sql = """
# ALTER TABLE stu ADD is_delete char(1);
# """

# sql = """
# UPDATE stu SET gender = '保密' WHERE name = '灰太狼';
# """
# sql = """
# DELETE FROM stu WHERE name = '张三';
# """

try:
    c1.execute(sql) # execute() 方法
    con.commit()
    print('执行成功,数据提交数据库')
except Exception as e:
    print(f'错误信息:{e}')
    con.rollback() # 回滚数据
    print('数据提交失败,回滚数据!')

c1.close() #关闭游标
con.close() # 关闭数据库连接
