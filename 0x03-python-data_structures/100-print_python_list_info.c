#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to python object list
 *
 * description: compile with 'gcc -Wall -Werror -Wextra -pedantic
 * -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC
 * -I/usr/include/python3.4 100-print_python_list_info.c'
 */
void print_python_list_info(PyObject *p)
{
	int len;

	if (!PyList_CheckExact(p))
	{
		return;
	}
	len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len);

	/* cast PyObject into PyListObject */
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (int i = 0; i < len; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
