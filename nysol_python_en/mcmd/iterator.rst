
Iterators
=======================
MCMD has iterators that iterate over each row and each key.
You can use those when you can't realize the processing you wish only by combining existing MCMD methods,
those enable you to write Python code that can process by row or key block unit.
:numref:`iterator_list` shows the list of iterators MCMD providing.


  .. list-table:: The list of member methods available for process flow object
    :header-rows: 1
    :name: iterator_list

    * - Method Name: Description
      - Parameter
    * - `__iter__: Row iterator`_
      - None
    * - `getline: Row iterator with specifying output formats`_
      - * ``dtype`` ={column name:str|int|float|bool,...}
        * ``otype`` ="list" | "dict"
        * ``skeys`` =a list of columns
        * ``keys`` =a list of columns
        * ``header`` =True|False
        * ``q`` =True|False
    * - `keyblock: Key block iterator`_
      - * ``dtype`` ={column name:str|int|float|bool,...}
        * ``otype`` ="list" | "dict"
        * ``skeys`` =a list of columns
        * ``keys`` =a list of columns
        * ``header`` =True|False
        * ``q`` =True|False


__iter__: Row iterator
---------------------------
An Iterator method(__iter__) is defined for process flow objects, that makes it possible to perform iterative processing over rows to output into a list.
:numref:`flow_iter` is the example of using for-in to output row by row.
Please note that each value is output as a string.
This is because MCMD is processing all data as a text byte stream internally.
If you want to specify types for each column, you can use the method ``getline``.
Also, it is a specification that the column header is not output, that is also can be output by ``getline`` .


  .. code-block:: python
    :linenos:
    :caption: Script using iterator
    :name: flow_iter

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]
    for line in nm.mcut(f="customer,date,amount",i=dat):
      print(line)

  .. code-block:: sh
    :caption: Execution result of :numref:`flow_iter`
    :name: flow_iter_result

    ['A', '20180101', '5200']
    ['B', '20180101', '800']
    ['B', '20180112', '3500']
    ['A', '20180105', '2000']
    ['B', '20180107', '4000']

getline: Row iterator with specifying output formats
------------------------------------------------------------
``getline`` method is an iterator that can control output formats.
By specifying ``otype = "dict"`` , it is possible to output with the dictionary type format with column names as keys, not as a list.
Also it is possible to output a header row with ``header = True`` .
By the parameter ``dtype``, types of output items are specified, and by using ``otype``, list or dictionary can be specified as a container type.
When ``dtype`` is not specified, all the columns are output as a string, and when ``otype`` is not specified, they are output by a list.
Also, by specifying column names by  ``skeys``, data can be sorted by columns specified in advance.
Furthermore, by specifying  ``keys`` , Key break information can also be output.


.. list-table::
  :header-rows: 1

  * - Parameter
    - Description
  * - | **dtype={column name:type,...}**
      |   optional
      |   default:"str" for all items
    - | Specify by dictionary type data, specify column names for keys, and data types for values
      |   The data types it can convert into are as follows.
      |   "str":String, "int":Integer, "float":Floating point number, "bool":Boolean
      | e.g.) dtype={"customer":"str","date":"str","amount":"int"}
  * - | **otype=type**
      |   optional
      |   default:"list"
    - | Specify the type of data container.
      |   From two types, "list"(list type),"dict"(dictionary type) can be specified.
      |   When "list" is specified, a column header is not output.
      |   When "dict" is specified, keys of dictionaries are column names, and values are the values of the columns.
      | e.g.) otype="dict"
  * - | **skeys=a list of column names**
      |   optional
      |   default:no sorting
    - | Sort in advance. Specify the sorting keys. 
      | e.g.) skeys="amount%nr,customer" # ``amount`` numerical descending order + ``customer`` ascending order
  * - | **keys=a list of columns**
      |   optional
      |   default:no key break information
    - | Output key break information according to a list of columns specified in advance.
      |   Data format of output is tuple like ([row data],top,bottom). 
      | e.g.) keys="customer,date"
  * - | **header=True|False**
      |   optional
      |   default:False
    - | Output a header row, too.
  * - | **q=True|False**
      |   optional
      |   default:False
    - | Do not sort by ``k=`` column in advance. 

:numref:`iter_header` is the same processing as :numref:`flow_iter` with the addition of column header output. 

  .. code-block:: python
    :linenos:
    :caption: Script of using iterator with specifying data types
    :name: iter_header

    f=nm.mcut(f="customer,date,amount",i=dat).getline(header=True)
    for line in f:
      print(line)
    # Followings are output contents
    # ['customer', 'date', 'amount']
    # ['A', '20180101', '5200']
    # ['B', '20180101', '800']
    # ['B', '20180112', '3500']
    # ['A', '20180105', '2000']
    # ['B', '20180107', '4000']


With the same data of :numref:`flow_iter`, :numref:`flow_getline` outputs only ``amount`` in integer(``int`` ),
and specifying the dictionary type(``dict`` ) as a container. 


  .. code-block:: python
    :linenos:
    :caption: Script of using the iterator with specifying data types
    :name: flow_getline

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dict")
    for line in f:
      print(line)
    # {'customer': 'A', 'date': '20180101', 'amount': 5200}
    # {'customer': 'B', 'date': '20180101', 'amount': 800}
    # {'customer': 'B', 'date': '20180112', 'amount': 3500}
    # {'customer': 'A', 'date': '20180105', 'amount': 2000}
    # {'customer': 'B', 'date': '20180107', 'amount': 4000}

:numref:`flow_getline_skeys` is performing iterative processing after sorting ``amount`` in numerically descending order in addition to :numref:`flow_getline`.
To sort by numerically descending order,  ``%nr``  needs to be added after a column name,
it is following the same rule of how to specify of  ``f=`` of  :doc:`msortf<methods/msortf>`.
Internally, specifying data types with ``dtype`` and specifying types of sorting with ``skeys`` operate entirely independently.
For example, given ``skeys="amount%nr",dtype={"amount":"str"}``, sorting order is numerically descending order( ``%nr`` ),
however, ``amount`` is in string( ``"str"`` ) format.


  .. code-block:: python
    :linenos:
    :caption: Iterative processing after sorting by ``amount`` in numerically descending order
    :name: flow_getline_skeys

    f=nm.mcut(f="customer,date,amount",i=dat).getline(dtype=dtype,otype="dict",skeys="amount%nr")
    for line in f:
      print(line)
    # {'customer': 'A', 'date': '20180101', 'amount': 5200}
    # {'customer': 'B', 'date': '20180107', 'amount': 4000}
    # {'customer': 'B', 'date': '20180112', 'amount': 3500}
    # {'customer': 'A', 'date': '20180105', 'amount': 2000}
    # {'customer': 'B', 'date': '20180101', 'amount': 800}

:numref:`flow_getline_keys` adds key break information at the time of sorting by column ``customer`` to the output.
The output format of the container is tuple and it is like ([row data list], first row flag, last row flag).
The first row flag is boolean which becomes ``True`` only when reading the first row of the same key.
The last row frag is boolean, the same as the first row flag, which becomes ``True`` when reading the last row of the same key.
You can use ``skeys`` parameter to specify the order in the same key.
In :numref:`flow_getline_keys` , ``skeys="amount%nr"`` is specified,
as result, output is in the order of ``customer`` ascending order+ ``amount`` numerically descending order.


  .. code-block:: python
    :linenos:
    :caption: Adding key break information by ``customer`` 
    :name: flow_getline_keys

    f=nm.mcut(f="customer,date,amount",i=dat).getline(keys="customer",skeys="amount%nr")
    for line in f:
      print(line)

  .. code-block:: sh
    :caption: Execution result of :numref:`flow_getline_keys`. For example, since the first row of the result is the first row of key item value ``A``, the second element of the tuple is ``True``, and the last row is the last row of the key item ``B``, thus the third element of the tuple is ``True``. 
    :name: flow_getline_result

    (['A', '20180101', '5200'], True, False)
    (['A', '20180105', '2000'], False, True)
    (['B', '20180101', '800'], True, False)
    (['B', '20180107', '4000'], False, False)
    (['B', '20180112', '3500'], False, True)

keyblock: Key block iterator
------------------------------------------
While the method ``getline`` iterates processing row by row, the method ``keyblock`` iterates processing by key block (rows contain the same key value).
Therefore, data is given by a two-dimensional list or a list of dictionaries format.
Parameters that can be specified are the same as ``getline`` method, however, specification of ``keys`` is mandatory.


.. list-table::
  :header-rows: 1

  * - Parameter
    - Description
  * - | **keys=a list of column names**
      |   Mandatory
    - | Specify columns to be key blocks
      |   Data is output with a two-dimensional list (or a list of dictionary type elements) like 
      |   ([[row data 1],[row data 2],...,[row data n])(n is the number of rows contained in the block).
      | e.g.) keys="customer"
  * - | **skeys=a list of column names**
      |   optional
      |   default:no sorting
    - | Specify columns to sort within key blocks
      | e.g.) skeys="amount%n" # ``amount`` Numerically descending order
  * - | **dtype={column name:Type,...}**
      |   optional
      |   default:String"str" for all data
    - | Specify by dictionary type data, specify column names as keys, and data types as values.
      |   The data types it can convert into are as follows.
      |   "str":String, "int":Integer, "float":Floating point number, "bool":Boolean
      | e.g.) dtype={"customer":"str","date":"str","amount":"int"}
  * - | **otype=type**
      |   optional
      |   default:"list"
    - | Specify the type of data container.
      |   From two types, “list”(list type),”dict”(dictionary type) can be specified.
      |   When “list” is specified, a column header is not output.
      |   When “dict” is specified, keys of dictionaries are column names, and values are the values of the columns.
      | e.g.) otype="dict"
  * - | **header=True|False**
      |   optional
      |   default:False
    - | Output a header row, too.
  * - | **q=True|False**
      |   optional
      |   default:False
    - | Do not sort by ``k=`` column in advance.


:numref:`flow_keyblock` is the example of specifying ``customer`` as a key block item using the same data as :numref:`flow_iter`.
As you can see in the output result, processing is iterated by values in ``customer`` column, and data is given by a two dimensional list of row and block.
Also,  ``skeys="date"`` is specified in this case, data is sorted by date within the key blocks of ``customer``.

  .. code-block:: python
    :linenos:
    :caption: Script of using key block iterator 
    :name: flow_keyblock

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).keyblock(keys="customer",skeys="date",dtype=dtype):
    for line in f:
      print(line)
    # [['A', '20180101', 5200], ['A', '20180105', 2000]]
    # [['B', '20180101', 800], ['B', '20180107', 4000], ['B', '20180112', 3500]]

When ``header=True`` is added, a column header row is output as the first row of a two dimensional list( :numref:`flow_keyblock_header` ).

  .. code-block:: python
    :linenos:
    :caption: Example of outputting column header 
    :name: flow_keyblock_header

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).keyblock(header=True,keys="customer",skeys="date",dtype=dtype):
    for line in f:
      print(line)
    # [['customer', 'date', 'amount']]
    # [['A', '20180101', 5200], ['A', '20180105', 2000]]
    # [['B', '20180101', 800], ['B', '20180107', 4000], ['B', '20180112', 3500]]


How to specify ``dtype`` , ``otype`` is the same as the method ``getline``.
:numref:`flow_keyblock_dict` is the example of outputting by the dictionary type using the example of :numref:`flow_keyblock` .

  .. code-block:: python
    :linenos:
    :caption: Example of outputting by the dictionary type using key block iterator
    :name: flow_keyblock_dict

    dtype = {'customer':'str', 'date':'str', 'amount':'int'}
    f=nm.mcut(f="customer,date,amount",i=dat).keyblock(keys="customer",skeys="date",dtype=dtype,otype="dict"):
    for line in f:
      print(line)
    # [{'customer': 'A', 'date': '20180101', 'amount': 5200},{'customer': 'A', 'date': '20180105', 'amount': 2000}]
    # [{'customer': 'B', 'date': '20180101', 'amount': 800},{'customer': 'B', 'date': '20180107', 'amount': 4000},{'customer': 'B', 'date': '20180112', 'amount': 3500}]

Be careful when you use  ``keyblock`` for a large number of rows existing for the same key.
``keyblock`` method tries to unfold data in a key block onto a python list as long as memory allows,
however, when memory usage exceeds the limit, the operation is indefinite.


