#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/*
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to pointer to  a singly linked list
* @number: number to insert into the list
* Return: NULL if failed else return a new_node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{	*head = new_node;
		return (new_node);
	}
	else if ((*head)->next == NULL && new_node->n < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL)
	{
		if (current->next->n > new_node->n)
			break;

		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
