__author__ = 'weekendlu'
#coding=utf-8
import random

def guessnumber(max_num=100, min_num=0):

	#min_num = int(raw_input('input the min number:'))
	#max_num = int(raw_input('input the max number:'))

	x = random.randint(min_num + 1, max_num - 1)

	print min_num, '-', max_num,

	y = int(raw_input(':'))

	while y != x:
		if y >= max_num:
			print 'What the hell you doing???'
			print min_num, '-', max_num,
		elif y <= min_num:
			print 'What are you fucking doing???'
			print min_num, '-', max_num,
		if x < y < max_num:
			max_num = y
			print min_num, '-', max_num,
		elif min_num < y < x:
			min_num = y
			print min_num, '-', max_num,
		y = int(raw_input(':'))

	print 'you are goddamn right!'

guessnumber()
