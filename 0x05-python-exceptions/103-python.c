#include <stdio.h>
#include <Python.h>
#include <time.h>

/**
 * print_python_float - function that gives info of the PyFloatObject.
 * @p: pointer to PyObject.
 *
 * Return: void, no return value.
 */
void print_python_float(PyObject *p)
{
        double obj_value;
        char *str;

        fflush(stdout);
        printf("[.] float object info\n");

        if (!PyFloat_CheckExact(p))
        {
                printf("  [ERROR] Invalid Float Object\n");
                return;
        }

        obj_value = ((PyFloatObject *)p)->ob_fval;
        str = PyOS_double_to_string(obj_value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

        printf("  value: %s\n", str);
}

/**
 * print_python_bytes - function that gives info of the PyFloatObject.
 * @p: pointer to PyObject.
 *
 * Return: void, no return value.
 */
void print_python_bytes(PyObject *p)
{
        Py_ssize_t obj_size = 0, i = 0;
        char *str = NULL;

        fflush(stdout);
        printf("[.] bytes object info\n");

        if (!PyBytes_CheckExact(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        obj_size = PyBytes_Size(p);
        str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));

        printf("  size: %zd\n", obj_size);
        printf("  trying string: %s\n", str);
        printf("  first %zd bytes:", obj_size < 10 ? obj_size + 1 : 10);

        while (i < obj_size + 1 && i < 10)
        {
                printf(" %02hhx", str[i]);
                i++;
        }

        printf("\n");
}

void print_python_list(PyObject *p)
{
        PyObject *obj;
        Py_ssize_t list_size = 0;
        int i = 0;

        fflush(stdout);
        printf("[*] Python list info\n");

        if (PyList_CheckExact(p))
        {
                list_size = PyList_GET_SIZE(p);
                printf("[*] Size of the Python List = %zd\n", list_size);
                printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
                while (i < list_size)
                {
                        obj = PyList_GET_ITEM(p, i);
                        printf("Element %d: %s\n", i, obj->ob_type->tp_name);
                        if (PyBytes_Check(obj))
                        {
                                print_python_bytes(obj);
                        }
                        else if (PyFloat_Check(obj))
                        {
                                print_python_float(obj);
                        }
                        i++;
                }
        }
        else
        {
                printf("  [ERROR] Invalid List Object\n");
        }
}
