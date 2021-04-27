#include "lists.h"
/**
 * insert_node - inserts a number int a sorted singly linked list
 * @head: the head of the linked list
 * @number: the number to insert into the ordered linked list
 * Return: newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_node;
	listint_t *ahead_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	current_node = *head;
	ahead_node = *head;
	ahead_node = ahead_node->next;
	while (ahead_node)
	{
		if (new_node->n > current_node->n && new_node->n < ahead_node->n)
			break;
		current_node = current_node->next;
		ahead_node = ahead_node->next;
	}
	current_node->next = new_node;
	new_node->next = ahead_node;
	return (new_node);
}
