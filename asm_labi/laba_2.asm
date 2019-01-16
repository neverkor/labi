;O= A - 3 (A + A) + N mod 4
MODEL small
STACK 256
DATASEG
a dw 10
b dw 20
c dw 30
x dw ?
exCode DB 0
CODESEG
Start:
mov ax,@data
mov ds,ax
;
mov ax,a
mov bx,b
add ax,bx
mov bx,3
mul bx
neg ax
mov bx,a
add ax,bx
mov cx,ax
mov ax,c
mov bl,4
div bl
mov al,ah
xor ah,ah
mov bx,ax
mov ax,cx
add ax,bx
mov x,ax
:neg ax
;
Exit:
mov ah, 04Ch
mov al, [exCode]
int 21h
END Start