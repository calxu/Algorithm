# Algorighm
## 计算机算法基础>>作业
## 中国软件杯大学生软件设计大赛>>针对以经纬度或经纬度带时间定义的不同轨迹
后台设计

7个类型的属性，10个有效方法：
属性
Path	String类型：采用绝对路径，路径初始为”E:\\clusters\\”
e	Double类型：控制两点之间的距离
o	Double类型：定义相邻的最长距离不超过一定点的个数
index	Int类型：初始化为0值，全局索引不标
x	Int[]类型：存储相似点
Similarity_point	String[]类型：存储相似点
Similarity_track	String[]类型：存储相似轨迹

操作
Cluster(int  lineNumber)	int类型：获取聚类的类号i,和类中的行号j;
Search(int i, int j)	String类型：找到第i类中的第j行数据（普通查找），返回查找到的轨迹;
Search(int lineNumber)	String类型：读取指定的行数据，返回查找到的轨迹;
Result(String[] A, String[] B, int[][] b)	Double类型：返回两条轨迹的相似度的结果；
Sort(double[] s)	Double类型：定制冒泡降序排序，伴随相应相似度的值、轨迹点以及相似的轨迹点；
Clean(int[] matrix)	Void类型：9宫格过滤，考虑上下左右四边；
Print_lcs(int[][] b, int i, int j)	Void类型：采用递归对X字符数组进行赋值相似轨迹点的编号，返回数组；
Reset_e_o(String[] A, int m)	Void类型：根据相应的轨迹选取合适的e和o的值；
Compute(int a, int b)	Double类型：计算两条轨迹的相似度，返回相似度的值；
Compute(int  a)	Double[]类型：查找最相似的10条轨迹，返回十条轨迹数组；


3、数据库设计
官网未提供1000万条数据，我们团队以中国大陆随机生成1000万条数据，因为这1000万条轨迹数据长度不统一，采用传统的关系型数据库会造成大量的空间浪费，并且这里的数据单一，都是一种类型的数据，不存数据表之间的关系，所以我们这里采用简单又方便的轻量级数据库；
为考虑到读取效率问题，我们针对所有轨迹数据进行聚类并且建立二级索引目录，以便提高读取轨迹的速度：1、聚类是针对每一条轨迹我们用矩形框最小化框住这条轨迹，取矩形框的中心代表这条轨迹，我们以中心点聚类，经过大量的实验，我们选取聚类个数为10000个（聚类概要图如下图，详细代码参考我们的源码文件中的预处理代码）：
100	200	300	400	500	600	...	...	9900	10000
99	199	299	399	499	599	...	...	9899	9999
...	...	...	...	...	...			...	...
...	...	...	...	...	...	...	...	...	...
6	106	206	306	406	506			9806	9906
5	105	205	305	405	505	...	...	9805	9905
4	104	204	304	404	504			9804	9904
3	103	203	303	403	503	...	...	9803	9903
2	102	202	302	402	502			9802	9902
1	101	201	301	401	501	...	...	9801	9901


轨迹相似度算法设计
根据前面的需求分析，我们这里根据《Discovering Similar Multidimensional Trajectories》这篇论文，并在这篇论文的基础上作出了很大的改进。

(其中轨迹和轨迹,对于，，这里的为一个整数，在轨迹相似度计算中，我们根据轨迹的长度动态地给出的值，ε值代表相近轨迹点之间的距离)
定义2：以下给定我们根据题目给出轨迹相似度的定义：
(m,n分别为轨迹A和轨迹B点的个数)
我们在论文给出的动态规划LCSS算法的基础上作出了很多的改进，我们采用了矩阵表的方式大大地降低了时间空复杂度与空间复杂度，时间复杂度降低至O(mn)，具体的算法伪代码可以参照下图(具体的算法代码实现可以参照LCSS类中result方法)：

以下给定我们根据题目给出轨迹相似度的定义：
(m,n分别为轨迹A和轨迹B点的个数)
我们在论文给出的动态规划LCSS算法的基础上作出了很多的改进，我们采用了矩阵表的方式大大地降低了时间空复杂度与空间复杂度，时间复杂度降低至O(mn)，具体的算法伪代码可以参照下图(具体的算法代码实现可以参照LCSS类中result方法)：

LCSS(X,Y)
  m = X.length
  n = Y.length
  Let b[1..m, 1..n] and c[0..m, 0..n] be new tables
  for i = 1 to m
c[i, 0] = 0
  for j = 0 to n
c[0,j] = 0
  for i = 1 to m
for j = 1 to n
  		If x[i] == y[j]
    		c[i, j] = c[i-1, j-1] + 1
  		elseif c[i-1, j] >= c[i, j-1]
    		c[i, j] = c[i-1, j]
  		else c[i, j] = c[i, j-1]
