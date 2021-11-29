#include<stdio.h>
#include<stdlib.h>
#define TRUE 1

void popula_matriz(int N, int *M){
    int i, j, k;
    int C=0,B=N-1,E=0,D=N-1;
    for (k=N; k>0; k--){
        for (i=0; i<N; i++){
            for (j=0; j<N; j++){
                if ((i==C) || (i==B))
                    M[i*N+j] = k;
                if ((j==E) || (j==D))
                    M[i*N+j] = k;
            }
        }
        C+=1; B-=1; E+=1; D-=1;
    }
}

void imprime(int N, int *M){
    int i, j;
    for (i=0; i<N; i++){
        for (j=0; j<N; j++){
            if (j==0)
                printf("  %d", M[i*N+j]);
            else{
                if(M[i*N+j] < 10){
                    printf("   %d", M[i*N+j]);
                }
                else if((M[i*N+j] >=10) && (M[i*N+j] <=99)){
                    printf("  %d", M[i*N+j]);
                }
                else if(M[i*N+j] >= 100){
                    printf(" %d", M[i*N+j]);
                }
            }
        }
        printf("\n");
    }
}

int main(){
    int N;
    while(TRUE){
        scanf("%d", &N);
        if (N == 0){
            break;
        }
        int *M;
        M = (int*)malloc(N*N*sizeof(int));
        popula_matriz(N, M);
        imprime(N, M);
        printf("\n");
        free(M);
    }
    return 0;
}