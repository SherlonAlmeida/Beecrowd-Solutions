#include<stdio.h>
#include<stdlib.h>
int main(){
	int a, b, c, i;
	int t1,t2,t3,t4,t5,t6;
	scanf("%d %d %d", &a, &b, &c);
	if(a == b || b == c || c == a){
		printf("S\n");
		exit(-1);
	}
	t1 = a-b; // a-b
	t2 = a-c; // a-c
	t3 = b-c; // b-c
	t4 = (a+b)-c; // a+b -c
	t5 = (a+c)-b; // a+c -b
	t6 = (b+c)-a; // b+c -a
	
	if(t1 == 0 || t2 == 0 || t3 == 0 || t4 == 0 || t5 == 0 ||t6 == 0){
		printf("S\n");
	}
	else{
		printf("N\n");
	}
	return 0;
}