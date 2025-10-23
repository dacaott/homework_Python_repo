#pragma once
#include <stdbool.h>

typedef struct StackNode {
  int value;
  struct StackNode *next;
} StackNode;

typedef struct Stack {
  StackNode *head;
} Stack;

// Инициализация стека
void initStack(Stack *stack);

// Добавление элемента в стек
void push(Stack *stack, int value);

// Удаление верхнего элемента и возвращение значения
int pop(Stack *stack);

// Просмотр верхнего элемента без удаления
int peek(const Stack *stack);

// Проверка, пуст ли стек
bool isEmpty(const Stack *stack);

// Очистка стека и освобождение памяти
void deleteStack(Stack *stack);