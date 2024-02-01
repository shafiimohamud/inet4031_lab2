#include <stdio.h>

int main() {
	int a = 2;
	int b = 2;
	int c = a + b;

	printf("C says: Hello World!\n");
	printf("%d + %d = %d\n",a,b,c);

	// This is the update part for the  lab 2 part 2
	char* listOfUsers[] = {"User1", "User2", "User3"};
	int i;
	for (i = 0; i < 3; i++) {
		printf("%s\n", listOfUsers[i]);
	}

	return 0;
}
