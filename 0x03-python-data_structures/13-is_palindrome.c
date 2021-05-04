#include "lists.h"
/**
 * listlength - checks length of linked list
 * @head: head
 * Return: length of list
 */
int listlength(listint_t **head)
{
	listint_t *node = *head;
	int iter = 0;

	while (node)
	{
		node = node->next;
		iter++;
	}
	return (iter);
}
/**
 * is_palindrome - checks for palindrome
 * @head: head
 * Return: 0 for palindrome, 1 for not
 */
int is_palindrome(listint_t **head)
{
	listint_t *node_start = *head, *node_end = *head;
	int end = listlength(head), end_ptr = 0, halfway;
	int iter = 0, end_tmp = 0, step = 0;

	halfway = end / 2;
	while (halfway != step)
	{
		node_end = *head;
		node_start = *head;
		end_tmp = end - end_ptr - 1;
		iter = 0;
		while (end_tmp > 0)
		{
			node_end = node_end->next;
			end_tmp--;
		}
		while (iter < end_ptr)
		{
			node_start = node_start->next;
			iter++;
		}
		if (node_start->n != node_end->n)
		{
			return (0);
		}
		end_ptr++;
		step++;
	}
	return (1);
}
