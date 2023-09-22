#include <stdio.h>
#include <stdlib.h>
//gcc -fno-stack-protector -no-pie aslrBypass.c -o aslrBypass
void also_not_called()
{
	puts("I am also not called");
	asm(
		"popq %rdi;"
		"ret;"		
	   );

}

void never_called()
{
	puts("I am never called");
	asm(
		"popq %rdx;"
		"popq %rsi;"
		"popq %rdi;"
		"ret;"
	   );
}


void first_input()
{
	char buffer[0x20];
	read(0, buffer, 0x100);
}

void second_input()
{
	char buffer2[0x20];
	read(0,buffer2, 0x100);
}

int main()
{
	puts("");
	printf("Welcome to Clinical's pwn labs.");
	puts("This challenge is called 'ASLR Bypass'.");
	puts("Please enter some data:");
	
    first_input();	
	

	puts("thanks");

    second_input();

	return 0;
}
