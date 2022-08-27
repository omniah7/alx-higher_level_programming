#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: a pointer to the first node of the list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list->next,  *first = list;
	int i;

	for (i = 0; current != NULL; i++)
	{
		if (current == first)
			return (1);
		current = current->next;
	}
	return (0);
}