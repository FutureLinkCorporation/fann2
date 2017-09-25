======
README
======


fann2
=====

Python bindings for Fast Artificial Neural Networks 2.2.0 (FANN >= 2.2.0). These
are the original python bindings included with FANN 2.1.0 beta and updated to
include support for python 2.6-3.4.


DESCRIPTION
===========

This is a python binding for Fast Artificial Neural Network Library (FANN >=
2.2.0) that implements multi-layer artificial neural networks with support for
both fully-connected and sparsely-connected networks. It includes a framework
for easily handling training data sets. It is easy to use, versatile, well-
documented, and fast.

FANN 2.2.0 source
-----------------

- http://sourceforge.net/projects/fann/files/fann/2.2.0/FANN-2.2.0-Source.zip/download


INSTALLATION
============

You can install fann2 from pkgsrc or from pypi, using either pip or
easy_install:

wheels
------

    $ pip install ${wheel_file}


pypi
----


    $ pip install fann2
    

or


    $ easy_install fann2

pkgsrc
------


Source installation
...................

Get and install pkgsrc. See `pkgsrc documentation
<http://pkgsrc.org/#index4h1>`_. for platform-specific information.

cd ${PKGSRCDIR}/devel/py-fann2

bmake install


From binaries
.............

Get and install pkgsrc. See `pkgsrc quickstart
<http://pkgsrc.org/#index1h1>`_. for platform-specific information.

pkgin -y install py-fann2

Windows considerations
----------------------

Source installation
...................

- Install Visual C++ Build Tools;
- Install `FANN source code <https://github.com/libfann/fann>`_, using cmake;
- Copy "fanndouble.lib" from FANN installed files to ${python_libs_directory} as "doublefann.lib";
- Install swig for Windows (you will need to set an Enviroment Variable for "swig.exe");
- Run > python setup.py install from PowerShell/Command Prompt.

USAGE
=====
Just 


    >> from fann2 import libfann 


and then create libfann.neural_net and libfann.training_data objects


    >> ann = libfann.neural_net()
    
    >> train_data = libfann.training_data()


Look at the examples in the FANN documentation and its C++ bindings for further
reference.


LICENSE
=======

As with the original python bindings, this package is distributed under the
terms of the GNU Lesser General Public License, Version 2.1. See LICENSE for
full terms and conditions.


LINKS
=====

`fann2 on pypi
<https://pypi.python.org/pypi/fann2>`_.

`py-fann2 in pkgsrc
<http://pkgsrc.se/devel/py-fann2>`_.

`FANN
<http://leenissen.dk/fann/>`_.

`pkgsrc
<http://pkgsrc.org/>`_.


CONTACT
=======

Send us your patches and pull requests! We will release as often as these
changes are received and integrated. There's no reason to have countless
branches of this package. Consider this the official one and that it's being
maintained!

The pkgsrc package is maintained by us as well. We are active users of FANN and
fann2. If you don't have or want a github account, send your patches for this
package or the pkgsrc version to pkgsrc@futurelinkcorporation.com.
