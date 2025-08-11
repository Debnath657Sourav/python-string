#include <stdio.h>
#include <stdlib.h>
typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->prev = newNode->next = NULL;
    return newNode;
}
Node* append(Node* head, int data) {
    Node* newNode = createNode(data);
    if (head == NULL) return newNode;

    Node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newNode;
    newNode->prev = temp;
    return head;
}
Node* deleteNodeAtPosition(Node* head, int x) {
    if (head == NULL || x <= 0) return head;

    Node* temp = head;
    for (int i = 1; temp != NULL && i < x; i++)
        temp = temp->next;
    if (temp == NULL) return head;
    if (temp == head) {
        head = temp->next;
        if (head != NULL) head->prev = NULL;
    } else {
        if (temp->prev != NULL) temp->prev->next = temp->next;
        if (temp->next != NULL) temp->next->prev = temp->prev;
    }

    free(temp);
    return head;
}
void printList(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
int main() {
    Node* head = NULL;
    head = append(head, 10);
    head = append(head, 20);
    head = append(head, 30);
    head = append(head, 40);
    head = append(head, 50);

    printf("Original List: ");
    printList(head);

    int x = 3; // Position to delete
    head = deleteNodeAtPosition(head, x);

    printf("After deleting position %d: ", x);
    printList(head);

    return 0;
}
