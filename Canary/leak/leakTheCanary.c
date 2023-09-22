#include <stdio.h>
#include <unistd.h>

//gcc -o leakTheCanary leakTheCanary.c
//Canary is argument nr. 15 on the stack and can be leaked with %15$p
//or
//%p %p %p %p %p %p %p %p %p %p %p %p %p %p %p
//It will come out with 00 as the last two digits.


int main()
{
    puts("Welcome to Clinical's pwn labs.");
    puts("This challenge is called 'Leak The Canary'");
    puts("Please enter some data:");

    char buffer[0x40];
    read(0, buffer, 0x40);
    
    puts("You entered:");
    printf(buffer);
}
