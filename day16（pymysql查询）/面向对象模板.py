import pymysql
class Database:
    def __init__(self):
        try:
            self.con = pymysql.connect(
                host = ''，
                port = 3306,
                user = 'root'，
                password = ''，
                database = ''，
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
