fann2
=====

Python bindings for Fast Artificial Neural Networks 2.2.0 (FANN 2.2.0).


DESCRIPTION
===========

This is a python binding for Fast Artificial Neural Network Library (FANN 2.2.0) that implements multilayer
artificial neural networks with support for both fully connected
and sparsely connected networks. It includes a framework for easy
handling of training data sets. It is easy to use, versatile, well
documented, and fast.

FANN 2.2.0 source:
http://sourceforge.net/projects/fann/files/fann/2.2.0/FANN-2.2.0-Source.zip/download


INSTALLATION
============

Before install the fann2 bindings from pip ensure you have the FANN 2.2.0 software
installed and the libs are accesible in the OS to other softwares.

You can install fann2 from pypi, using either pip or easy_install:

::

    $ pip install fann2

or

::

    $ easy_install fann2


USAGE
=====
Just 

::

    >> from fann2 import libfann 


and then create libfann.neural_net and libfann.training_data objects

::

    >> ann = libfann.neural_net()
    >> train_data = libfann.training_data()


Look at the examples at the FANN documentation and its 
C++ bindings for further reference.
