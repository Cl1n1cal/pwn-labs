#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        printf("hashcode is: %d\n", hashcode);
        for(i=0; i<5; i++){
                res += ip[i];
                printf("i is %d, res is %d in hex %x\n", i, res, res);
        }
        printf("final res: %d in hex %x hashcode %x\n",res, res, hashcode);
        printf("you are %d off", res - 0x21DD09EC);
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
