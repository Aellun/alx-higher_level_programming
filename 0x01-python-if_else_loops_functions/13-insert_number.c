#include "lists.h"

/**
 * insert_node - Funct to Insert num to sorted singly-linked list.
 * @head: A ptr to node  head of the linked list.
 * @number: num being inserted.
 * Return: Inull on failure, ptr to new node on success.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
