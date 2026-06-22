用好装饰函数

@WINFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))

the result type as first argument, and the callback functions expected argument types as the remaining arguments.



structure的话可以和list类似的方法取用

https://gist.github.com/ethanhs/80f0a7cc5c7881f5921f







### Loading dynamic link libraries



ctypes exports the cdll, and on Windows windll and oledll objects, for loading dynamic link libraries.

>>> from ctypes import *

>>> print(windll.kernel32)  

<WinDLL 'kernel32', handle ... at ...>

>>> print(cdll.msvcrt)      

<CDLL 'msvcrt', handle ... at ...>

>>> libc = cdll.msvcrt      

>>>



On Linux, it is required to specify the filename including the extension to load a library, so attribute access can not be used to load libraries.



>>> cdll.LoadLibrary("libc.so.6")  

<CDLL 'libc.so.6', handle ... at ...>

>>> libc = CDLL("libc.so.6")       

>>> libc                           

<CDLL 'libc.so.6', handle ... at ...>

>>>



### Accessing functions from loaded dlls



Functions are accessed as attributes of dll objects:

>>>

>>> from ctypes import *

>>> libc.printf

<_FuncPtr object at 0x...>

>>> print(windll.kernel32.GetModuleHandleA)  

<_FuncPtr object at 0x...>



Note that win32 system dlls like kernel32 and user32 often export ANSI as well as UNICODE versions of a function. The UNICODE version is exported with an W appended to the name, while the ANSI version is exported with an A appended to the name

windll does not try to select one of them by magic, you must access the version you need by specifying GetModuleHandleA or GetModuleHandleW explicitly, and then call it with bytes or string objects respectively.

Sometimes, dlls export functions with names which aren’t valid Python identifiers, like "??2@YAPAXI@Z". In this case you have to use getattr() to retrieve the function:

>>>

>>> getattr(cdll.msvcrt, "??2@YAPAXI@Z")  

<_FuncPtr object at 0x...>

>>>

On Windows, some dlls export functions not by name but by ordinal. These functions can be accessed by indexing the dll object with the ordinal number:

>>>

>>> cdll.kernel32[1]  

<_FuncPtr object at 0x...>



### Calling functions

>>> print(libc.time(None))  

1150640792

>>> print(hex(windll.kernel32.GetModuleHandleA(None)))  

0x1d000000

>>>

ValueError is raised when you call an stdcall function with the cdecl calling convention, or vice versa:

>>>

>>> cdll.kernel32.GetModuleHandleA(None)  

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: Procedure probably called with not enough arguments (4 bytes missing)

>>>



>>> windll.msvcrt.printf(b"spam")  

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: Procedure probably called with too many arguments (4 bytes in excess)

>>>

To find out the correct calling convention you have to look into the C header file or the documentation for the function you want to call.

There are, however, enough ways to crash Python with ctypes, so you should be careful anyway. The faulthandler module can be helpful in debugging crashes (e.g. from segmentation faults produced by erroneous C library calls).



### Fundamental data types



If you need mutable memory blocks, ctypes has a create_string_buffer() function which creates these in various ways. The current memory block contents can be accessed (or changed) with the raw property; if you want to access it as NUL terminated string, use the value property:



>>> from ctypes import *

>>> p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes

>>> print(sizeof(p), repr(p.raw))

3 b'\x00\x00\x00'

>>> p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string

>>> print(sizeof(p), repr(p.raw))

6 b'Hello\x00'

>>> print(repr(p.value))

b'Hello'

>>> p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer

>>> print(sizeof(p), repr(p.raw))

10 b'Hello\x00\x00\x00\x00\x00'

>>> p.value = b"Hi"

>>> print(sizeof(p), repr(p.raw))

10 b'Hi\x00lo\x00\x00\x00\x00\x00'

>>>

The create_string_buffer() function replaces the c_buffer() function (which is still available as an alias), as well as the c_string() function from earlier ctypes releases. To create a mutable memory block containing unicode characters of the C type wchar_t use the create_unicode_buffer() function.



### Calling functions, continued

>>> printf = libc.printf

>>> printf(b"Hello, %s\n", b"World!")

Hello, World!

14

>>> printf(b"Hello, %S\n", "World!")

Hello, World!

14

>>> printf(b"%d bottles of beer\n", 42)

42 bottles of beer

19

>>> printf(b"%f bottles of beer\n", 42.5)

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ArgumentError: argument 2: exceptions.TypeError: Don't know how to convert parameter 2

>>>

As has been mentioned before, all Python types except integers, strings, and bytes objects have to be wrapped in their corresponding ctypes type, so that they can be converted to the required C data type:

>>>

>>> printf(b"An int %d, a double %f\n", 1234, c_double(3.14))

An int 1234, a double 3.140000

31

>>>



### Calling functions with your own custom data types

You can also customize ctypes argument conversion to allow instances of your own classes be used as function arguments. ctypes looks for an _as_parameter_ attribute and uses this as the function argument. Of course, it must be one of integer, string, or bytes:

>>>

>>> class Bottles:

...     def __init__(self, number):

...         self._as_parameter_ = number

...

>>> bottles = Bottles(42)

>>> printf(b"%d bottles of beer\n", bottles)

42 bottles of beer

19

>>>

If you don’t want to store the instance’s data in the _as_parameter_ instance variable, you could define a property which makes the attribute available on request.



### Specifying the required argument types (function prototypes)

It is possible to specify the required argument types of functions exported from DLLs by setting the argtypes attribute.

argtypes must be a sequence of C data types

>>> printf.argtypes = [c_char_p, c_char_p, c_int, c_double]

>>> printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)

String 'Hi', Int 10, Double 2.200000

37

>>>

Specifying a format protects against incompatible argument types (just as a prototype for a C function), and tries to convert the arguments to valid types:

>>>

>>> printf(b"%d %d %d", 1, 2, 3)

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ArgumentError: argument 2: exceptions.TypeError: wrong type

>>> printf(b"%s %d %f\n", b"X", 2, 3)

X 2 3.000000

13

>>>



If you have defined your own classes which you pass to function calls, you have to implement a from_param()class method for them to be able to use them in the argtypes sequence. 

### Return types

By default functions are assumed to return the C int type. Other return types can be specified by setting the restype attribute of the function object.

Here is a more advanced example, it uses the strchr function, which expects a string pointer and a char, and returns a pointer to a string:

>>>

>>> strchr = libc.strchr

>>> strchr(b"abcdef", ord("d"))  

8059983

>>> strchr.restype = c_char_p    # c_char_p is a pointer to a string

>>> strchr(b"abcdef", ord("d"))

b'def'

>>> print(strchr(b"abcdef", ord("x")))

None

>>>



You can also use a callable Python object (a function or a class for example) as the restype attribute, if the foreign function returns an integer. The callable will be called with the integer the C function returns, and the result of this call will be used as the result of your function call. This is useful to check for error return values and automatically raise an exception:

>>>

>>> GetModuleHandle = windll.kernel32.GetModuleHandleA  

>>> def ValidHandle(value):

...     if value == 0:

...         raise WinError()

...     return value

...

>>>

>>> GetModuleHandle.restype = ValidHandle  

>>> GetModuleHandle(None)  

486539264

>>> GetModuleHandle("something silly")  

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

  File "<stdin>", line 3, in ValidHandle

OSError: [Errno 126] The specified module could not be found.

>>>

WinError is a function which will call Windows FormatMessage() api to get the string representation of an error code, and returns an exception. WinError takes an optional error code parameter, if no one is used, it calls GetLastError() to retrieve it.

Please note that a much more powerful error checking mechanism is available through the errcheck attribute; see the reference manual for details.



### Passing pointers (or: passing parameters by reference)¶

Sometimes a C api function expects a pointer to a data type as parameter, probably to write into the corresponding location, or if the data is too large to be passed by value. This is also known as passing parameters by reference.



ctypes exports the byref() function which is used to pass parameters by reference. 



>>> i = c_int()

>>> f = c_float()

>>> s = create_string_buffer(b'\000' * 32)

>>> print(i.value, f.value, repr(s.value))

0 0.0 b''

>>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",

...             byref(i), byref(f), s)

3

>>> print(i.value, f.value, repr(s.value))

1 3.1400001049 b'Hello'

>>>



### Structures and unions

Structures and unions must derive from the Structure and Union base classes which are defined in the ctypesmodule. Each subclass must define a _fields_ attribute. _fields_ must be a list of 2-tuples, containing a field name and a field type.

The field type must be a ctypes type like c_int, or any other derived ctypes type: structure, union, array, pointer.

Here is a simple example of a POINT structure, which contains two integers named x and y, and also shows how to initialize a structure in the constructor:

>>>

>>> from ctypes import *

>>> class POINT(Structure):

...     _fields_ = [("x", c_int),

...                 ("y", c_int)]

...

>>> point = POINT(10, 20)

>>> print(point.x, point.y)

10 20

>>> point = POINT(y=5)

>>> print(point.x, point.y)

0 5

>>> POINT(1, 2, 3)

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: too many initializers

>>>

You can, however, build much more complicated structures. A structure can itself contain other structures by using a structure as a field type.

Here is a RECT structure which contains two POINTs named upperleft and lowerright:

>>>

>>> class RECT(Structure):

...     _fields_ = [("upperleft", POINT),

...                 ("lowerright", POINT)]

...

>>> rc = RECT(point)

>>> print(rc.upperleft.x, rc.upperleft.y)

0 5

>>> print(rc.lowerright.x, rc.lowerright.y)

0 0

>>>

Nested structures can also be initialized in the constructor in several ways:

>>>

>>> r = RECT(POINT(1, 2), POINT(3, 4))

>>> r = RECT((1, 2), (3, 4))

Field descriptors can be retrieved from the class, they are useful for debugging because they can provide useful information:

>>>

>>> print(POINT.x)

<Field type=c_long, ofs=0, size=4>

>>> print(POINT.y)

<Field type=c_long, ofs=4, size=4>

>>>



### Type conversions

For example, you can pass compatible array instances instead of pointer types. So, for POINTER(c_int), ctypes accepts an array of c_int



### Callback functions¶

ctypes allows creating C callable function pointers from Python callables. These are sometimes called callback functions.

First, you must create a class for the callback function.

The CFUNCTYPE() factory function creates types for callback functions using the cdecl calling convention. On Windows, the WINFUNCTYPE() factory function creates types for callback functions using the stdcall calling convention.

Both of these factory functions are called with the result type as first argument, and the callback functions expected argument types as the remaining arguments.



The callback will then be called with two pointers to items, and it must return a negative integer if the first item is smaller than the second, a zero if they are equal, and a positive integer otherwise.

So our callback function receives pointers to integers, and must return an integer. First we create the type for the callback function:

The function factories can be used as decorator factories, so we may as well write:

>>>

>>> @CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

... def py_cmp_func(a, b):

...     print("py_cmp_func", a[0], b[0])

...     return a[0] - b[0]

...

>>> qsort(ia, len(ia), sizeof(c_int), py_cmp_func)

py_cmp_func 5 1

py_cmp_func 33 99

py_cmp_func 7 33

py_cmp_func 1 7

py_cmp_func 5 7

>>>

Note

 

Make sure you keep references to CFUNCTYPE() objects as long as they are used from C code. ctypes doesn’t, and if you don’t, they may be garbage collected, crashing your program when a callback is made.

Also, note that if the callback function is called in a thread created outside of Python’s control (e.g. by the foreign code that calls the callback), ctypes creates a new dummy Python thread on every invocation. This behavior is correct for most purposes, but it means that values stored with threading.local will not survive across different callbacks, even when those calls are made from the same C thread.



### Accessing values exported from dlls¶

Some shared libraries not only export functions, they also export variables. An example in the Python library itself is the Py_OptimizeFlag, an integer set to 0, 1, or 2, depending on the -O or -OO flag given on startup.

ctypes can access values like this with the in_dll() class methods of the type.

























