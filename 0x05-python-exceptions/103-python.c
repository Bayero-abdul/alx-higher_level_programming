#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_float(PyObject *p);
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
	
	fflush(stdout);	

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	len = PyObject_Length(p);
        alloc = ((PyListObject *)p)->allocated;
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
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
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

	fflush(stdout);
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

	for (i = 0; i <= len; i++)
	{
		if (i == len)
			printf("%02hhx\n", string[i]);
		else
			printf("%02hhx ", string[i]);
	}
}


/**
* print_python_float - prints an info about Python float object
* @p: float object
*/
void print_python_float(PyObject *p)
{
        double num;
	char *str_float;

	fflush(stdout);
        printf("[.] float object info\n");
        if (!PyFloat_Check(p))
        {
                printf("  [ERROR] Invalid Float Object\n");
                return;
        }

        num = ((PyFloatObject *)p)->ob_fval;
	str_float = PyOS_double_to_string(num, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
        printf("  value: %s\n", str_float);
	PyMem_Free(str_float);
}
