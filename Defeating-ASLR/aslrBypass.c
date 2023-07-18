#include <stdio.h>

//gcc -fno-stack-protector -no-pie aslrBypass.c -o aslrBypass

void never_called()
{
	puts("I am never called");
	asm(
		"popq %rdx;"
		"popq %rsi;"
		"popq %rdi;"
	   );
}



int main()
{
	puts("");
	puts("Welcome to Clinical's pwn labs.");
	puts("This challenge is called 'ASLR Bypass'.");
	puts("Please enter some data:");

	char buffer[0x20];
	gets(buffer);

	return 0;
}
