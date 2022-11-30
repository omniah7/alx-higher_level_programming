#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: the first node
* @number: the number to be added
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = (*head);
	listint_t *target;
	listint_t *next;

	if (current == NULL)
	{
		return (add_nodeint_end(head, number));
	}
	target = malloc(sizeof(listint_t));
	if (target == NULL)
	{
		free(target);
		return (NULL);
	}
	target->n = number;

	if (number < current->n)
	{
		target->next = current;
		(*head) = target;
	}
	next = current->next;
	while (next)
	{
		if (number >= current->n && number <= next->n)
		{
			target->next = next;
			current->next = target;
			return (target);
		}
		current = next;
		next = next->next;
	}

	if (number >= current->n)
	{
		free(target);
		return (add_nodeint_end(head, number));
	}
	return (NULL);
}
