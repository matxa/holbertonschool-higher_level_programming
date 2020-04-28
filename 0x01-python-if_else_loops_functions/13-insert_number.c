#include "lists.h"
#include <stdlib.h>

/**
* insert_node - insert node at head
* @head: head of the singly linked list
* @number: value
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *last = *head;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (NULL);
	}

	while (last->next != NULL && last->next->n < new_node->n)
	last = last->next;

	 new_node->next = last->next;
	last->next = new_node;

	return (new_node);
}
