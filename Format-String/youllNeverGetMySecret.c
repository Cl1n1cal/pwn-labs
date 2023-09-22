#include <stdio.h>
#include <unistd.h>

//gcc -o youllNeverGetMySecret
//Can be solved using:
//%p %p %p %p %p %p %p %p
//or
//%7$llx
//or
//%7$p
//or
//using gdb
int main()
{
    //Secret value
    int secreNum = 0xdeadBeef;

    //Intro
    puts("Welcome to Clinical's pwn labs");
    puts("This challenge is called: youllNevergetMySecret");
    puts("Can you utilize a format string vulnerability and leak the hidden value?");
    puts("\n");

    //actual vulnerability
    char name[0x40] = {0};
    puts("Please enter your name: ");
    read(0, name, 0x40);
    printf(name);
    return 0;
}

