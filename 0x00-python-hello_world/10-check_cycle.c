#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *hare = list->next;
	listint_t *tortoise = list->;

	while (hare != NULL)
	{	
		hare = hare->next->next;
		tortoise = tortoise->next;
		
		if (hare == tortoise)
			return 1;
	}
	return 0;
}
