# day16

# 知识点回顾

## 表结构操作

```mysql
1.修改表名
	>>> alter table 表名 rename 新表名;
2.增加字段
	>>> alter table 表名 add 字段名 类型 约束;
3.删除字段 
	>>> alter table 表名 drop 字段名;
4.修改字段
	修改字段名的修改
		>>> alter table 表名 change 原字段名 新字段名 类型 约束;
	不修改字段名的修改
		>>> alter table 表名 modify 字段名 类型 约束;
```

## 数据的修改与删除

```mysql
1.数据的修改
	>>> update 表名 set 字段 = 新值 where 条件;
2.数据的删除
	物理删除
		>>> delete from 表名 where 条件;
	逻辑删除 本质是修改数据
		>>> alter table 表名 add 字段 类型 约束;
		>>> update 表名 set 字段 = 新值 where 条件;
```

## 数据的查询

```mysql
1. 简单查询
	查询表中所有字段的值：>>> select * from 表名;
	查询表中指定字段的值：>>> select 字段,字段…… from 表名;
	给字段起别名：>>> select 字段 as 别名,字段…… from 表名;
	给表起别名：>>> select 字段,字段…… from 表名 as 别名;  
	给字段的值进行去重：>>> select distinct 字段 from 表名;
2. 条件查询
	查询表中满足指定条件的数据：>>> select * from 表名 where 条件;
3. 比较运算符
	>   <   >=   <=  =   !=或<>
4. 逻辑运算符
	and or not
5. 范围查询
	in：判断数据是否在指定不连续的区间范围内 
	not in：判断数据是否不在指定不连续的区间范围内
		>>> select * from stu where id in (1,9,11);
	between a and b：判断数据是否在a-b之间，包括a和b
	not between a and b：判断数据是否不在a-b之间
		>>> select * from stu where id between 5 and 10;
6. 空判断与非空判断
	is null：判断是否为空
	is not null：判断是否为非空
7. 排序
	asc 升序  默认排序方式，可以不指定
	desc 降序
	>>> select * from 表名 order by 字段 排序,字段 排序……;
8. 聚合函数
	max(字段)
	min(字段)
	sum(字段)
	count(字段)
	avg(字段)
		保留小数  round(小数,要保留的位数)  满足四舍五入
9. 分组
	group by
	>>> select * from 表名 group by 字段;
10. 过滤
	having
	>>> select * from 表名 group by 字段 having 过滤条件;
11. 分页
	limit num：获取前num条数据
		>>> select * from 表名 limit 5;
	limit start,num：进行分页查询
		start:从哪条数据开始查询  start = （页数 - 1 ）* 每一页的数据条数
		num：要查询的数据条数(一页有多少条数据)
```

## pymysql实现表结构操作

```python
不触发事务的操作
1. 连接mysql
2. 获取游标对象
3. 编写sql语句
4. 游标对象执行sql语句
5. 关闭数据连接
```

## pymysql实现数据修改与删除

```python
会触发事务的操作：增加数据 insert  修改数据 update  删除数据 delete
1. 连接mysql
2. 获取游标对象
3. 编写sql语句
4. 游标对象执行sql语句
	如果sql语句执行成功则让数据库对象提交事务
  如果sql语句执行失败则让数据库对象将事务进行回滚
5. 关闭数据连接
```

## pymysql实现数据查询

```python
1. 连接mysql
2. 获取游标对象
3. 编写sql语句
4. 游标对象执行sql语句
5. 调用方法从游标对象中获取数据
6. 关闭数据连接

fetchone():一次获取一条数据
fetchmany(num):不指定num，默认获取一条数据；指定num获取num条数据；如果num大于获取到的数据条数，查询全部，不报错。
fetchall():一次性获取所有的数据
```

# 连接查询

## 概念

```
当查询结果的列来源于多张表时，需要将多张表连接成一个大的数据集，再选择合适的列返回
```

## 分类

```
1. 内连接
	普通内连接
	自关联
2. 外连接
	左外连接
	右外连接
```

## 案例

```mysql
一张班级表
create table class(
id tinyint primary key auto_increment,
name varchar(5) unique
);

insert into class value
(0,"A班"),
(0,"B班"),
(0,"C班");

一张学生表
create table student(
id tinyint primary key auto_increment,
name varchar(5) unique,
age tinyint,
gender enum("男","女","保密") default "保密",
cls_id tinyint
);


insert into student value
(0,"张三",18,"男",1),
(0,"李四",16,"女",1),
(0,"王五",20,"男",1),
(0,"赵六",23,"男",2),
(0,"田七",17,"女",2),
(0,"胡八",30,"男",5);
```

## 普通内连接

### 语法

```mysql
select * from 表1 inner join 表2 on 连接条件
特点：如果连接表中没有与之对应的数据，则该条数据不展示
```

### 案例

```mysql
1. 将班级表与学生表内连接--》将班级表作为表1-->班级表中数据在左侧展示
>>> select * from class inner join student on cls_id = class.id;

2. 将班级表与学生表内连接--》将学生表作为表1-->学生表中数据在左侧展示
>>> select * from student inner join class on cls_id = class.id;

3. 获取所有的学生姓名及对应的班级名称，将数据按照年龄从大到小进行排序
>>> select c.name,s.name from class as c inner join student as s on cls_id = c.id order by age desc;

4. 查询人数大于2人的班级，班级名称、该班级中学生的数量及学生名称
>>> select c.name,count(*),group_concat(s.name) from student as s inner join class as c on cls_id = c.id group by c.name having count(*) > 2;

5. 查询所有有学生的班级，获取班级名即可
>>> select distinct class.name from class inner join student on cls_id = class.id;
```

## 左外连接

### 语法

```mysql
select * from 表1 left join 表2 on 连接条件
哪张表作为表1，哪张表就是主表
主表中所有的数据在左侧展示，如果从表中没有与之对应的数据则用null填充
从表中没有对应的数据则不展示
```

### 案例

```mysql
1. 将班级表与学生表左外连接--》将学生表作为表1
>>> select * from student as s left join class as c on cls_id = c.id;

2. 将班级表与学生表左外连接--》将班级表作为表1
>>> select * from class as c left join student as s on cls_id = c.id;

3. 获取所有的学生姓名及对应的班级名称，将数据按照年龄从大到小进行排序
>>> select s.name,c.name from student as s left join class as c on cls_id = c.id order by age desc;

4. 查询没有班级的学生
>>> select * from student as s left join class as c on cls_id = c.id where c.name is null;

5. 查询有学生的班级
>>> select * from class as c left join student as s on cls_id = c.id where cls_id is not null;
```

## 右外连接

### 语法

```mysql
select * from 表1 right join 表2 on 连接条件;
哪张表作为表2，哪张表就是主表
主表中所有的数据在右侧展示，如果从表中没有与之对应的数据则用null填充
从表中没有对应的数据则不展示
```

### 案例

```mysql
1. 将班级表与学生表右外连接--》将学生表作为表1
>>> select * from student right join class on cls_id = class.id;

2. 将班级表与学生表右外连接--》将班级表作为表1
>>> select * from class right join student on cls_id = class.id;
```

## 自关联

### 案例

```mysql
省份表
id    name
1     河南省
2     河北省
3     山东省

市级表
id    name      pid
1     郑州市     1
2     洛阳市     1
3     石家庄市   2
4     青岛市     3


县级表
id    name      pid
1     二七区     1
2     金水区     1
3     桥东区     3
4     崂山区     4

将三张表合为一张
id     name     pid
1     河南省    null
2     河北省    null
3     山东省    null
4     郑州市     1
5     洛阳市     1
6     石家庄     2
7     青岛市     3
8     二七区     4
9     金水区     4
10    桥东区     6
11    崂山区     7

create table area(
id tinyint primary key auto_increment,
name varchar(5) unique,
pid tinyint
);

insert into area value
(0,"河南省",null),
(0,"河北省",null),
(0,"山东省",null),
(0,"郑州市",1),
(0,"洛阳市",1),
(0,"石家庄",2),
(0,"青岛市",3),
(0,"二七区",4),
(0,"金水区",4),
(0,"桥东区",6),
(0,"崂山区",7);
```

### 语法

```mysql
自关联本质就是内连接
select * from 表1 inner join 表2 on 连接条件;
```

### 案例

```mysql
1. 实现自关联
# 自己关联自己，表必须起别名
>>> select * from area as a1 inner join area as a2 on a1.id = a2.pid;

2. 查询所有的省
>>> select * from area where pid is null;

3. 查询河南省下面的市
>>> select * from area as a1 inner join area as a2 on a1.id = a2.pid where a1.name = "河南省";
>>> select a1.name,group_concat(a2.name) from area as a1 inner join area as a2 on a1.id = a2.pid group by a1.name having a1.name = "河南省";
```

# 外键约束

## 概念

```mysql
foreign key
外键约束:对外键字段的值进行更新和插入时会和引用表中字段的数据进行验证，数据如果不合法则更新和插入会失败，保证数据的有效性

1. 想要限制哪一张表中的哪一个字段的值，该字段应该设置外键约束，必须收到另外一张表的某个字段的值的限制
2. 被限制的字段与起限制性作用的字段类型一致
3. 起限制性作用的字段要求必须是主键
4. 如果表中已经存在不合规的数据，再增加外键约束会失败；需要将不合规的数据删除，再增加外键约束即可
```

## 案例

```mysql
create table address(
id tinyint primary key,
name varchar(5)
);

insert into address value
(1,"河南省"),
(2,"河北省"),
(3,"山东省");

create table user1(
id tinyint,
name varchar(5),
add_id tinyint,
foreign key(add_id) references address(id)
);

insert into user1 value(1,"张三",1);   # add_id在范围内，则添加成功
insert into user1 value(2,"李四",6);   # add_id超出范围，则添加失败
```

## 设置外键

```mysql
foreign key(字段) references 表(字段)

1.在创建表时增加外键约束
语法：>>> create table 表名(字段 类型 约束,字段 类型 约束,foreign key(字段) references 表(字段));
案例：>>> create table user1(
id tinyint,
name varchar(5),
add_id tinyint,
foreign key(add_id) references address(id)
);

2.给已经创建好的表增加外键约束
语法：>>> alter table 表名 add foreign key(字段) references 表(字段);
案例：>>> alter table user1 add foreign key(add_id) references address(id);
```

## 删除外键

```mysql
如果给一张表中设置外键，系统会自动生成外键名

# 查询外键名-->查询创建表的语句
语法：>>> show create table 表名;
案例：>>> show create table user1;
结果：CONSTRAINT `user1_ibfk_1`    此时user1_ibfk_1就是外键名

# 从表中删除外键
语法：>>> alter table 表名 drop foreign key 外键名;
案例：>>> alter table user1 drop foreign key user1_ibfk_1;
```

# 子查询

## 概念

```
在一个select语句中嵌套另外一个select语句
被嵌套的select语句被称之为子查询语句
起嵌套作用select语句被称之为主查询语句
```

## 分类

```mysql
标量子查询：子查询的结果是一个具体的数据
	>>> select max(age) from stu;      56
行子查询：子查询的结果是一行数据/多个数据
	>>> select * from stu where name = "张三";
	>>> select avg(height),avg(age),avg(money) from stu;
列子查询：子查询的结果是一列数据
	>>> select id from stu;
```

## 案例

```mysql
# 聚合函数不能作为where条件使用，可以having中直接使用

1. 查询年龄最大的这个人的信息
	1>. 按照年龄从大到小排序，取第一个值-->仅限于最大值只有一个
		>>> select * from stu order by age desc limit 1;
	2>. 使用子查询语句
		第一步：查询表中最大的年龄    >>> select max(age) from stu;
		第二步：查询该年龄对应的学生的信息   >>> select * from stu where age = 59;
		综上所述：>>> select * from stu where age = (select max(age) from stu);

2. 查询身高高于平均身高的人的信息
>>> select * from stu where height > (select avg(height) from stu);
```

## 子查询中关键字的使用

### 算术运算符

```mysql
>   <   =   >=    <=   !=

# 查询年龄低于平均年龄的人的信息
>>> select * from stu where age < (select avg(age) from stu);
```

### in、not  in

```mysql
# 查询有学生的班级
1>. 内连接
	>>> select distinct c.name from class as c inner join student as s on cls_id = c.id;
2>. 外连接
	>>> select distinct c.name from class as c left join student as s on cls_id = c.id where cls_id is not null;
3>. 子查询
	第一步：从学生表中获取cls_id    select cls_id from student;
	第二步：从班级中查询哪个id再查询到的cls_id中   select name from class where id in (1,1,1,2,2,5);
	>>> select name from class where id in (select cls_id from student);
```

### any、some

```mysql
some是any别名
any:任意一个
# 查询身高高于  (未成年的人)的身高  任意一个的人的信息
1. 获取未成年的人的身高
>>> select height from stu where age < 18;

2. 查询身高高于这一部分身高的人的信息
>>> select * from stu where height > (180,170);

3. 子查询
>>> select * from stu where height > any(select height from stu where age < 18);
```

### all

```mysql
all：全部
# 查询身高高于  (未成年的人)的身高   全部的人的信息
1. 获取未成年的人的身高
>>> select height from stu where age < 18;

2. 查询身高高于这一部分身高的人的信息
>>> select * from stu where height > (180,170);

3. 子查询
>>> select * from stu where height > all(select height from stu where age < 18);
```

### exists

```mysql
exists：存在
如果子查询语句有结果，则执行主查询语句
如果子查询语句没有结果，则不执行主查询语句

子查询：select * from stu where height > 190;
主查询：select * from stu;
>>> select * from stu where exists (select * from stu where height > 190);
```

