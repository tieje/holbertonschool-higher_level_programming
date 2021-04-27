#include "lists.h"
/**
 * insert_node - inserts a number int a sorted singly linked list
 * @head: the head of the linked list
 * @number: the number to insert into the ordered linked list
 * Return: newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *ahead_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	ahead_node = *head;
	ahead_node = ahead_node->next;
	if (*head == NULL || ahead_node->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current_node = *head;
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
