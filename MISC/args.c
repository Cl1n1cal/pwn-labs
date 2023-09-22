#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char buf[32];
int main(int argc, char *argv[]) 
{
        int fd = atoi( argv[1] ) - 0x1234;
        printf("fd is: %d\n", fd);
        int len = 0;
        len = read(fd, buf, 32);
        printf("len is: %d\n", len);
        int myBool = strcmp("LETMEWIN\n", buf);
        printf("mybool %d\n", myBool);
        return 0;

                
}
