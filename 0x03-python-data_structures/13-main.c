#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
	{
	listint_t *head;
	int arr1[] = {1, 17, 972, 50, 98, 98, 50, 972, 17, 1};


	head = NULL;
	for (int i = 0; i < 10; i++)
	{
		add_nodeint_end(&head, arr1[i]);
	}
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	free_listint(head);

	return (0);
}
