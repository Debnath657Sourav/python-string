#include <stdio.h>

int josephus(int n, int k) {
    int res = 0; // Position in 0-based index
    for (int i = 1; i <= n; i++)
        res = (res + k) % i;
    return res + 1;
}

int main() {
    int n = 7, k = 3;
    printf("Survivor position: %d\n", josephus(n, k));
    return 0;
}
