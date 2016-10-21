#include<stdio.h>
int a,b,u,v,n,i,j,ne=1;
int visited[10]={0},min,mincost=0,cost[10][10],TID,nthreads;
int main()
{
 printf("\n Enter the number of nodes:");
 scanf("%d",&n);
 printf("\n Enter the adjacency matrix:\n");
 #pragma omp parallel default(none), private(i,j), shared(cost,n)
 {
 	#pragma omp for
 	 for(i=1;i<=n;i++)
  for(j=1;j<=n;j++)
  {
   scanf("%d",&cost[i][j]);
   if(cost[i][j]==0)
    cost[i][j]=999;
  }
 }
#pragma omp parallel default(none), private(i,j,TID), shared(nthreads,cost,n)
{
TID = omp_get_thread_num();
if (TID == 0)
	 {
	nthreads = omp_get_num_threads();
	printf("Number of threads = (%d) \n",nthreads);
	}
printf("Thread %d starting \n",TID);

#pragma omp for
 visited[1]=1;
 printf("\n");
 while(ne<n)
 {
  for(i=1,min=999;i<=n;i++)
  	for(j=1;j<=n;j++)
    if(cost[i][j]<min)
     if(visited[i]!=0)
     {
      min=cost[i][j];
      a=u=i;
      b=v=j;
     }
     if(/*visited[u]==0 || */visited[v]==0)
  {
   printf("\n Edge %d:(%d %d) cost:%d",ne++,a,b,min);
   mincost+=min;
   visited[b]=1;
 }
  cost[a][b]=cost[b][a]=999;
}
}
 printf("\n Minimun cost=%d",mincost);
return 1;
}
