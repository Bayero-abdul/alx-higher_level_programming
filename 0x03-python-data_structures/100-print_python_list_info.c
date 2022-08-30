#include <python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a list (python object)
 */
void print_python_list_info(PyObject *p)
{
	int alloc, i, len = 0;

	len = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < len; i++)
	{
		PyObject *pItem = PyList_GetItem(p, i);

		if (!pItem)
			return;

		printf("Element[%d]: %s\n", i, pItem->ob_type->tp_name);
	}
}
