#include "lists.h"

/**
  * insert_node - inserts a number into a sorted singly linked list.
  *@head: Double pointer to head of the list.
  *@number: Integer value to insert.
  *
  *Return: Address of the new node, or NULL if it failed.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (current_node == NULL || current_node->n >= number)
	{
		new_node->next = current_node;
		current_node = new_node;
		return (new_node);
	}

	while (current_node && current_node->next->n < number)
		current_node = current_node->next;

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
