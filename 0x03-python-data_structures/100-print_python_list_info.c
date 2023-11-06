#include <lists.h>
/**
* Check if a linked list is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *p = *head;
	listint_t *q = *head;

	while (q != NULL && q->next != NULL)
	{
		p = p->next;
		q = q->next->next;
	}

	while (p != NULL && q != NULL)
	{
		if (p->n != q->n)
		{
			return (0);
		}
		p = p->next;
		q = q->next;
	}

	return (1);
}
