#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/*Read a string until \n and store dinamically in memory*/
char* readLine(FILE* stream) {
    char *str = NULL;
	int pos = 0;
	
	//Reallocate and get all chars from Stream
	do {
		str = realloc(str, pos + 1);
		str[pos] = fgetc(stream);
		pos++;
	} while (str[pos-1]!='\n' && !feof(stream));
	
	//After read all the characters in the Stream, we must replace the last char of string with '\0'
	str[pos-1] = '\0';
	
	//Return the pointer to the string in memory
	return str;
}

int main(void) {
	int N, i, j;
	scanf("%d ", &N);

	for (i=0; i<N; i++){
		char *word = NULL;
        word = readLine(stdin);
		int size = strlen(word);
		//printf("%s\n", word);

		char *reverse = NULL;
		reverse = (char*) malloc ((size+1) * sizeof(char));


		//Cifrando string
		for (j=0; j<size; j++) {
			//Checando letras maiusculas e minusculas
			if ((word[j] > 64 &&  word[j] < 91) || (word[j] > 96 && word[j] < 123)) {
				word[j] = word[j] + 3;
			}
		}
		
		//Invertendo string
		for (j=0; j<size; j++) {
			reverse[j] = word[size-1-j];
		}
		reverse[size] = '\0';

		//Truncando
		int t = floor(size/2);
		for (j=t; j<size; j++) {
			reverse[j] = reverse[j] - 1;
		}
		
		printf("%s\n", reverse);
		free(word);
		free(reverse);
	}

	return 0;
}