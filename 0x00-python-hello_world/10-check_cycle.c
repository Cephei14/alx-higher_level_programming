#include "lists.h"

/**
 * check_cycle - function that check if there is a cycle in a linked list
 * @list: list to check
 * Return: 0 of not cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *t;

	t = list;
	if (list == NULL)
		return (0);
	while (t)
	{
		t = t->next;
		if (t == NULL)
			return (0);
		else if (t == list)
			return (1);
	}
	return (0);
}
