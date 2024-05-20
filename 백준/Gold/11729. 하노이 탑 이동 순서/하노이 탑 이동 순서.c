#include <stdio.h>
#include <math.h>

void move_disk(int from, int to) {
    printf("%d %d\n", from, to);
}

void hanoi(int disk, int from, int via, int to) {
    
    if(disk == 1) {
        move_disk(from, to);
    } else {
        hanoi(disk - 1, from, to, via);
        move_disk(from, to);
        hanoi(disk - 1, via, from, to);
    }
}

int main(int argc, const char * argv[]) {
    int disk;
    
    scanf("%d", &disk);
    int run = pow(2, disk) - 1;
    printf("%d\n", run);
    hanoi(disk, 1, 2, 3);
    return 0;
}
