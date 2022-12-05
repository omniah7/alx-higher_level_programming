#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = (*head);
	int *list;
	int i;

	if (current == NULL || current->next == NULL)
	{
		return (1);
	}

	for (i = 0; current; i++, current = current->next)
	{
		if (i == 0) /* first iteration */
		{
			list = malloc(sizeof(int));
			if (list == NULL)
			{
				return (-1);
			}
			list[0] = current->n;
			continue;
		}
		list = realloc(list, (i + 1) * sizeof(int));
		list[i] = current->n;
	}

	for (int j = 0; j < i / 2; j++)
	{
		if (list[j] != list[i - j - 1])
		{
			free(list);
			return (0);
		}
	}
	free(list);
	return (1);
}
