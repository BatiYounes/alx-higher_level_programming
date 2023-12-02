#include "lists.h"

/**
 * is_palindrome - function in C that checks if a singly linked list
 * is a palindrome or not.
 * @head: pointer to the first node of singly linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome,
 * empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_node = *head, *second_node = *head;
	listint_t *prev_node = NULL, *tmp;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (first_node && first_node->next)
	{
		first_node = first_node->next->next;
		tmp = second_node->next;
		second_node->next = prev_node;
		prev_node = second_node;
		second_node = tmp;
	}

	second_node = (first_node ? second_node->next : second_node);

	while (second_node)
	{
		if (second_node->n != prev_node->n)
		{
			return (0);
		}
		else
		{
			second_node = second_node->next;
			prev_node = prev_node->next;
		}
	}

	return (1);
}

