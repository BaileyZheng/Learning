# 找出第n个丑数

## 题目描述
丑数，就是只包含2，3和5质因数的数，其中1也是丑数

前10个丑数为1，2，3，4，5，6，8，9，10，12

要求输入n，输出第n个丑数

## 思路
- naive
从1往后一个一个判断，看是不是丑数，这个想法too naive，数据越大，越慢，越容易超时
```
#include <iostream> 
using namespace std;
int main(){
	int n;
	cin>>n;
	int count = 1;
	int i=1;
	for(i=2;count<n;i++){
		int x = i;
		while(x%30==0){
			x/=30;
		}
		while(x%15==0){
			x/=15;
		}
		while(x%10==0){
			x/=10;
		}
		while(x%6==0){
			x/=6;
		}
		while(x%2==0){
			x/=2;
		}
		while(x%3==0){
			x/=3;
		}
		while(x%5==0){
			x/=5;
		}
		if(x==1){
			count++;
		}
	}
	cout<<i-1<<endl;
	return 0;
}
```

- 快速
将丑数存在数组中，每一个丑数一定是已有的较小丑数的2倍或3倍或5倍，所以采用竞争的方式，生成丑数序列。
```
#include <iostream>     
using namespace std;     
int min(int a, int b, int c)     
{     
    int temp = (a < b ? a : b);     
    return (temp < c ? temp : c);     
}     
int findNum(int n) 
{     
    int* num = new int[n];     
    num[0] = 1;     
    int index2 = 0;     
    int index3 = 0;     
    int index5 = 0;     
    int index = 1;     
    while (index < n)     
    {     
        int val = min(num[index2]*2, num[index3]*3, num[index5]*5);   
        if (val == num[index2]*2) 
            index2++;     
        if (val == num[index3]*3)  
            index3++;     
        if (val == num[index5]*5)     
            index5++;     
        num[index++] = val;     
    } 
    int result = num[n-1];     
    delete[] num;     
    return result;     
} 
int main()     
{     
    int n;  
    cin >> n;  
    cout << findNum(n) << endl;  
    return 0;     
}    
```

## 参考
[1] https://blog.csdn.net/leex_brave/article/details/51766194
