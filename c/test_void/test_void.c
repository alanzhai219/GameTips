#include <stdio.h>

int main(void) {
	int a[] = {0x01020304, 2019};
	int *b = a;
	char *c = (char*)&a[0];
	printf("b+1:%d\n", *(b+1));
	printf("c+1:%d\n", *(c+1));
	return 0;
}
