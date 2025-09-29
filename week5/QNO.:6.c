#include <stdio.h>
#include <stdlib.h>

span[]) {
    int stack[n];  
    int top = -1;  

    span[0] = 1;
    stack[++top] = 0; 
  
    for (int i = 1; i < n; i++) {
       
        while (top >= 0 && arr[stack[top]] <= arr[i]) {
            top--;
        }

        span[i] = (top == -1) ? (i + 1) : (i - stack[top]);

        stack[++top] = i;
    }
}

int main() {
    int arr[] = {100, 80, 60, 70, 60, 75, 85};
    int n = sizeof(arr) / sizeof(arr[0]);
    int span[n];

    calculateSpan(arr, n, span);

    for (int i = 0; i < n; i++) {
        printf("%d ", span[i]);
    }

    return 0;
}
