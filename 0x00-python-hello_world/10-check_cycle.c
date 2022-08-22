#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *start = list->next;
	while (start)
	{	
		if (head == start)
			return 1;

		start = start->next;
	}	

	return 0;
}
