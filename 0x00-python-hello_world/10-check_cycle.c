#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: a pointer to the first node of the list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current = list, *checker;
	int i, j;


	for (i = 0; current != NULL; i++)
	{
		checker = list;
		for (j = 0; j < i; j++)
		{
			if (current == checker)
				return (1);
			checker = checker->next;
		}
		current = current->next;
	}
	return (0);
}
