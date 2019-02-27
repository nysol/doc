Installation
==================

Supported operating systems
-----------------------------------
It has been confirmed that nysol operates on widely used operating systems such as Linux, MacOSX, and Bash on Ubuntu on Windows. 
nysol is also available on other UNIX variants. Here is the list of operating systems and their versions which have been confirmed the operation of nysol.

* MacOS 10.9.5(Marverics) or later
* CentOS 7.3 1611
* Ubuntu 16.04 LTS
* Bash on Ubuntu on Windows(Windows 10)

Python version
-----------------------
We have confirmed nysol operation on Python 3.6.5. 
Python 2.x are not supported.

Required Libraries
-----------------------
nysol installation requires following softwares.

* c++compiler
* |boost|
* |lib2xml|

.. |boost| raw:: html

  <a href="http://www.boost.org/" target="_blank">boost C++ library</a>

.. |lib2xml| raw:: html

  <a href="http://xmlsoft.org/" target="_blank">lib2xml library</a>

pip installation
-------------------------------------
Same as other various Python packages, installation can be done by pip. Please refer 
|pypi_nysol| for nysol in Pypi.

  .. code-block:: bash
    :linenos:
    :caption: Installation on MAC OS
    :name: install_pip_mac

    $ brew install boost
    $ pip install nysol

  .. code-block:: bash
    :linenos:
    :caption: Installation on CentOS
    :name: install_pip_centos

    $ sudo yum install boost-devel
    $ sudo yum install libxml2-devel
    $ pip install nysol

  .. code-block:: bash
    :linenos:
    :caption: Installation on Ubuntu,Bash on Windows
    :name: install_pip_bow

    $ sudo apt-get install libboost-all-dev
    $ sudo apt-get install libxml2-dev
    $ pip install nysol
    # Set path of shared Libraries
    # If you need to set up every time you boot, write in bash_profile(It will not be activate until you log-in again.)
    $ export LD_LIBRARY_PATH=/usr/local/lib

  .. |pypi_nysol| raw:: html

    <a href="https://test.pypi.org/project/nysol" target="_blank">https://test.pypi.org/project/nysol</a>

Off-line installaion
-------------------------------------
In an environment where you don't have any internet access, please download the all sources from gitHub in advance, and follow the procedure below.

  .. code-block:: bash
    :linenos:
    :caption: nysol download and off-line installation
    :name: custAmount

    # Download(clone) the all sources in an online environment from the gitHub below.
    $ git clone https://github.com/nysol/nysol_python.git
    # move nysol_python directory in an off-line environment and install as follows.
    $ cd nysol_python
    $ pip install .

Verifying the installation
-------------------------------------
After the installation is completed, run Python and import nysol modules. If there is no error message, nysol is successfully installed. Let's try the examples in the chapter " :doc:`mcmd/hello` " of MCMD module!

  .. code-block:: bash
    :linenos:
    :caption: import modules
    :name: install_import

    $ python
    Python 3.6.5 (default, Apr  4 2018, 11:29:29) 
    [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import nysol.mcmd as nm # import mcmd module
    >>> import nysol.take as tk # import take module

