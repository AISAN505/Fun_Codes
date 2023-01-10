#include<stdio>
// This code was written at Jan 10, 2023.
int main(void) {
  int a = 5;
  int *ptr = a;
  /*If you use the direct way, don't use (void *)!!
  Also, for formating pointers, use %p instead of %x!!*/
  printf("The direct address is %p\n", &a);
  /*If you use the indirect way, do use (void *)!!*/
  printf("The direct address is %p\n", (void *)ptr);
}
