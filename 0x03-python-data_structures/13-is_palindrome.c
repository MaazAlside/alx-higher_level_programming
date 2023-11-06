#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if it is a palindrome, 0 if it is not a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head;
	listint_t *fast_node = *head;

	while (fast_node != NULL && fast_node->next != NULL)
	{
		current_node  = current_node->next;
		fast_node = fast_node->next->next;
	}

	while (current_node  != NULL && fast_node != NULL)
	{
		if (current_node->n != fast_node->n)
		{
			return (0);
		}
		current_node  = current_node->next;
		fast_node = fast_node->next;
	}

	return (1);
}
