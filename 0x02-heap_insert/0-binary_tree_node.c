#include "binary_trees.h"

/**
 * *binary_tree_node - Creates a binary tree node
 *
 * @parent: A pointer to the parent node of the node to create
 * @value: Value to put in the node
 *
 * Return: Pointer to a new node or NULL on failure
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node = malloc(sizeof(binary_tree_t));

	if (!new_node)
	{
		return (NULL);
	}

	new_node->n = value;

	new_node->parent = parent;
	new_node->left = NULL;
	new_node->right = NULL;

	return (new_node);
}
