# 0x02. Heap Insert


### Basic Binary Tree
```
/**
 * struct binary_tree_s - Binary tree node
 *
 * @n: Integer stored in the node
 * @parent: Pointer to the parent node
 * @left: Pointer to the left child node
 * @right: Pointer to the right child node
 */
struct binary_tree_s
{
    int n;
    struct binary_tree_s *parent;
    struct binary_tree_s *left;
    struct binary_tree_s *right;
};
```

### Max Binary Heap
typedef struct binary_tree_s heap_t;

To match the examples in the tasks, you are given [this function](https://github.com/holbertonschool/0x1C.c)