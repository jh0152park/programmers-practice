#include <stdio.h>
#include <string.h>

int RUN;

int recursion(const char *s, int l, int r){
    RUN++;
    if(l >= r) return 1;
    else if(s[l] != s[r]) return 0;
    else return recursion(s, l+1, r-1);
}

void isPalindrome(const char *s){
    RUN = 0;
    int ret = recursion(s, 0, strlen(s)-1);
    printf("%d %d\n", ret, RUN);
}

int main(){
    int loop;
    
    scanf("%d", &loop);
    for(int i = 0; i < loop; i++) {
        char s[1001];
        scanf("%s", s);
        isPalindrome(s);
    }
}
