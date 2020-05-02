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
	listint_t *new_n;
	listint_t *temp;

	new_n = malloc(sizeof(listint_t));
	if (new_n == NULL)
		return (NULL);

	temp = *head;
	new_n->n = number;
	if (head == NULL || temp->n > new_n->n)
	{
		new_n->next = *head;
		*head = new_n;
		return (new_n);
	}

	while (temp->next != NULL && temp->next->n < new_n->n)
	{
		if ((temp->next->n > new_n->n && temp->n < new_n->n) || new_n->n == temp->n)
		{
			new_n->next = temp->next;
			temp->next = new_n;
			return (new_n);
		}
		temp = temp->next;
	}
	new_n->next = temp->next;
	temp->next = new_n;
	return (new_n);
}
