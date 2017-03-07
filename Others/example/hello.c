#include <stdio.h>
#include <unistd.h>


void f(int n, int m)
{
	printf("Number1: %d\n",n);
	printf("Number2: %d\n",m);
}

int main (int argc, char *argv[])
{
   int i= 0;
   int j= 0;
   printf("f() is at %p\n", f);
   while(1)
   {
   	f(i++,j++);
   	sleep(1);
   }
}