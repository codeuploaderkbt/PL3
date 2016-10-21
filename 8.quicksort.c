Assignment no.:
Title:-	Implement a Parallel Quick Sort algorithm using 		NVIDIA GPU or equivalent ARM board.
Batch:-
*************************************************************
#include<stdio.h>
#include<omp.h>

int k=0;

int partition(int arr[], int low_index, int high_index)
{
int i, j, temp, key;
key = arr[low_index];
i= low_index + 1;
j= high_index;
while(1)
{
while(i < high_index && key >= arr[i])
    i++;
while(key < arr[j])
    j--;
if(i < j)
{
temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
}
else
{
temp= arr[low_index];
arr[low_index] = arr[j];
arr[j]= temp;
return(j);
}
}
}


void quicksort(int arr[], int low_index, int high_index)
{
int j;

if(low_index < high_index)
{
j = partition(arr, low_index, high_index);
printf("Pivot element with index %d has been found out by thread %d\n",j,k);

#pragma omp parallel sections
{
    #pragma omp section
    {
        k=k+1;
        quicksort(arr, low_index, j - 1);
    }

    #pragma omp section
    {
        k=k+1;
        quicksort(arr, j + 1, high_index);
    }

}
}
}


int main()
{
int arr[100];
int n,i;

printf("Enter the value of n\n");
scanf("%d",&n);
printf("Enter the %d number of elements \n",n);

for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}

quicksort(arr, 0, n - 1);

printf("Elements of array after sorting \n");

for(i=0;i<n;i++)
{
printf("%d\t",arr[i]);
}

printf("\n");
} 

*************************************************************
OUTPUT:-

#Terminal 1:
comp-sl-22@compsl22-OptiPlex-3020:~$ scp quicksort.c root@192.168.7.2:/home
Debian GNU/Linux 7

BeagleBoard.org BeagleBone Debian Image 2014-04-23

Support/FAQ: http://elinux.org/Beagleboard:BeagleBoneBlack_Debian
odd_even.c                                    100% 2413     2.4KB/s   00:00    
comp-sl-22@compsl22-OptiPlex-3020:~$ 

*********************************************************

#Terminal 2:
compsl20@compsl20-OptiPlex-3010:~$ ssh root@192.168.7.2
Debian GNU/Linux 7

BeagleBoard.org BeagleBone Debian Image 2014-04-23

Support/FAQ: http://elinux.org/Beagleboard:BeagleBoneBlack_Debian
Last login: Wed Apr 23 22:16:44 2014 from 192.168.7.1
root@beaglebone:~# ls
root@beaglebone:~# cd /home
root@beaglebone:/home# ls
debian	odd_even.c  oo	six2.c
root@beaglebone:/home# gcc quicksort.c -fopenmp
root@beaglebone:/home# ./a.out

Enter the value of n:
5
Enter the 5 number of elements: 
25
20
15
10
5
Pivot element with index 4 has been found out by thread 0
Pivot element with index 0 has been found out by thread 1
Pivot element with index 3 has been found out by thread 4
Pivot element with index 1 has been found out by thread 5
Elements of array after sorting 
5	10	15	20	25	
root@beaglebone:/home#