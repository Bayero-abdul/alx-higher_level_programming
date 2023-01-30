#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int alloc, i, len;
	
	len = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < len; i++)
	{
		PyObject *pItem = PyList_GetItem(p, i);
		printf("Element %d: %s\n",i, pItem->ob_type->tp_name);
	}
}
