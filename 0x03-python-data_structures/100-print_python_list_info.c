#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - C function that prints some basic info about Python lists.
 * @p: pointer to python object (list).
 *
 * Return: void, no return.
 */
void print_python_list_info(PyObject *p)
{
	long int list_size = PyList_Size(p);
	int i;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", object->allocated);

	for (i = 0; i < list_size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
	}
}

