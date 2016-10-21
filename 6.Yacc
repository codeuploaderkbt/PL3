Assignment no.:
Title:	Write an application to parse input text file concurrently and compare the result of
concurrent parsing with serial parsing ( Use concurrent YACC parser)
*****************************************************

%{

#include <stdio.h>
#include "y.tab.h"   /*to use declared variables in yacc program*/
extern int scanner;
%}


%option reentrant 
%option noyywrap  

NUMBER      [0-9]+

%%


" "         ;
{NUMBER}    {
                yylval.i = atoi(yytext);
                return(NUMBER);
            }
[^0-9\b]    {
                return(yytext[0]);
            }

%%
--------------------------------------------------------
%{   
#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include <sys/stat.h> 
void * scanner;
FILE *yyin; //input file pointer
%}

%union {
         int i;
       }
%token digit
%lex-param {void * scanner} 
%parse-param {void * scanner}
%start list
%type <i> expr
%token <i> NUMBER 

%left '+' '-'
%left '*' '/'

//rule section
%%

list: |                     
    list stat '\n'
    |
    list error '\n'{ yyerrok; }
    ;

stat:   expr { 
    int g = pthread_self();
    printf("Thread = %d ... Ans = %d\n",g,$1);
     }
    ;

expr: expr '*' expr { $$ = $1 * $3; }
    |
    expr '/' expr { $$ = $1 / $3; }
    |
    expr '+' expr { $$ = $1 + $3; }
    |
    expr '-' expr { $$ = $1 - $3; }
    |
    NUMBER
    ;

%%


//subroutines

struct struct_arg  //to pass parameters to pthread, create structure
{
    unsigned char* file; //here file is parameter e.g.test0,test1,test2
};

int yyerror()
{
    return 1;
}

void *parse(void *arguments)
{
    struct struct_arg *args = (struct struct_arg *)arguments;
    unsigned char* filename;
    filename = args -> file;
    yyin = fopen(filename,"r");
    if(yyin == NULL)
   {
	printf("\n input not received");
     
   }
   else
   {
       yylex_init(&scanner);//initialize the memory for lexer
       yyset_in(yyin,scanner); //to set input parameters
       yyparse(scanner);
       yylex_destroy(scanner); //release the memory for lexer
       
   }

   fclose(yyin);
}

int main(int argc, char *argv[])
{
    int num;
    printf("How many threads you want to create??\n");
    scanf("%d", &num);

    int error, count = 0;
    FILE *fp0, *fp1, *fp2, *main_file;
    char line[256];
    size_t len = 0;
    char read;

    main_file = fopen("test.txt", "r");


        fgets(line, sizeof(line), main_file);
        fp0 = fopen("test0.txt", "w");
	printf("\n line1 = %s",line);
        fprintf(fp0, "%s", line);
        fclose(fp0);


        fgets(line, sizeof(line), main_file);
        fp1 = fopen("test1.txt", "w");
	printf("\n line2 = %s",line);
        fprintf(fp1, "%s", line);
        fclose(fp1);

        fgets(line, sizeof(line), main_file);
        fp2 = fopen("test2.txt", "w");
	printf("\n line3 = %s",line);
        fprintf(fp2, "%s", line);
        fclose(fp2);
	fclose(main_file);



    struct struct_arg arguments[num];


    arguments[0].file = "test0.txt";
    arguments[1].file = "test1.txt";
    arguments[2].file = "test2.txt";

    pthread_t tid[num];
    int j = 0;
    while(j < num)
    {
        error = pthread_create(&(tid[j]), NULL, &parse, (void *) &arguments[j]);
        j++;
    } 

    
    int n = 0;
    while(n < num)
    {
        pthread_join(tid[n], NULL);
	printf("** ");
	n++;
    }
	sleep(30);

    return 0;
}
**********************************************************************
Output:-

comp-sl-19@compsl19-OptiPlex-3020:~/TE56/lex/lexyacc$ yacc -d cy.y
comp-sl-19@compsl19-OptiPlex-3020:~/TE56/lex/lexyacc$ lex cy.l
comp-sl-19@compsl19-OptiPlex-3020:~/TE56/lex/lexyacc$ cc lex.yy.c y.tab.c -o parser.exe -pthread
comp-sl-19@compsl19-OptiPlex-3020:~/TE56/lex/lexyacc$ ./parser.exe
How many threads you want to create??
3

 line1 = 5+6

 line2 = 8*9

 line3 = 4-3
Thread = 149583616 ... Ans = 11
Thread = 141190912 ... Ans = 72
Thread = 132798208 ... Ans = 1
comp-sl-19@compsl19-OptiPlex-3020:~/TE56/lex/lexyacc$ 

