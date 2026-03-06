section .text
	global _start

start:
	jmp main

main:
	jmp exit

exit:
	mov rax, 60
	xor rdi, rdi
	syscall
