-- 单表查询
--1. 查询出部门编号为30的所有员工
  SELECT * FROM t_dept WHERE deptno=30;
-- 2. 所有销售员的姓名、编号和部门编号。
  SELECT ename,empno,deptno FROM t_employees WHERE job ='销售员';
-- 3. 找出奖金高于工资的员工。
  SELECT * FROM t_employees WHERE comm>sal;
-- 4. 找出奖金高于工资60%的员工。
  SELECT * FROM t_employees WHERE comm>(sal*0.6);
-- 5. 找出部门编号为10中所有经理，和部门编号为20中所有销售员的详细资料。
  SELECT * FROM t_employees WHERE(job = "经理" AND deptno=10) OR (job="销售员" AND deptno=20);
-- 6. 找出部门编号为10中所有经理，部门编号为20中所有销售员，还有即不是经理又不是销售员但其工资大或等于20000的所有员工详细资料。
    SELECT * FROM t_employees WHERE(job = "经理" AND deptno=10) OR (job="销售员" AND deptno=20) OR (job NOT IN("经理","销售员") AND sal>2000);
-- 7. 无奖金或奖金低于1000的员工。
    SELECT * FROM t_employees WHERE comm = NULL OR comm<1000 ;
-- 8.查询名字由三个字组成的员工。
   SELECT * FROM t_employees WHERE ename LIKE "____";
-- 9.查询2000年入职的员工。
   SELECT * FROM t_employees WHERE hiredate LIKE "2000%";
-- 10.查询所有员工详细信息，用编号升序排序 asc升序 desc降序
    SELECT * FROM t_employees  ORDER BY empno DESC;
-- 11.查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
  SELECT * FROM t_employees ORDER BY sal DESC ,hiredate ASC;
-- 12.查询每个部门的平均工资
  SELECT deptno ,AVG(sal)FROM t_employees ; 
 -- 13. 查询每个部门的雇员数量。
  SELECT deptno ,COUNT(empno)FROM t_employees ORDER BY deptno;
-- 14.查询每种工作的最高工资、最低工资、人数
   SELECT job,MAX(sal),MIN(sal),COUNT(*) FROM t_employees ORDER BY job;
   
 #多表查询
 #1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
 SELECT COUNT(*),d.`deptno`,d.`dname`,d.`loc`
 FROM `t_employees` e JOIN `t_dept` d ON  e.`deptno`=d.`deptno` 
GROUP BY deptno  HAVING COUNT(*)>=1;
#2.列出所有员工的姓名及其直接上级的姓名。
SELECT yg.`ename`,sj.`ename`
FROM `t_employees` yg JOIN `t_employees` sj ON yg.`MGR`=sj.`empno`;
#3.列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
SELECT  yg.`empno`,yg.`ename`,d.`dname`
FROM `t_employees` yg JOIN `t_dept` d ON yg.`deptno`=d.`deptno` JOIN `t_employees` sj ON yg.`MGR`=sj.`empno`
WHERE yg.`hiredate`<sj.`hiredate`;
#4.列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
SELECT d.dname , e.* FROM `t_employees` e RIGHT OUTER JOIN `t_dept` d ON e.`deptno`=d.`deptno` ;
#5.列出最低薪金大于1500的各种工作及从事此工作的员工人数
SELECT e.job,COUNT(*)

FROM `t_employees` e 
GROUP BY job HAVING MIN(sal)>1500
#6.列出在销售部工作的员工的姓名，假定不知道销售部的部门编号。
SELECT e.`ename`
FROM t_employees  e  JOIN `t_dept` d ON e.`deptno`=d.deptno WHERE d.dname='sales';
#7.列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，
#工资等级。
SELECT e.*,d.`dname`,sj.`ename`
FROM `t_employees` e JOIN `t_dept` d ON e.`deptno`=d.`deptno` JOIN `t_employees` sj ON e.`MGR`=sj.`empno`
WHERE e.sal>(SELECT AVG(sal) FROM `t_employees` e);
#8.列出与张飞从事相同工作的所有员工及部门名称。
SELECT e.`ename`,d.`dname`
FROM `t_employees` e JOIN `t_dept` d ON e.`deptno`=d.`deptno`
WHERE job =(SELECT `job` FROM `t_employees`  WHERE ename='张飞');
