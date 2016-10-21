    #include<omp.h>
    #include<semaphore.h>
    #include<stdio.h>
    #include<unistd.h>

    int var=10;
    int ReadCount=0;

    sem_t Sem;

    void main()
    {
        sem_init(&Sem, 0, 1);
        int ThreadId = 0;
        int NReader, NWriter;
        int i,j;

        printf("\nEnter number of readers: ");
        scanf("%d",&NReader);
        printf("\nEnter number of writers: ");
        scanf("%d",&NWriter);

     #pragma omp parallel num_threads( (NReader+NWriter) ) shared(ThreadId) /*specifies threadId variable is shared among all the threads*/                                                                                                 
        {
            //printf("  in parallel construct");

            #pragma omp for nowait
            for(i=0 ; i<NReader ; i++)
            {
                printf("\nReader %d",i);
				printf("started");
                //sleep(5);

                #pragma omp critical
                {           
                    ReadCount++;
                    if(ReadCount==1)
                        sem_wait(&Sem);
                }

                ThreadId = omp_get_thread_num();
                printf("\n\nReader %d with thread id %d is reading shared variable %d ",i,ThreadId,var);    

                #pragma omp critical
                {           
                    ReadCount--;
                    if(ReadCount==0)
                        sem_post(&Sem);
                }
            //  sleep(5);       
            }
            #pragma omp for nowait
            for(j=0 ; j<NWriter ; j++)
            {
                printf("\nWriter %d",j);
				printf("started");
                sem_wait(&Sem);
                sleep(1);

                var=var+2;

                ThreadId = omp_get_thread_num();

                printf("\nWriter %d with ThreadId %d has updated the shared variable to %d ",j,ThreadId,var);

                sem_post(&Sem);


            }


        }
        //end of parallel construct



    }
/*-----------------------------------------------------------
comp-sl-19@compsl19-OptiPlex-3020:~$ cd Desktop
comp-sl-19@compsl19-OptiPlex-3020:~/Desktop$ gcc e.c -fopenmp
comp-sl-19@compsl19-OptiPlex-3020:~/Desktop$ ./a.out

Enter number of readers: 3

Enter number of writers: 2

Reader 0started
Reader 2started

Reader 2 with thread id 2 is reading shared variable 10 

Reader 0 with thread id 0 is reading shared variable 10 
Writer 0started
Reader 1started
Writer 0 with ThreadId 0 has updated the shared variable to 12 

Reader 1 with thread id 1 is reading shared variable 12 
Writer 1started
Writer 1 with ThreadId 1 has updated the shared variable to 14 comp-sl-19@compsl19-OptiPlex-3020:~/Desktop$ 
-----------------------------------------------------------------------------------------------
./a.out

Enter number of readers: 2

Enter number of writers: 3

Reader 0started
Reader 1started

Reader 1 with thread id 1 is reading shared variable 10 
Writer 1started
Writer 2started

Reader 0 with thread id 0 is reading shared variable 10 
Writer 0started
Writer 0 with ThreadId 0 has updated the shared variable to 12 
Writer 2 with ThreadId 2 has updated the shared variable to 14 
Writer 1 with ThreadId 1 has updated the shared variable to 16 comp-sl-19@compsl19-OptiPlex-3020:~/Desktop$ */

