#include<stdio.h>
int calls = 0;

int fibonacci(int n){
    calls += 1;
    if (n < 2)
        return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

int main(){
    int N, i, entrada, resultado;
    scanf("%d", &N);
    for (i=0; i<N; i++){
        scanf("%d", &entrada);
        resultado = fibonacci(entrada);
        printf("fib(%d) = %d calls = %d\n", entrada, calls-1, resultado);
        calls = 0;
    }
    return 0;
}