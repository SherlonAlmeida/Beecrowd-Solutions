N = int(input())
for i in range(N):
	flag = 1
	message = ""
	line = input()
	n_chars = len(line)
	for j in range(n_chars):
		c = line[j]
		#print(c, end = "")
		if c != ' ':
			if flag == 1:
				message += c
				flag = 0
		else:
			flag = 1 #Se for ponto, libera a proxima letra
	print(message)