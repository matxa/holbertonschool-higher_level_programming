#include "lists.h"

/**
* check_cycle - check if the linked list has a cycle
* @list: the given list
* Return: 0 if no cycle or 1 if cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *one_second = list;
	listint_t *two_seconds = list;

	while (two_seconds && one_second && one_second->next)
	{
		two_seconds = two_seconds->next;
		one_second = one_second->next->next;
		if (two_seconds == one_second)
			return (1);
	}
	return (0);
}
