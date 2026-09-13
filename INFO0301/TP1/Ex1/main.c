#include <stdio.h>
#include <stdlib.h>

void ech2(int *p1, int *p2);
void ord2(int *p1, int *p2);
void ord3(int *p1, int *p2, int *p3);
int extr(int x, int a, int b);

int main(void){
    int a, b, x;
    
    scanf("%d%d%d", &a, &b, &x);
    ord3(&a, &x, &b);
    printf("a = %d \nb = %d \nx = %d \n", a,b,x);

    x = extr(x,a,b);
    printf("\nx = %d\n", x);
    
    return EXIT_SUCCESS;
}

void ech2(int *p1, int *p2){
    int x = *p1;
    *p1 = *p2;
    *p2 = x;
}

void ord2(int *p1, int *p2){
    if (*p1>*p2)
        ech2(p1,p2);
}

void ord3(int *p1, int *p2, int *p3){
    ord2(p1,p2);
    ord2(p2,p3);
    ord2(p1,p2);
}

int extr(int x, int a, int b){
    int res;
    if ((b-x)>(x-a))
        return res = a;
    else
        return res = b;
}