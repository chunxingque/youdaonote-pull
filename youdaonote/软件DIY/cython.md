There are several ways to build Cython code:

- Write a distutils/setuptools setup.py. This is the normal and recommended way.





next to the source file for direct import (-i builds “in place”)



 -j option for running multiple parallel build jobs. 





If you need to specify compiler options, libraries to link with or other linker options you will need to create Extension instances manually (note that glob syntax can still be used to specify multiple extensions in one line):

from distutils.core import setup

from distutils.extension import Extension

from Cython.Build import cythonize



extensions = [

    Extension("primes", ["primes.pyx"],

        include_dirs=[...],

        libraries=[...],

        library_dirs=[...]),

    # Everything but primes.pyx is included here.

    Extension("*", ["*.pyx"],

        include_dirs=[...],

        libraries=[...],

        library_dirs=[...]),

]

setup(

    name="My hello app",

    ext_modules=cythonize(extensions),

)



from distutils.core import setup

from Cython.Build import cythonize

from distutils.extension import Extension



sourcefiles = ['example.pyx', 'helper.c', 'another_helper.c']

extensions = [Extension("example", sourcefiles)]



setup(

    ext_modules=cythonize(extensions)

)



Cython.Build.cythonize(module_list, exclude=None, nthreads=0, aliases=None, quiet=False, force=False, language=None, exclude_failures=False, **options)



|   |   |
| - | - |
| Parameters: | module\_list – As module list, pass either a glob pattern, a list of glob patterns or a list of Extension objects. The latter allows you to configure the extensions separately through the normal distutils options. You can also pass Extension objects that have glob patterns as their sources. Then, cythonize will resolve the pattern and create a copy of the Extension for every matching file. |




- nthreads – The number of concurrent builds for parallel compilation (requires the multiprocessingmodule).



## Multiple Cython Files in a Package¶

To automatically compile multiple Cython files without listing all of them explicitly, you can use glob patterns:

setup(

    ext_modules = cythonize("package/*.pyx")

)

You can also use glob patterns in Extension objects if you pass them through cythonize():

extensions = [Extension("*", ["*.pyx"])]



setup(

    ext_modules = cythonize(extensions)

)



### Distributing Cython modules

It is strongly recommended that you distribute the generated .c files as well as your Cython sources, so that users can install your module without needing to have Cython available.



class distutils.core.Extension

The Extension class describes a single C or C++ extension module in a setup script. It accepts the following keyword arguments in its constructor:

| argument name | value | type |
| - | - | - |
| name | the full name of the extension, including any packages — ie. not a filename or pathname, but Python dotted name | a string |
| sources | list of source filenames, relative to the distribution root (where the setup script lives), in Unix form (slash-separated) for portability. Source files may be C, C++, SWIG (.i), platform-specific resource files, or whatever else is recognized by the build\_ext command as source for a Python extension. | a list of strings |








python setup_cython.py build_ext --inplace





























