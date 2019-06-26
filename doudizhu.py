#有1——10、J、Q、K各四张以及大小王，现在初始除了大小王以外均为4张，每次输入一个就会减少一。





def judge_num(instruct,num):
	
	# str = instruct.split("")
	# length = len(instruct)
	# print (length)
	for letter in instruct:
		if letter == '1':
			num[0] = num[0] - 1
		if letter == '2':
			num[1] = num[1] - 1
		if letter == '3':
			num[2] = num[2] - 1
		if letter == '4':
			num[3] = num[3] - 1
		if letter == '5':
			num[4] = num[4] - 1
		if letter == '6':
			num[5] = num[5] - 1
		if letter == '7':
			num[6] = num[6] - 1
		if letter == '8':
			num[7] = num[7] - 1
		if letter == '9':
			num[8] = num[8] - 1
		if letter == '0':
			num[9] = num[9] - 1
		if letter == 'q' or letter == 'Q':
			num[10] = num[10] - 1
		if letter == 'w' or letter == 'W':
			num[11] = num[11] - 1
		if letter == 'e' or letter == 'E':
			num[12] = num[12] - 1
		if letter == 'a' or letter == 'A':
				for x in range(13):
					num[x] = 4
		
	for x in range(13):
		if num[x] < 0:
			num[x] = 0
	return num



if __name__ == '__main__':   
	num=[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4];
	while True:
		print('\n')
		print('3 4 5 6 7 8 9 10 J Q K A 2' )
		print(num[2],num[3],num[4],num[5],num[6],num[7],num[8],num[9],'',num[10],num[11],num[12],num[0],num[1])
		print('\n')
		instruct = input('输入：')
		judge_num(instruct,num)
		
