#include "lists.h"
/**
 * print_dlistint - print element of linkedlist
 * @h: head node
 * Return: return number of element present in linkedlist
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *temp;
	size_t i = 0;

	temp = h;
	while (temp != 0)
	{
		printf("%i\n", temp->n);
		i++;
		temp = temp->next;	}
	return (i);
}
