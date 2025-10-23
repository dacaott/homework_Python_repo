#include "stack.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool checkBrackets(int counter, char *stringWithBrackets) {
  if (counter == 0) {
    return false;
  }
  struct Stack stack = newStack();
  char tmp = ' ';
  for (int i = 0; i < counter; i++) {
    tmp = stringWithBrackets[i];
    if ((tmp == '(') || (tmp == '{') || (tmp == '[')) {
      push(&stack, tmp);
    }
    // если встретилась закрывающаяся и стек не пустой
    else if ((tmp == ')' || tmp == '}' || tmp == ']') && (stack.head != NULL)) {
      char previousBracket = pop(&stack);
      // проверка скобок одного типа через номера из таблицы ASCII
      if ((previousBracket + 1 == tmp) || (previousBracket + 2 == tmp)) {
        continue;
      } else {
        deleteStack(&stack);
        return false;
      }
    }
    // закрывающаяся и пустой стек
    else if ((tmp == ')' || tmp == '}' || tmp == ']') && (stack.head == NULL)) {
      deleteStack(&stack);
      return false;
    }
  }
  if ((stack.head) == NULL) {
    deleteStack(&stack);
    return true;
  }
  deleteStack(&stack);
  return false;
}

int main() {
  // подразумеватся, что пользователь может ввести не только скобки и в кол-ве
  // символов он должен указать всё кол-во символов включая скобки и не скобки.
  int len = 0;
  printf("Введите, сколько символов Вы хотите ввести, закончите ввод, нажав "
         "enter\n");
  printf("На следующей строке введите скобочную последовательность\n");
  scanf("%d", &len);
  // отловим этот '\n'
  getchar();
  char *stringWithBrackets = malloc(len * sizeof(char));
  int counter = 0;
  for (int i = 0; i < len; i++) {
    char tmp = ' ';
    scanf("%c", &tmp);

    if ((tmp == 40) || (tmp == 41) || (tmp == 91) || (tmp == 93) ||
        (tmp == 123) || (tmp == 125)) {
      stringWithBrackets[counter] = tmp;
      ++counter;
    }
  }
  bool isCorrect = checkBrackets(counter, stringWithBrackets);
  if (isCorrect) {
    printf("Скобочная последовательность правильная\n");
  } else {
    printf("Скобочная последовательность неправильная или не было введено ни "
           "одной скобки\n");
  }
  free(stringWithBrackets);
  return 0;
}