# 2.pymysql创建表user
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
-- 1.pymysql创建表user
CREATE TABLE user\
(id TINYINT PRIMARY KEY AUTO_INCREMENT,\
name VARCHAR(10) UNIQUE,\
age TINYINT NOT NULL,\
gender ENUM('男', '女', '保密'),\
height DECIMAL(3,0) NOT NULL,\
birthday DATE NOT NULL,\
class ENUM('A班','B班','C班') NOT NULL);
-- 2.给表增加字段is_delete,单选是、否, 默认为否
ALTER TABLE user ADD is_delete ENUM('是', '否') DEFAULT '否';
-- 3.修改字段gender名为sex,增加一个选项中性,并设置为默认值
ALTER TABLE user CHANGE gender sex ENUM('男', '女', '中性', '保密') DEFAULT '中性';
-- 4.删除字段is_delete
ALTER TABLE user DROP COLUMN is_delete;
-- 5.向表中添加数据
INSERT INTO user VALUES\
(1, '张三', 18, '男', 174, '2006-7-4', 'A班'),
(0, '李四', 21, '女', 165, '2003-9-9', 'A班'),
(0, '王五', 16, '男', 172, '2008-12-19', 'B班'),
(0, '赵六', 19, '保密', 168, '2005-10-21', 'C班'),
(0, '田七', 18, '男', 156, '2006-6-30', 'A班'),
(0, '胡八', 19, '女', 147, '2005-3-18', 'B班');
-- 6.调整李四为C班
UPDATE user SET class = 'C班' WHERE name = '李四';
-- 7.删除性别为保密的学生
DELETE FROM user WHERE sex = '保密';
"""
try:
    c1.execute(sql)
    con.commit()
    print('执行成功,数据提交数据库')
except Exception as e:
    print(e)
    con.rollback() # 回滚数据
    print('数据提交失败,回滚数据!')

c1.close() #关闭游标
con.close() # 关闭数据库连接