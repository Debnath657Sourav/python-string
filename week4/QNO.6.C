#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = NULL;
    return node;
}

struct Node* insertSorted(struct Node* head, int data) {
    struct Node* node = newNode(data);
    if (!head) {
        node->next = node;
        return node;
    }

    struct Node* curr = head;
    if (data <= head->data) {
        while (curr->next != head) curr = curr->next; 
        curr->next = node;
        node->next = head;
        head = node;
        return head;
    }
    while (curr->next != head && curr->next->data < data)
        curr = curr->next;

    node->next = curr->next;
    curr->next = node;

    return head;
}

void printList(struct Node* head) {
    if (!head) return;
    struct Node* temp = head;
    do {
        printf("%d ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("\n");
}

int main() {
    struct Node* head = newNode(1);
    head->next = newNode(3);
    head->next->next = newNode(4);
    head->next->next->next = head;

    printf("Original list: ");
    printList(head);

    head = insertSorted(head, 2);
    printf("After inserting 2: ");
    printList(head);

    head = insertSorted(head, 5);
    printf("After inserting 5: ");
    printList(head);

    head = insertSorted(head, 0);
    printf("After inserting 0: ");
    printList(head);

    return 0;
}
