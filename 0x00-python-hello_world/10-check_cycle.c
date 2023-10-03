#include "list.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it or not
 * @list: input head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
		return (0);
	while (list)
	{
		temp = list;
		list = list->next;
		if (temp <= list)
			return (1);
	}
	return (0);
}
