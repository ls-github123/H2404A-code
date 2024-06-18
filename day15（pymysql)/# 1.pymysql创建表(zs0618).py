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
-- 1.pymysql创建表zs0618
CREATE TABLE zs0618\
(id TINYINT PRIMARY KEY AUTO_INCREMENT,\
name VARCHAR(10) UNIQUE,\
sex ENUM('男','女'),\
birthday DATE NOT NULL,\
phone CHAR(11));
-- 2.给创建好的表增加字段is_delete
ALTER TABLE zs0618 ADD is_delete ENUM('√','X') DEFAULT 'X';
-- 3.修改表名为zhangsan0109
ALTER TABLE zs0618 RENAME zhangsan0109;
-- 4.修改字段sex名为gender,并在原来的选项上增加'保密'选项,设置为默认值
ALTER TABLE zhangsan0109 CHANGE sex gender ENUM('男','女','保密') DEFAULT '保密';
-- 5.给表中任意增加5条数据
INSERT INTO zhangsan0109 VALUES\
(1, '张重量', '男', '1998-05-02','18095190558', default),\
(0, '黄子', '女', '2001-01-08', '18005051125', default),\
(0, '罗佩奇', default, '2000-12-25', '15001010202', default),\
(0, '杜佳琪', '女', '1999-05-08', '18102020303', default),\
(0, '刘思莹', '女', '2001-02-22', '19995004665', default);
-- 6.修改id为3的is_delete值为'√'
UPDATE zhangsan0109 SET is_delete = '√' WHERE id = 3;
-- 7.删除id为1的学生的信息
DELETE FROM zhangsan0109 WHERE id = 1;
-- 8.删除表中phone字段
ALTER TABLE zhangsan0109 DROP COLUMN phone;
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