#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//gcc -fno-stack-protector -o defeatingPie defeatingPie.c

void win()
{
    FILE *flagptr;
    flagptr = fopen("flag.txt", "r");
    if (flagptr == NULL) { //Check if 'flag.txt' exists
        puts("Please create a 'flag.txt' in this folder.");
        exit(1);
    } else {
        puts("Good Job! Here is your flag:");
        char buffer[100];
        size_t bytesRead;
        while ((bytesRead = fread(buffer, 1, sizeof(buffer), flagptr)) > 0) { //fread reads 1 byte at a time into the buffer. The '1' specifies that we are reading 1 byte at a time.
            fwrite(buffer, 1, bytesRead, stdout); //write to stdout from chararray 'buffer'
        }

        fclose(flagptr); //Close the file 'flag.txt'
        exit(0);
    }
}

void userData1()
{
    char buffer[0x40];
    read(0, buffer, 0x40);
    puts("You entered:");
    printf(buffer);
    puts("\nNow enter some more data:");
}

void userData2()
{
    char buffer2[0x20];
    read(0, buffer2, 0x50);
}




int main()
{
    puts("Welcome to Clinical's pwn-labs.");
    puts("This challenge is called: Defeating PIE.");
    puts("In order to solve this challenge you will have to use a format string vulnerability");
    puts("to leak an address and then you can make your BOF to call the win() function.");
    puts("Enter some data:");
    userData1();

    userData2();
    
    return 0;
}

