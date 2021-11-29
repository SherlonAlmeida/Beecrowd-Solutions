/* Autor: Sherlon Almeida da Silva
** Universidade: Universidade de São Paulo
** Data: 14/06/2020
** Descrição: Programa para identificar quadrantes de coordenadas (x,y).
*/

#include <stdio.h>

int main(void) {
  
  double x, y;
  scanf("%lf%lf", &x, &y);
  if (x > 0){
    if (y > 0) {
      printf("Q1\n");
    } else if (y < 0) {
      printf("Q4\n");
    } else {
      printf("Eixo X\n");
    }
  } else if (x < 0){
    if (y > 0) {
      printf("Q2\n");
    } else if (y < 0) {
      printf("Q3\n");
    } else {
      printf("Eixo X\n");
    }
  } else if (x==0) {
    if (y==0){
      printf("Origem\n");
    } else {
      printf("Eixo Y\n");
    }
  }

  return 0;
}