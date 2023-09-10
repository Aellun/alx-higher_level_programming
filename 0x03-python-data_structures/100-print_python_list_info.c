#include <Python.h>

/**
 * print_python_list_info - shows the very basic information about python
 * @p: A list of PyObject
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, c;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (c = 0; c < size; c++)
	{
		printf("Element %d: ", c);

		obj = PyList_GetItem(p, c);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
