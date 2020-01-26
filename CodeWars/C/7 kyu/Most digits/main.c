#include <stddef.h>

int find_longest(int *numbers, size_t numbers_size)
{
  int max_digits = 0;
  int max_number = 0;
  for (int i = 0; i < numbers_size; ++i)
  {
    char str_num[1000];
    sprintf(str_num, "%d", numbers[i]);
    int digits = numbers[i] > 0 ? strlen(str_num) : strlen(str_num) - 1; 
    if(max_digits < digits)
    {
      max_digits = digits;
      max_number = numbers[i];
    }
  }
  
  return max_number;
}