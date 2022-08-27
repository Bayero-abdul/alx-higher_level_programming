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
	listint_t *current, *temp1, *temp2;
	int first_elem, second_elem;

	if (*head == NULL || (*head)->next == NULL || (*head)->n == (*head)->next->n)
		return (1);

	current = *head;
	first_elem = (*head)->n;
	while (current->next->next != NULL)
		current = current->next;

	second_elem = current->next->n;
	if (first_elem == second_elem)
	{
		temp1 = *head;
		*head = (*head)->next;
		temp2 = current->next;
		current->next = NULL;
		free(temp1);
		free(temp2);
		return (is_palindrome(head));
	}
	else
		return (0);
}
