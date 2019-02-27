
MCMD module
------------------
MCMD [#f1]_ is a set of methods developed for the purpose of high-speed processing of large-scale structured data tables. 
MCMD provides more than 80 different methods where each command is specific to a single function (e.g. sort, or join tables).
The basic tenets of what all methods have in common is it reads CSV(comma separated value) data file or a list of Python from standard input, 
and executes a very simple processing method and writes the results to standard output. 
Each method is run by a unit of thread and data is processed by connecting individual method with an inter-process stream called "pipe", 
which enables users to complete their programming within Python without using shells of operating systems such as sh.
MCMD demonstrates its power especially in **data preprocessing** of knowledge discovery process [#f2]_ , 
however it also can be used in other processes.

.. toctree::
   :maxdepth: 2
   :numbered: 2
   :caption: Contents:

   mcmd/hello
   mcmd/data
   mcmd/field
   mcmd/flow
   mcmd/methods/index
   mcmd/common_param
   mcmd/calsel
   mcmd/methods/func_index
   mcmd/autoadd
   mcmd/special
   mcmd/run
   mcmd/iterator

..
   mcmd/workfile
   mcmd/jupyter


パラメータ

.. rubric:: Footnotes

.. [#f1] It is called "M-Command" according to the convention, however it is no longer a command. The "M" in MCMD refers to the inventor Mr. Yasuyuki Matsuda's initial.
.. [#f2] Referring to the set of cycle contains data acquisition, selection, preprocessing, conversion, applying knowledge discovery algorithm, interpretation, and evaluation (Reference: OR encyclopedia [#f3]_ ).
.. [#f3] http://www.orsj.or.jp/~wiki/wiki/index.php/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%9E%E3%82%A4%E3%83%8B%E3%83%B3%E3%82%B0
