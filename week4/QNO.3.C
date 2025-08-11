#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next, *prev;
};

struct Node* reverseDLL(struct Node* head) {
    struct Node* temp = NULL;
    struct Node* curr = head;
    while (curr) {
        temp = curr->prev;
        curr->prev = curr->next;
        curr->next = temp;
        curr = curr->prev;
    }
    if (temp) head = temp->prev;
    return head;
}

struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->next = node->prev = NULL;
    return node;
}

void printList(struct Node* head) {
    while (head) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

int main() {
    struct Node* head = newNode(1);
    head->next = newNode(2); head->next->prev = head;
    head->next->next = newNode(3); head->next->next->prev = head->next;
    head->next->next->next = newNode(4); head->next->next->next->prev = head->next->next;

    printf("Original list: ");
    printList(head);

    head = reverseDLL(head);

    printf("Reversed list: ");
    printList(head);

    return 0;
}
