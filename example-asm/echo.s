section .bss
    buffer resb 64             ; Reserve 64 bytes for our input

section .text
    global _start

_start:
    ; --- STEP 1: READ INPUT ---
    mov rax, 0                 ; sys_read
    mov rdi, 0                 ; file descriptor 0 (stdin)
    mov rsi, buffer            ; address to store data
    mov rdx, 64                ; max bytes to read
    syscall                    ; RAX now holds the actual number of bytes read

    ; --- STEP 2: ECHO OUTPUT ---
    mov rdx, rax               ; move bytes read into RDX (count for write)
    mov rax, 1                 ; sys_write
    mov rdi, 1                 ; file descriptor 1 (stdout)
    mov rsi, buffer            ; address of data to print
    syscall

    ; --- STEP 3: EXIT ---
    mov rax, 60                ; sys_exit
    xor rdi, rdi               ; return code 0
    syscall
