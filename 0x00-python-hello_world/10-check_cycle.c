#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/*
* check_cycle - checks if there is a cycle in a singly linked list
* @list: pointer to a singly linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{

	listint_t *hare = list;
	listint_t *tortoise = list;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (hare == tortoise)
			return (1);
	}
	return (0);
}
