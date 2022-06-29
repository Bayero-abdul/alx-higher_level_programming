#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - checks if a listint_t list has a cycle
* @list: pointer to a listint_t list
* Return: 1 if there is cycle else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *traverse;

	current = list;
	while (current)
	{
		traverse = current->next;
		while (traverse)
		{
			if (current == traverse)
				return (1);
			traverse = traverse->next;
		}
		current = current->next;
	}
	return (0);
}

