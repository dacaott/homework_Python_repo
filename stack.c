#include "stack.h"
#include <stdlib.h>

// Инициализация стека
void initStack(Stack *stack) {
  if (stack == NULL)
    return;
  stack->head = NULL;
}

// Добавление элемента
void push(Stack *stack, int value) {
  if (stack == NULL)
    return;

  StackNode *node = (StackNode *)malloc(sizeof(StackNode));
  if (!node)
    return;

  node->value = value;
  node->next = stack->head;
  stack->head = node;
}

// Удаление верхнего элемента и возвращение значения
int pop(Stack *stack) {
  if (stack == NULL || stack->head == NULL) {
    return 0;
  }

  StackNode *oldNode = stack->head;
  int res = oldNode->value;
  stack->head = oldNode->next;
  free(oldNode);
  return res;
}

// Просмотр верхнего элемента без удаления
int peek(const Stack *stack) {
  if (stack == NULL || stack->head == NULL) {
    return 0;
  }
  return stack->head->value;
}

// Проверка, пуст ли стек
bool isEmpty(const Stack *stack) {
  return stack == NULL || stack->head == NULL;
}

// Очистка стека и освобождение памяти
void deleteStack(Stack *stack) {
  if (stack == NULL)
    return;

  while (stack->head != NULL) {
    StackNode *temp = stack->head;
    stack->head = temp->next;
    free(temp);
  }
}