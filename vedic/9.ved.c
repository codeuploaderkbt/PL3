#include<stdio.h>
#include<omp.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    int a,n,N, sum=0,d1[10], d[10],i,j,nj,nj1,t1,t2,t3,tsum=0,k;
	
	printf("enter the n digit number to be squared\n");
	scanf("%d",&N);
	a=N;
	for(i=0;a;i++)//separate out digits 
	{
	 d[i]=a%10;
	 a=a/10;	
	}
	n=i;
      printf("The Number is %d",N);
      printf("\nTotal digits are %d\n",n);

    #pragma omp parallel num_threads(n) private(sum,nj,nj1,t1,t2,t3)
    {
    	#pragma omp for
    	for(j=1;j<=n;j++) //apply the formula for Nn2 = E(j=1ton) 
    	{ 	int id = omp_get_thread_num();
	    	nj=n-j;
		nj1=n-j+1;               
		t1=N%((int) (pow(10,nj)));
		t2=N%((int) (pow(10,nj1)));
		t3= d[nj]*(int) pow(10,nj);
		printf("Thread-%d printing N= %d\t n= %d\t j= %d\t nj= %d \t nj1= %d\t t1= %d\t t2= %d\t t3= %d\n",id,N,n,j,nj,nj1,t1,t2,t3);
		sum=t3*(t1+t2);
		printf("Summation thread-%d is  %d\n",id,sum);
		#pragma omp atomic
		tsum+=sum;

     	}
    }

	printf("the suqare of %d is %d\n",N,tsum);
    return 0;
}

/* OUTPUT :-

comp-sl-09@compsl09-OptiPlex-3020:~$ cd Desktop
comp-sl-09@compsl09-OptiPlex-3020:~/Desktop$ gcc ved.c -fopenmp -lm
comp-sl-09@compsl09-OptiPlex-3020:~/Desktop$ ./a.out
enter the n digit number to be squared
45
The Number is 45
Total digits are 2
Thread-0 printing N= 45	 n= 2	 j= 1	 nj= 1 	 nj1= 2	 t1= 5	 t2= 45	 t3= 40
Thread-1 printing N= 45	 n= 2	 j= 2	 nj= 0 	 nj1= 1	 t1= 0	 t2= 5	 t3= 5
Summation thread-1 is  25
Summation thread-0 is  2000
the suqare of 45 is 2025
comp-sl-09@compsl09-OptiPlex-3020:~/Desktop$ ./a.out
enter the n digit number to be squared
123
The Number is 123
Total digits are 3
Thread-2 printing N= 123	 n= 3	 j= 3	 nj= 0 	 nj1= 1	 t1= 0	 t2= 3	 t3= 3
Summation thread-2 is  9
Thread-0 printing N= 123	 n= 3	 j= 1	 nj= 2 	 nj1= 3	 t1= 23	 t2= 123 t3= 100
Summation thread-0 is  14600
Thread-1 printing N= 123	 n= 3	 j= 2	 nj= 1 	 nj1= 2	 t1= 3	 t2= 23 t3= 20
Summation thread-1 is  520
the suqare of 123 is 15129
comp-sl-09@compsl09-OptiPlex-3020:~/Desktop$ ./a.out
enter the n digit number to be squared
1234
The Number is 1234
Total digits are 4
Thread-2 printing N= 1234	 n= 4	 j= 3	 nj= 1 	 nj1= 2	 t1= 4	 t2= 34 t3= 30
Summation thread-2 is  1140
Thread-3 printing N= 1234	 n= 4	 j= 4	 nj= 0 	 nj1= 1	 t1= 0	 t2= 4	 t3= 4
Summation thread-3 is  16
Thread-0 printing N= 1234	 n= 4	 j= 1	 nj= 3 	 nj1= 4	 t1= 234	 t2= 1234	 t3= 1000
Summation thread-0 is  1468000
Thread-1 printing N= 1234	 n= 4	 j= 2	 nj= 2 	 nj1= 3	 t1= 34	 t2= 234 t3= 200
Summation thread-1 is  53600
the suqare of 1234 is 1522756
comp-sl-09@compsl09-OptiPlex-3020:~/Desktop$ 

*/
