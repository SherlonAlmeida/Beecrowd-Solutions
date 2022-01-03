max_words = []
text = []

while(True):
	N = int(input())
	
	if (N == 0):
		break
	
	phrase = []
	max_just = 0
	for i in range(N):
		line = input().split()
		
		formatted = ""
		for w in range(len(line)):
			formatted += line[w] + " "
		line = formatted[:-1]
		phrase.append(line)
		
		n_words = len(line)

		if n_words > max_just:
			max_just = n_words
	
	text.append(phrase)
	max_words.append(max_just)

#Percorrendo cada texto
n_texts = len(text)
for i in range(n_texts):
	#Percorrendo cada frase
	n_phrases = len(text[i])
	for j in range(n_phrases):
		n_spaces = max_words[i] - len(text[i][j])
		spaces = ""
		for s in range(n_spaces):
			spaces += " "
		output = spaces + text[i][j]
		print(output)
	if i < n_texts-1:
		print("")