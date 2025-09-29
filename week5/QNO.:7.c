#include <stdio.h>
void nextGreaterElements(int arr[], int n, int nge[]) {
    int stack[n]; 
    int top = -1;  
  
    for (int i = n - 1; i >= 0; i--) {
        while (top >= 0 && stack[top] <= arr[i]) {
            top--;
        }

        nge[i] = (top == -1) ? -1 : stack[top];

        stack[++top] = arr[i];
    }
}

int main() {
    int arr[] = {4, 5, 2, 25};
    int n = sizeof(arr) / sizeof(arr[0]);
    int nge[n];

    nextGreaterElements(arr, n, nge);

    for (int i = 0; i < n; i++) {
        printf("%d ", nge[i]);
    }

    return 0;
}
