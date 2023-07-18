#include <stdio.h>

//gcc -fno-stack-protector -no-pie aslrBypass.c -o aslrBypass

int main()
{
	printf("Welcome to Clinical's pwn labs.\n");
	printf("This challenge is called 'ASLR Bypass'.\n");
	printf("Please enter some data:\n");

	char buffer[0x20];
	gets(buffer);










	return 0;
}
