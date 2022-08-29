#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

listint_t *reverse(listint_t *head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *mid_node;
	int counter = 0;

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		counter++;
	}

	if (counter % 2 != 0)
		counter++;
	counter = counter / 2;

	mid_node = *head;
	while (counter--)
		mid_node = mid_node->next;

	mid_node = reverse(mid_node);

	current = *head;
	while (mid_node)
	{
		if (current->n == mid_node->n)
		{
			current = current->next;
			mid_node = mid_node->next;
		}
		else
			return (0);
	}

	reverse(mid_node);
	return (1);
}

/**
 * reverse - reverses a singly linked list
 * @head: pointer to a singly linked list
 * Return: return a pointer to the reversed list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *result = NULL;

	while (head)
	{
		listint_t *next = head->next;

		head->next = result;
		result = head;
		head = next;
	}
	return (result);
}
