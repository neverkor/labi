data segment
mass dw 14, -25, 32, 43, -54, 61, -74, 84, -95, 100
len dw 10
n dw 0
s dw 0
sr dw 0
data ends
stk segment stack
db 256 dup (0)
stk ends
code segment
assume cs:code, ds:data, ss:stk
start:
mov ax, data
mov ds, ax
mov cx, 10
lea bx, mass

cykle:
mov ax, [bx]
cmp ax, 0
jl min
jmp max

min:
mov dx, n
inc dx
mov n, dx
xor dx, dx
add s, ax

max:
add bx, 2
loop cykle

xor dx, dx
mov ax, s
not ax
inc ax
mov bx, n
div bx
not ax
inc ax
mov sr, ax

mov ah, 4ch
mov al, 0
int 21h
code ends
end start
