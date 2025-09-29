#include <stdio.h>
int findCelebrity(int mat[][100], int n) {
    int a = 0, b = n - 1;

    while (a < b) {
        if (mat[a][b] == 1) {
            a++;
        } else {
          
            b--;
        }
    }

    int candidate = a;

    for (int i = 0; i < n; i++) {
        if (i != candidate) {
            if (mat[candidate][i] == 1 || mat[i][candidate] == 0) {
                return -1;
            }
        }
    }
    return candidate;
}
int main() {
    int mat[100][100] = {
        {0, 1, 1},
        {0, 0, 1},
        {0, 0, 0}
    };
    int n = 3;

    int celeb = findCelebrity(mat, n);
    if (celeb == -1)
        printf("-1\n");
    else
        printf("Celebrity Index: %d\n", celeb);

    return 0;
}
