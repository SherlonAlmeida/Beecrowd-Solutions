#include<stdio.h>
#include<stdlib.h>

int divide(int *vet, int p, int q, int r){
    int i,j,k = 0,count = 0;
    int w[r-p];
    i = p;
    j = q;
    while(i < q && j < r){
        if(vet[i] <= vet[j])
            w[k++] = vet[i++];
        else{
            w[k++] = vet[j++];
            count += q-i;
        }
    }
    while(i < q)
        w[k++] = vet[i++];
    while(j < r)
        w[k++] = vet[j++];
    for (i = p; i < r; i++)
        vet[i] = w[i-p];
    return count;
}

int mergesort(int *vet, int p, int r){
    int q, esq = 0, dir = 0, inter = 0;
    if(p < r-1){
        q = (p+r)/2;
        esq = mergesort(vet,p,q);
        dir = mergesort(vet,q,r);
        inter = divide(vet,p,q,r);
    }
    return esq + dir + inter;
}

int main(){
    int N = -1, *vet, i, iteracoes;
    while (N != 0){
        scanf("%d", &N);
        if(N != 0){
            vet = (int*)malloc(N*sizeof(int));
            for(i=0; i<N; i++){
                scanf("%d", &vet[i]);
            }
            iteracoes = mergesort(vet, 0, N);
            if(iteracoes%2 == 0){ //Par
                printf("Carlos\n");
            } else{
                printf("Marcelo\n");
            }
            free(vet);
        }
    }
    return 0;
}