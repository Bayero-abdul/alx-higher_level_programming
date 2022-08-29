#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int arr[100];
	int i = 0, counter = 0;

	current = *head;
	while (current != NULL)
	{
		arr[i++] = current->n;
		current = current->next;
		counter++;
	}

	current = *head;
	counter = counter / 2;
	while (--counter)
	{
		if (current->n != arr[--i])
			return (0);
		current = current->next;
	}
	return (1);
}
