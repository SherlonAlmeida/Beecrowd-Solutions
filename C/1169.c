#include<stdio.h>
#include<math.h>
int main(){
    int N, i, j;
    scanf("%d", &N);
    for(i=0; i<N; i++){
        int X;
        unsigned long long int graos=1, ant=1;
        double KG = 0.0;
        scanf("%d", &X);
        if (X>=63){
            for(j=2; j<X+1; j++){
                graos += ant;
                ant = ant*2;
            }
            KG = graos/6000;
        } else{
            for(j=2; j<X+1; j++){
                graos += (ant*2);
                ant = ant*2;
            }
            KG = graos/12000;
        }
        printf("%.0lf kg\n", floor(KG));
    }
    return 0;
}