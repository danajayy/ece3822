	.file	"f_00.cc"
	.section	.rodata
.LC2:
	.string	"Hello World"
.LC3:
	.string	"Sum of the sines is: %.2f\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	leal	4(%esp), %ecx
	.cfi_def_cfa 1, 0
	andl	$-16, %esp
	pushl	-4(%ecx)
	pushl	%ebp
	.cfi_escape 0x10,0x5,0x2,0x75,0
	movl	%esp, %ebp
	pushl	%ecx
	.cfi_escape 0xf,0x3,0x75,0x7c,0x6
	subl	$36, %esp
	movl	.LC0, %eax
	movl	%eax, -20(%ebp)
	movl	.LC1, %eax
	movl	%eax, -16(%ebp)
	subl	$12, %esp
	pushl	$.LC2
	call	puts
	addl	$16, %esp
	subl	$8, %esp
	pushl	-16(%ebp)
	pushl	-20(%ebp)
	call	_Z16ece_3822_add_sinff
	addl	$16, %esp
	movl	%eax, -28(%ebp)
	fildl	-28(%ebp)
	fstps	-12(%ebp)
	flds	-12(%ebp)
	subl	$4, %esp
	leal	-8(%esp), %esp
	fstpl	(%esp)
	pushl	$.LC3
	call	printf
	addl	$16, %esp
	movl	$0, %eax
	movl	-4(%ebp), %ecx
	.cfi_def_cfa 1, 0
	leave
	.cfi_restore 5
	leal	-4(%ecx), %esp
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.section	.rodata
	.align 4
.LC0:
	.long	1102053376
	.align 4
.LC1:
	.long	1107558400
	.ident	"GCC: (Ubuntu 4.9.2-10ubuntu13) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
