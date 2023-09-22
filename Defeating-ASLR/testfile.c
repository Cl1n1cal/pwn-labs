#include <stdio.h>







int main()
{
	puts("Please enter some data:");

	char buffer[0x20];

	gets(buffer);

	puts("Do it again");

	gets(buffer);


	return 0;

}
