#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that print some info about python list
 * @p: a python object
 * Return: 0
 */

void print_python_list_info(PyObject *p)
{
	int list_size, a, i;

	i = 0;
	PyObject *obj;

	list_size = PyList_Size(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", a);
	while (i < list_size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
