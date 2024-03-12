#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *t;

	t = list;
	if(list == NULL)
		return (0);
	while(t)
	{
		t = list->next;
		if (t == NULL)
			return (0);
		else if (t == list)
			return (1);
	}
	return (0);
}
