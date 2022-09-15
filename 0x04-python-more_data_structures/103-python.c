#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_bytes(PyObject *p);

/**
 *  print_python_list - prints an info about a Python list
 * @p: list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t alloc, i, len;
	const char *type;
	PyListObject *list = (PyListObject *)p;

	len = PyObject_Length(p);

	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < len; i++)
	{
		PyObject *index = PyLong_FromSsize_t(i);

		if (!index)
			return;

		PyObject *pItem = PyObject_GetItem(p, index);

		type = pItem->ob_type->tp_name;
		printf("Element %zd: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		Py_DECREF(index);
	}
}


/**
 * print_python_bytes - prints an info about a Python byte object
 * @p: byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	len = PyObject_Length(p);
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", string);
	if (len > 9)
		len = 9;
	printf("  first %zd bytes: ", len + 1);

	for (i = 0; i <= len && i < 10; i++)
	{
		if (i == len || i == 9)
			printf("%02hhx\n", string[i]);
		else
			printf("%02hhx ", string[i]);
	}
}
