/**************************
Title : Implement n-ary search algorithm using OPENMP.
ASSIGNMENT NO. : B5
Batch : T3
***************************/


# include <stdio.h>
# include <omp.h>


int a[65536],s,test;

int global_size,global_x,n;


void nary_search(int size,int x)
{

    if(size<=n)
    {
       test=0;
       #pragma omp parallel num_threads(n)
	{
	     int tid=omp_get_thread_num();
	     if(a[x+tid]==s)
	     {
		printf("\n FOUND... %d\n",x+tid);
		test=1;
	     }
        }

       if(test==0)
	{
	   printf("\n NOT FOUND....");
	}
     }
     
     else
     {
        test=0;
     	 #pragma omp parallel num_threads(n)
	{
	     int tid=omp_get_thread_num();
	      if(s>=a[tid*size/n+x] && s<=a[tid*size/n+size/n-1+x])
              {
                  printf("IT MAY BE HERE %d.......%d\n" 	,a[tid*size/n+x],a[(tid+1)*size/n-1+x]);
                   global_size=size/n;
		   global_x=tid*global_size+x;
		   test=1;
	      }
	}

    if(test==1)
             nary_search(global_size,global_x);
        else
	     printf("\n not found");
     }
} 



int main()
{

   int i,size=65536,x=0;

  for(i=0;i<=size;i++)
  
    a[i]=i;
    printf("\nENTER NUMBER TO BE SEARCH......");
    scanf("%d",&s);
    printf("\nENTER THE NO.OF THREADS TO BE USE......");
    scanf("%d",&n);

   nary_search(size,x);
return 0;
}


/*****OUTPUT********
comp-sl-12@compsl12-OptiPlex-3020:~/Varsha$ gcc nary_search.c -fopenmp
comp-sl-12@compsl12-OptiPlex-3020:~/Varsha$ ./a.out

ENTER NUMBER TO BE SEARCH......456

ENTER THE NO.OF THREADS TO BE USE......3
IT MAY BE HERE 0.......21844
IT MAY BE HERE 0.......7280
IT MAY BE HERE 0.......2426
IT MAY BE HERE 0.......808
IT MAY BE HERE 269.......538
IT MAY BE HERE 448.......537
IT MAY BE HERE 447.......475
IT MAY BE HERE 456.......465
IT MAY BE HERE 456.......458

 FOUND... 456
******************/



