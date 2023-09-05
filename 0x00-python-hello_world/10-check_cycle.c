#include "lists.h"

/**
 * check_cycle - determine if there is cycle in linked list
 * @list: the linked list being checked
 * Return: 0 on failure 1 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

