#include <stdio.h>

void print(int x, int y, int n) {
    if((x / n) % 3 == 1 && (y / n) % 3 == 1) {
        printf(" ");
    } else {
        if(n == 1) {
            printf("*");
        } else {
            print(x, y, n / 3);
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            print(i, j, n);
        }
        printf("\n");
    }
    
    return 0;
}
