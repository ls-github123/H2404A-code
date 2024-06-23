# 6.mysql定义食物表food\kind
import pymysql
class Mypymysql:
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host = '182.92.217.5',
                port = 3306,
                user = 'root',
                password = '',
                database = 'H2404A',
                charset = 'utf8'
                )
            print(f'数据库连接{self.con}建立成功')
        except Exception as e:
            print(f'数据库连接建立失败!错误信息:{e}')
        else:
            self.c1 = self.con.cursor()
            print(f'游标对象{self.c1}建立成功')
            
    def excute_sql(self, sql):
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'非查询指令({sql})执行成功,已上传服务器')
        except Exception as e:
            self.con.rollback()
            print(f'非查询指令({sql})执行失败!数据回滚-错误信息:{e}')
    
    def select_sql(self, sql):
        try:
            self.c1.execute(sql)
            self.con.commit()
            print(f'查询指令({sql})执行成功,已上传服务器')
            result = self.c1.fetchall()
            return result
        except Exception as e:
            self.con.rollback()
            print(f'查询指令({sql})执行失败!数据回滚-错误信息:{e}')

mypymysql = Mypymysql()
sql1 = """
-- 1.创建种类表kind
CREATE TABLE kind(\
    id TINYINT PRIMARY KEY AUTO_INCREMENT,\
    name CHAR(2) UNIQUE NOT NULL);
"""
mypymysql.excute_sql(sql1)

sql2 = """
-- 2.向种类表kind中添加数据
INSERT INTO kind VALUES
(1, '水果'),
(0, '蔬菜'),
(0, '零食'),
(0, '生鲜');
"""
mypymysql.excute_sql(sql2)

sql3 = """
-- 3.创建食物表food
CREATE TABLE food(\
    id TINYINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(3) UNIQUE NOT NULL,
    price DECIMAL(2,0) NOT NULL,
    num INT NOT NULL,
    evaluate ENUM('Good', 'Just so so', 'Bad') NOT NULL,
    kind_id TINYINT NOT NULL,
    FOREIGN KEY(kind_id) REFERENCES kind(id));
"""
mypymysql.excute_sql(sql3)

sql4 = """
-- 4.向食物表food中添加数据
INSERT INTO food VALUES
(1, '菠萝', 10, 5, 'Good', 1),
(0, '香蕉', 10, 14, 'Just so so', 1),
(0, '巧克力', 35, 10, 'Good', 3),
(0, '芒果', 20, 7, 'Good', 1),
(0, '薯片', 18, 30, 'Bad', 3),
(0, '茄子', 12, 20, 'Bad', 2);
"""
mypymysql.excute_sql(sql4)

sql5 = """
SELECT k.name, GROUP_CONCAT(f.name) FROM food AS f INNER JOIN kind AS k ON f.kind_id = k.id GROUP BY k.name HAVING COUNT(*) >= 2;
"""
print(f'5.查询种类数量大于等于2个的种类及包含的商品名称为:{mypymysql.select_sql(sql5)}')

sql6 = """
SELECT name, price FROM food HAVING price = (SELECT MAX(price) FROM food);
"""
print(f'6.查询价格最高的食物名称及价格为:{mypymysql.select_sql(sql6)}')

sql7 = """
SELECT name, price FROM food HAVING price > (SELECT AVG(price) FROM food);
"""
print(f'7.查询价格高于平均价格的商品的名称和价格为:{mypymysql.select_sql(sql7)}')

sql8 = """
SELECT * FROM food ORDER BY price DESC, num ASC;
"""
print(f'8.查询商品信息按照价格从高到低排序，如果价格相同则按照数量从低到高排序为:{mypymysql.select_sql(sql8)}')

sql9 = """
SELECT evaluate, name FROM food;
"""
print(f'9.查询不同评价(evaluate)及其对应的商品名称为:{mypymysql.select_sql(sql9)}')

sql10 = """
SELECT k.name, GROUP_CONCAT(f.name) FROM food AS f INNER JOIN kind AS k ON f.kind_id = k.id GROUP BY k.name HAVING AVG(f.price) >= 15;
"""
print(f'10.查询平均价格大于等于15的商品种类及对应商品的名称为:{mypymysql.select_sql(sql10)}')

sql11 = """
SELECT DISTINCT k.name FROM kind AS k LEFT JOIN food AS f ON k.id = f.kind_id WHERE f.id IS NOT NULL;;
"""
print(f'10.查询并打印所有有商品的种类为:{mypymysql.select_sql(sql11)}')

# del_food_name = input('请输入要删除的商品的名称:')
# sql12 = f"""
# DELETE FROM food WHERE name = '{del_food_name}';
# """
# mypymysql.excute_sql(sql12)

select_kind = input('请输入要查询信息的种类名称:')
sql13 = f"""
SELECT f.num, f.name FROM food AS f INNER JOIN kind AS k ON k.id = f.kind_id WHERE k.name = '{select_kind}'
"""
print(f'12.查询种类({select_kind})对应的商品的数量及商品的名称为:{mypymysql.select_sql(sql13)}')