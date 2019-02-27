
.. _Get Started:

Get started
==================
Let's get started with simple examples.
Once you have installed nysol_python, start python and enter code according to the following examples and confirm the operation.

  .. note::  
   When you start python from the tty (a torminal）with the interpreter mode (interactive mode), 
   primary prompt (>>>) for command input, or secondary prompt (as a default) will be shown on the continuation line,
   but those are omitted in the examples on this site. 
   Also, execution results are shown in the comment lines (the line beginning with #). 

Let's look at simple execution examples using data of customers' daily amount of purchase shown by :numref:`hello_intable`. 
MCMD handles structured data table as shown below. 
As of today, data needs to be given by either two-dimensional Python list or CSV format. 

  .. csv-table:: data input example :Structured data table which MCMD can handle
    :name: hello_intable

    customer,date,amount
    A,20180101,5200
    B,20180101,800
    B,20180102,3500
    A,20180105,2000
    B,20180107,4000
 
At first, import MCMD module and store the above table into ``dat`` variable as a two-dimensional list.( :numref:`hello_indat` ).

  .. code-block:: python
    :linenos:
    :caption: Importing MCMD and setting of input data 
    :name: hello_indat

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

The processing to total the amount by customer using the data is shown below.
Let's begin with extracting the specified two necessary columns(``customer`` , ``amount`` ) (:numref:`hello_cutCustAmount` ).
``mcut`` is the method which can execute the function, and ``dat`` variable is specified as an input data ( ``i=`` ).
Then, by specifying ``run`` method, ``mcut`` processing is executed.
MCMD is provding more than 80 different methods having a simple function like this, and those methods are called **Processing Method**.


  .. code-block:: python
    :linenos:
    :caption: The processing of extracting necessary columns
    :name: hello_cutCustAmount

    nm.mcut(f="customer,amount",i=dat).run()
    #[['A', '5200'], ['B', '800'], ['B', '3500'], ['A', '2000'], ['B', '4000']]

For the extracted data, ``msum`` executes the process of calculating the total amount by customer.
In the following example, msum is specified after  ``mcut`` by connecting with ``.`` (dot).
In this format, the output of ``mcut`` is going to be used as input data of ``msum``.
Each method is run on a thread and data is connected by a pipe (FIFO queue) [#f1]_.
Please see the chapter :doc:`flow` for the detail.

  .. code-block:: python
    :linenos:
    :caption: The calculation of total amount by customer
    :name: hello_custAmount

    nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount").run()
    #[['A', '7200'], ['B', '8300']]

By the way, the column names are omitted from the list of above two execution results, this is a specification [#f2]_.
Like the example of :numref:`hello_custAmount` , although MCMD connects methods and processes them step by step,
data flowing between methods is not a Python list but a byte stream of text. 
When a user does not specify the output file explicitly by ``o=`` as the last method ( ``msum`` in the example of :numref:`hello_custAmount` ),
it outputs a list without the header of column names.
 
When the number of MCMD methods to be combined increase, it becomes hard to see if these methods are connected with dots.
In addition, we cannot write any comments and conditional statements between them.
In such a case, we can solve the issue by using  ``<<=`` operator to process the same function.
:numref:`hello_ope` is a rewrite of the same processing shown in :numref:`hello_custAmount` with the ``<<=`` operator.
It additionally registers contents of processing with the variable ``f`` one by one and executes it at the end by ``run`` method.

  .. code-block:: python
    :linenos:
    :caption: Example of using operator ``<<=``
    :name: hello_ope

    f=None
    f <<= nm.mcut(f="customer,amount",i=dat)
    f <<= nm.msum(k="customer",f="amount")
    f.run()
    #[['A', '7200'], ['B', '8300']]

It is possible to connect multiple methods more intricately. Please refer to the chapter " :doc:`flow` " for details. 

Lastly, we introduce an example that processes a structured data table using Python native code. 
MCMD can realize various kind of operation by combining multiple methods as introduced above,
however, you will face difficulty in realizing what you wish by using only those.
In such a case, you can use the iterators built in MCMD.
It makes it possible to connect seamlessly the result processed by MCMD to the iterator.
:numref:`hello_iterator` shows the example.
This connects the result of :numref:`hello_ope` (without ``run``) to the iterator of ``for in``.
This is the iterator that reads line by line,
and outputs the result of the item ``amount`` divided by 100.
``for in`` iterator outputs all data as a string.
MCMD contains some more iterators other than  ``for in`` , which have various functions such as specifying data type, specifying container type, and furthermore the iterator for block unit.
Please see the " :doc:`iterator` " for details.


  .. code-block:: python
    :linenos:
    :caption: Example of using an iterator
    :name: hello_iterator

    f=None
    f <<= nm.mcut(f="customer,amount",i=dat)
    f <<= nm.msum(k="customer",f="amount")
    for line in f:
       print(line[0],int(line[1])/100)
    #A 72.0
    #B 83.0

.. [#f1] To be exact, it only registers the operation methods (mcut, msum, etc) with the process flow object, and execute the process flow which the last run method was registered with. Please refer to the chapter " :doc:`Processing flow<flow>` " for detail.

.. [#f2] If you want to output the item names as the first element, you can do it with the function ``writelist`` . In the example, you only need to write  ``nm.mcut(f="customer,amount",i=dat).msum(k="customer",f="amount").writelist(header=True).run()``.

