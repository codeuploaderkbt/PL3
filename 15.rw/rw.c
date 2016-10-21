#include<stdio.h>
#include <time.h>
#include <unistd.h>
#include <omp.h>

int var=10;

int main()
{
 int i=0,NumberofReaderThread=0,NumberofWriterThread;

omp_lock_t writelock,xlock;
omp_init_lock(&writelock);
omp_init_lock(&xlock);

int readCount=0;

int tid=0;
#pragma omp parallel sections shared(readCount) private(i)
{
 #pragma omp section
 {
    i=0;
    printf("\nReader %d is trying to enter into the Database for reading the data",i);

    omp_set_lock(&xlock);
    readCount++;
    if(readCount==1)
    {
      omp_set_lock(&writelock);
    }
    omp_unset_lock(&xlock);

    printf("\nReader %d is reading the database var = %d",i, var); 
    printf("\nReader %d is leaving the database",i);  
   
    omp_set_lock(&xlock);
    readCount--;
    if(readCount==0)
    {
      omp_unset_lock(&writelock);
    }
    omp_unset_lock(&xlock);
 }

#pragma omp section 
{
    i=0;
    printf("\nWriter %d is trying to enter into database for modifying the data",i);
    omp_set_lock(&writelock);
    var++;
    printf("\nWriter %d is writting into the database var = %d",i, var); 

    printf("\nWriter %d is leaving the database",i); 
    omp_unset_lock(&writelock);
}

 #pragma omp section
 {
    i=1;
    printf("\nReader %d is trying to enter into the Database for reading the data",i);

    omp_set_lock(&xlock);
    readCount++;
    if(readCount==1)
    {
      omp_set_lock(&writelock);
    }
    omp_unset_lock(&xlock);

   printf("\nReader %d is reading the database var = %d",i, var); 
    printf("\nReader %d is leaving the database",i);  
   
    omp_set_lock(&xlock);
    readCount--;
    if(readCount==0)
    {
      omp_unset_lock(&writelock);
    }
    omp_unset_lock(&xlock);
 }

#pragma omp section
{
    i=1;
    printf("\nWriter %d is trying to enter into database for modifying the data",i);
    omp_set_lock(&writelock);
var++;
    printf("\nWriter %d is writting into the database var = %d",i, var); 
    printf("\nWriter %d is leaving the database",i); 
    omp_unset_lock(&writelock);
}

#pragma omp section
 {
    i=2;
    printf("\nReader %d is trying to enter into the Database for reading the data",i);

    omp_set_lock(&xlock);
    readCount++;
    if(readCount==1)
    {
      omp_set_lock(&writelock);
    }
    omp_unset_lock(&xlock);

    printf("\nReader %d is reading the database var = %d",i, var); 
    printf("\nReader %d is leaving the database",i);  
   
    omp_set_lock(&xlock);
    readCount--;
    if(readCount==0)
    {
      omp_unset_lock(&writelock);
    }
    omp_unset_lock(&xlock);
 }

}
	sleep(5);
  omp_destroy_lock(&writelock); 
  omp_destroy_lock(&xlock); 
 return 0;
}
