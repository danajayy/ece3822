	.file	"f_01.cc"
	.text
	.globl	_Z16ece_3822_add_sinff
	.type	_Z16ece_3822_add_sinff, @function
_Z16ece_3822_add_sinff:
.LFB2:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$40, %esp
	flds	8(%ebp)
	subl	$8, %esp
	leal	-8(%esp), %esp
	fstpl	(%esp)
	call	sin
	addl	$16, %esp
	fstpl	-40(%ebp)
	flds	12(%ebp)
	subl	$8, %esp
	leal	-8(%esp), %esp
	fstpl	(%esp)
	call	sin
	addl	$16, %esp
	faddl	-40(%ebp)
	fstps	-12(%ebp)
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE2:
	.size	_Z16ece_3822_add_sinff, .-_Z16ece_3822_add_sinff
	.ident	"GCC: (Ubuntu 4.9.2-10ubuntu13) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
