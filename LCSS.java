// clusters_index 被聚成100*100个类
// 10000个类似于100_data文件在相应目录中

import java.io.*;
import java.lang.Math;

public class LCSS
{	
	// 属性
	
	// LCSS算法待确定参数
	private double e = 0.01;              // 两点之间的距离
	private double o = 20;                // 定义相邻的最长距离不超过20个点
	
	// 相似点的变量的定义
	private int index = 0;                // 全局索引下标
	private int[] x;                      // 相似点的存储
	
	// 相似点 与 相似轨迹
	public  String[] Similarity_point = new String[10];    // 相似点
	public  String[] Similarity_track = new String[10];    // 相似轨迹
	
	
	// 方法
	
	// 聚类 i*10000 + j
	public int cluster(int lineNumber) throws IOException            
	{
		boolean flag = false;                                                  // 哨兵标记
		int i = 1, j = 0;                                                      // 计数器,表示第i个聚类; j用于统于索引下标   
		FileReader fr = new FileReader("F:\\Trajectory_project\\trajectory\\src\\clusters\\clusters_index"); // 普通方式读取文件
		BufferedReader bfr = new BufferedReader(fr, 65536);                    // 创建缓冲流,加速读取速度
		for (i=1; i<= 10000; i++)                                               // 遍历100个聚类
		{
			Similarity_track = bfr.readLine().split(",");                      // 按","分割
			j = 0;                                                             // 索引下标置0
		    for (String element: Similarity_track)
		    {
		    	if (Integer.parseInt(element) == lineNumber)                   // 如果相等,即找到对应的轨迹所属的类
		    	{
		    		flag = true;
		    		break;                                                     // 找到则退出内层循环
		    	}
		    	j++;                                                           // 索引下标自增1
		    }
		    if(flag) break;                                                    // 找到并退出外层循环
		}
		
		bfr.close();                                                           // 关闭缓冲流
		fr.close();                                                            // 关闭普通文件
		
		return(i*10000+j);                                                     // 返回j , i;j聚类中的第几个;i第几个聚类 
	}
	
	// 第i类中的第j行数据(普通查找)
	public String search(int i, int j) throws IOException
	{
		FileReader fr = new FileReader("F:\\Trajectory_project\\trajectory\\src\\clusters\\"+i+"_data"); // 普通方式读取文件
		BufferedReader bfr = new BufferedReader(fr, 65536);                                              // 创建缓冲流
		int k = 0;
		while (k++ < j) bfr.readLine();                                        // 跳过前面j-1行 
		String s = bfr.readLine();                                             // 找到指定的行数据
		bfr.close();                                                           // 关闭缓冲流
		fr.close();                                                            // 关闭普通文件
		return(s);                                                             // 返回指定行数据
	}
	
	// 读取指定的行数据
	public String search(int lineNumber) throws IOException
	{
		int i,j;                                     // 计数器,表示第i个聚类; j用于统于索引下标   
		int t = cluster(lineNumber);                 // t = j*1000+i
		i = t / 10000;                               // 所属的聚类号
		j = t % 10000;                               // 所属聚类中第几行数据
		String s = search(i, j);                     // 指定行的数据
		
		return s;                                    // 返回轨迹的详细信息
	}
	
	// 返回两条轨迹的相似度的结果
	public double result(String[] A, String[] B, int[][] b)
	{
		int m = A.length/3;                        // A轨迹对的个数
		int n = B.length/3;                        // B轨迹对的个数
		int[][] c = new int[m+1][n+1];             // 矩阵表
		
		// 遍历整个m*n的矩阵
		for (int i = 1; i <= m; i++)    
		{
			for (int j = 1; j <= n; j++)
			{
				// 两点之间的纬经度足够短,并两点之间的距离不超过20
				if ( (Math.abs(Double.valueOf(A[3*i])-Double.valueOf(B[3*j])) < e) && (Math.abs(Double.valueOf(A[3*i+1])-Double.valueOf(B[3*j+1])) < e) && (Math.abs(i - j) <= o) )
				{
					c[i][j] = c[i-1][j-1] + 1;            // 左上角的值加1
					b[i][j] = 0;                          // 参考左上角的值
				}
				else if (c[i-1][j] >= c[i][j-1])          // 上方的值大于左边的值
				{
					c[i][j] = c[i-1][j];                  // 参考正上方的值
					b[i][j] = 1;                          // 参考正上方的值
				}
				else                                      // 左边的值大于上方的值
				{
					c[i][j] = c[i][j-1];                  // 参考左边的值
					b[i][j] = 2;                          // 参考左边的值
				}
			}
		}
		// c[m][n]的值为相似点的个数
		// 相似度=相似点的个数/两条轨迹的最少点个数
		return ( c[m][n] * 2. / (m + n) );
	}
	
	// 定制冒泡排序  降序
	public double[] Sort(double[] s)
	{
		// 冒泡排序
		for (int i = 0; i < s.length; i++)
		{
			for (int j = s.length - 1; j > i; j--)
			{
				if (s[j] > s[j-1])                               // 降序排序,根据相似度进行比较
				{
					double t_1 = s[j];                           // 相似度的值交换
					String t_2 = Similarity_track[j];            // 伴随轨迹
					String t_3 = Similarity_point[j];            // 伴随相似轨迹点
					
					s[j] = s[j-1];                               // 相似度的值交换
					Similarity_track[j] = Similarity_track[j-1]; // 伴随轨迹
					Similarity_point[j] = Similarity_point[j-1]; // 伴随相似轨迹点
					
					s[j-1] = t_1;                                // 相似度的值交换
					Similarity_track[j-1] = t_2;                 // 伴随轨迹
					Similarity_point[j-1] = t_3;                 // 伴随相似轨迹点
				}
			}
		}
		return s;                                                // 返回排序好的相似度值
	}

	// 9宫格过滤,考虑上下左右四边
	public void clean(int[] matrix)
	{
		//PASS掉边界的情况
		if (matrix[7] % 100 == 1)                 // 最上边
		{
			matrix[6] = 0; matrix[7] = 0; matrix[8] = 0;
		}
		else if(matrix[2] % 100 == 0)             // 最下边
		{
			matrix[1] = 0; matrix[2] = 0; matrix[3] = 0;
		}
		if (matrix[4] < 1)                        // 最左边
		{
			matrix[1] = 0; matrix[4] = 0; matrix[6] = 0;
		}
		else if(matrix[5] > 10000)                // 最右边
		{
			matrix[3] = 0; matrix[5] = 0; matrix[8] = 0;
		}
	}

	// 对x字符数组进行赋值相似轨迹点的编号
	public void print_lcs(int[][] b, int i, int j)
	{
		if ( (i == 0) || (j == 0))           // 如果为0,则返回
			return ;                         // 返回
		if (b[i][j] == 0)                    // 0代表取得左上角的值
		{
			print_lcs(b, i-1, j-1);          // i, j分别减1;进一步进行递归
			x[index++] = i;                  // 相似的点存储到数组x中
		}
		else if (b[i][j] == 1)               // 1代表取得上方的值
			print_lcs(b, i-1, j);            // 行i减1;进一步进行递归
		else                                 // 2代表取得左边的值
			print_lcs(b, i, j-1);            // 列j减1;进一步进行递归
	}
	
	// 重新定义最短距离e和最少点数o
	public void reset_e_o(String[] A, int m)
	{
		double sum = 0;                             // 此编号轨迹的长度
		for (int p=3; p<3*m; p += 3)                // 遍历轨迹点求e值
		{
			// 计算两点之间的欧式距离
			sum += Math.sqrt((Math.pow((Double.valueOf(A[p]) - Double.valueOf(A[p+3])), 2) +
			Math.pow((Double.valueOf(A[p+1]) - Double.valueOf(A[p+4])), 2)));
			// System.out.println(A[p]+" "+ A[p+3]+" "+ A[p+1]+" "+ A[p+4]);
		}
		e = sum / (m-1) * 3;                        // 重新定义最短距离
		o = m / 3;                                  // 重新定义最少点数
	}
	
	// 计算两条轨迹的相似度       例子:compute(73, 33334)   计算73号轨迹与33334号轨迹的相似度
	public double compute(int a, int b)
	{
		String[] A = null, B = null;                                           // 轨迹A 和 轨迹B
		try
		{
			Similarity_track[0] = search(a);                                   // 轨迹A字符串
			Similarity_track[1] = search(b);                                   // 轨迹B字符串
			A = Similarity_track[0].split(",");                                // 轨迹A数组
			B = Similarity_track[1].split(",");                                // 轨迹B数组
		}
		catch (IOException e)
		{}

		int m = Integer.valueOf(A[1]);                                         // 获取矩阵A的长度
		reset_e_o(A, m);                                                       // 根据新点编号的轨迹重新定义值e和值o
		int n = Integer.valueOf(B[1]);                                         // 获取矩阵B的长度
		int[][] array = new int[m+1][n+1];                                     // 定义方向矩阵表
		double value = result(A, B, array);                                    // 计算相似度
		
		// 查找相似点
		x = new int[m+1];                                                      // 初始化相似点存储数组
		print_lcs(array, m, n);                                                // 输出相似轨迹点的编号
	    
		String temp = "";                                                      // 初始化temp字符串
		for (int k = 0; x[k]!=0; k++ )                                         // 遍历x数组,直至不为0
	    {
	    	if (x[k+1] == 0)                                                   // 考虑是否加"," 
	            temp += String.valueOf(x[k]);                                  // 连接所有轨迹点的编号
	    	else
	    		temp += String.valueOf(x[k]) + ",";
	    }
		Similarity_point[1] = temp;                                            // 将temp赋值给全局变量
		index = 0;                                                             // 将全局索引下标置0
		
		return(value);                                                         // 返回相似度的值
	}
	
	// 查找最相似的轨迹Top-10
	public double[] compute(int a) throws IOException
	{
		double[] s = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};  // 初始化10个相似度计算的结果
		
		// 聚类 并提取出所属类别 和 类中的第几个元素
		int t = cluster(a);             // 聚类
		int i, j;                       // i代表所属的类;j代表类中的第几个
		i = t / 10000;                  // i所属的类
		j = t % 10000;                  // j代表类中的第几个
		
		// 初始化需要扫描的矩阵 并 过滤矩阵
		int[] matrix = {i, i-101, i-1, i+99, i-100, i+100, i-99, i+1, i+101};   // 9个矩阵
		clean(matrix);                                                          // 过滤无关矩阵

		// 轨迹A和轨迹B的比较
		String A = search(i, j);                    // 找出指定行的轨迹数据
		int m = Integer.valueOf(A.split(",")[1]);   // 轨迹A的长度
		reset_e_o(A.split(","), m);                 // 根据新点编号的轨迹重新定义值e和值o
		String B;                                   // 需要比较的轨迹数据
		
		double r = 0;                               // 临时存放相似度计算的结果
		
		for (int element: matrix)                   // 遍历需要考虑的矩阵
		{
			if (element == 0)                       // 如果为过滤掉的矩阵则跳过
				continue;
			
			System.out.println(element);
			
	    	FileReader fr = new FileReader("F:\\Trajectory_project\\trajectory\\src\\clusters\\"+element+"_data"); // 普通方式读取文件
	    	BufferedReader bfr = new BufferedReader(fr, 65536);                                                    // 创建缓冲流
	    	while ( (B = bfr.readLine())!=null )           // 读取每行数据
	    	{
	    		if (A.equals(B))                           // 如果A和B是同一条轨迹则跳过
	    			continue;
	    		
	    		int n = Integer.valueOf(B.split(",")[1]);  // 轨迹B的长度
	    		int[][] b = new int[m+1][n+1];             // 方向矩阵表
			    r = result(A.split(","), B.split(","), b); // 相似度计算的结果
			    if (r >= s[9])                             // 如果相似度的计算结果大于最小值
			    {
			    	x = new int[m+1];                      // 初始化相似点存储数组
			    	
			    	print_lcs(b, m, n);                    // 输出相似轨迹点的编号                   
				    
			    	// 覆盖当前最小值
			    	s[9] = r;                              // 当前值替换最小值
				    Similarity_track[9] = B;               // 替换轨迹
				    String temp = "";                      // 初始化字符串
				    for (int k = 0; x[k]!=0; k++ )
				    {
				    	if (x[k+1] == 0)                   // 考虑是否加"," 
				            temp += String.valueOf(x[k]);  // 连接所有轨迹点的编号
				    	else
				    		temp += String.valueOf(x[k]) + ",";
				    }
				    Similarity_point[9] = temp;            // 覆盖当前最小值
				    
				    Sort(s);                               // 重新降序排序
				    index = 0;                             // 将全局索引下标置0
			    }
	    	}
	    	bfr.close();                                   // 关闭缓冲流
	    	fr.close();                                    // 关闭普通文件
		}
		return s;                                          // 返回相似度计算的数组结果
	}
}
