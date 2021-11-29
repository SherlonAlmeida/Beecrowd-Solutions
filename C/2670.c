//Inicialmente eu achei que dava para colocar a maquina no andar onde tivesse mais pessoas, visando anular o seu custo,
//porem deu 10% de resposta errada, porque?
/*#include<stdio.h>
int main(){
  int a, b, c, soma;
  scanf("%d", &a);
  scanf("%d", &b);
  scanf("%d", &c);

  if ((a >= b) && (a >= c)){		  //Andar 0
    soma = b*2 + c*4;
  } else if ((c >= a) && (c >= b)){   //Andar 2
	soma = a*4 + b*2;
  } else {                            //Andar 1 Na metade do caminho
    soma = a*2 + c*2;
  } 
  printf("%d\n", soma);
  return 0;
}*/

//Embora essa solucao funcione nos casos apresentados no enunciado do problema, ela nao funciona na realidade!
//Por exemplo, se as entradas forem 10 20 100, se sempre colocar a maquina no andar do meio a resposta vai ser (a*2 + c*2)=220.
//Deu 15% de wrong answer
//Porém a resposta certa eh o mínimo entre os três andares (Ver solucao abaixo)
/*#include<stdio.h>
int main(){
	int a, b, c, soma;
  scanf("%d", &a);
  scanf("%d", &b);
  scanf("%d", &c);
  
  soma = a*2 + c*2; #Colocar a maquina no meio
  printf("%d\n", soma);
	return 0;
}*/


//Aqui, caso a entrada seja 10 20 100, as respostas para o andar A0=(20*2 + 100*4)=440; A1=(10*2 + 100*2)=220;
//e A3=(10*4 + 20*2)=80, logo a resposta eh o menor entre eles, ou seja, 80;
//RESPOSTA CORRETA
#include<stdio.h>
int main(){
	int a, b, c, soma=0, s1=0, s2=0, s3=0;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	s1 = b*2 + c*4; //Andar 0
	s2 = a*2 + c*2; //Andar 1
	s3 = a*4 + b*2; //Andar 2
	
	if ((s1 <= s2) && (s1 <= s3)){
		soma = s1;
	} else if ((s2 <= s1) && (s2 <= s3)){
		soma = s2;
	} else if ((s3 <= s1) && (s3 <= s2)){
		soma = s3;
	}
	
	printf("%d\n", soma);
	return 0;
}