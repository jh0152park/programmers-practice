#include <stdio.h>

long fact(unsigned long n) {
    if(n <= 1)
        return 1;
    return n * fact(n - 1);
}

int main(int argc, const char * argv[]) {
    unsigned long n;
    
    scanf("%ld", &n);
    printf("%ld\n", fact(n));
    
    return 0;
}
