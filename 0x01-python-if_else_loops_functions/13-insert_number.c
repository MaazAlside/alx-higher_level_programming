#include "lists.h"

/**
  * insert_node - inserts a number into a sorted singly linked list.
  *@head: first node
  *@number: number to add
  *
  *Return: linked list
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}

	current_node = *head;

	while (current_node->next && current_node->next->n < number)
		current_node = current_node->next;

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
