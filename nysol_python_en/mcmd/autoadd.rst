
Automatic addition of methods
-------------------------------

When we register some MCMD methods, there are cases that MCMD method(s) may be added automatically before executing them with the ``run`` method.
Such conditions and details are explained below.


Addition of msortf accompanied by key break processing
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
The method msortf is added automatically before the method using the key break processing (processing on the key item basis). 
The manual of each method specifies whether the msortf method will be automatically added or not.
It also applies to the iterators such as ``keyblock`` which is for key basis and ``getline`` method specifying ``k=`` .
If you want to suppress automatic addition of msortf method, you only need to specify ``q=True`` .
:numref:`autoadd_sort` shows the example using ``msum`` method.
When ``q=True`` is specified, we see that the key break processing is performed in the order of the input data.
However, since the automatic addition of msortf function is the function built in each method,
even if you display contents with `` drawModelsDS`` etc., it will not be output,
even if you display a message at runtime, the END message of msortf will not be displayed.


  .. code-block:: python
    :linenos:
    :caption: Examples with and without the automatic sort
    :name: autoadd_sort

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["customer","amount"],
    ["A",5200],
    ["B",800],
    ["B",3500],
    ["A",2000],
    ["B",4000]
    ]
    >>> f1=nm.msum(k="customer",f="amount",i=dat)
    >>> f1.run()
    [['A', '7200'], ['B', '8300']]
    >>> f2=nm.msum(k="customer",f="amount",i=dat,q=True)
    >>> f2.run()
    [['A', '5200'], ['B', '4300'], ['A', '2000'], ['B', '4000']]


.. _autoadd_keybreak:

Key break processing
::::::::::::::::::::::::::
Key break processing is a processing method that performs specific processing for each same key item value on the premise that the items have been sorted.
Key break processing is broadly divided into two types of processes.
First is key break processing for aggregate calculation (referred to as "aggregate key break processing" below), 
and the other is key break processing for joins (referred to as "join key break processing" below ).

You can think that join key break processing is executed by methods that contain "join" or "common" in their method names such as :doc:`mjoin<methods/mjoin>` and :doc:`mcommon<methods/mcommon>`,
and aggregate key break processing is carried out by all other methods that have ``k=`` parameter.

For example, ``msum`` that does aggregate key processing, detects the change of the value in the key field and then executes 
total processing for each same key.
Therefore, it is necessary to sort the records by the key field in advance, (Unless input file is sorted in advance) ``msum`` aggregates after it additionally processes sorting internally.


Join key break processing is slightly more complicated, for example,  ``mjoin`` compares the values in the key fields in two files.
It keeps reading the data file that has a smaller value in the key field and executes join processing when the key fields of the two files have the same value.
As described, it compares the sizes of the values in the key fields, for the key break processing for join, there is a need that both data files have been sorted by the key field beforehand.
Therefore, ``mjoin`` adds internally the sorting process on two data files at first.


In both key break processing, basically, the sort is done by ascending string order, however, in the join key processing by numerical range such as ``mrjoin`` , the sort is processed by ascending numerical order.


Just by specifying the key field by ``k=``, each method automatically determines whether it needs to sort records or not, and it does when necessary, so basically, users don't need to think about sorting files. 
However, it does not mean that sorting is not required, you need to note that each method processes sorting internally.
Depending on the structure of the script, sorting processing may occur very often, which causes low performance. 


:numref:`autoadd_keybreak_sort` shows an example.
This is a simple processing which joins the list ( ``purchase`` ) which contains data of which customer( ``customer`` ) purchased, when( ``date`` ), at which store( ``store`` ),
with other three lists, customer names( ``custName`` ), age( ``age`` ), store names( ``storeName`` ).
In the processing flow ``f1`` , the order of the join key is  ``customer`` , ``store`` , ``customer`` , sort was processed three times,
however, in the processing flow ``f2`` , the order of the join key is ``customer`` , ``customer`` , ``store`` , as the second join key is the same as the first key, it requires one less sorting.


.. code-block:: python
  :linenos:
  :caption: Different sorting load on different order of methods
  :name: autoadd_keybreak_sort

  import nysol.mcmd as nm

  purchase=[
  ["customer","date","store"],
  ["A","20181019","p"],
  ["B","20181019","q"],
  ["B","20181022","q"],
  ["A","20181021","q"],
  ["B","20181023","p"]
  ]

  custName=[
  ["customer","custName"],
  ["A","Ken"],
  ["B","Lisa"]
  ]

  age=[
  ["customer","age"],
  ["A",30],
  ["B",28]
  ]

  storeName=[
  ["store","storeName"],
  ["p","TokyoStore"],
  ["q","OsakaStore"]
  ]

  f1=None
  f1 <<= nm.mjoin(k="customer", m=custName, i=purchase)
  f1 <<= nm.mjoin(k="store", m=storeName)
  f1 <<= nm.mjoin(k="customer", m=age)
  result1=f1.run(msg="on")
  print(result1)
  # [['A', '20181019', 'p', 'Ken', 'TokyoStore', '30'], ['A', '20181021', 'q', 'Ken', 'OsakaStore', '30'], ['B', '20181023', 'p', 'Lisa', 'TokyoStore', '28'], ['B', '20181019', 'q', 'Lisa', 'OsakaStore', '28'], ['B', '20181022', 'q', 'Lisa', 'OsakaStore', '28']]

  f2=None
  f2 <<= nm.mjoin(k="customer", m=custName, i=purchase)
  f2 <<= nm.mjoin(k="store", m=storeName)
  f2 <<= nm.mjoin(k="customer", m=age)
  result2=f2.run(msg="on")
  print(result2)
  # [['A', '20181019', 'p', 'Ken', '30', 'TokyoStore'], ['B', '20181023', 'p', 'Lisa', '28', 'TokyoStore'], ['A', '20181021', 'q', 'Ken', '30', 'OsakaStore'], ['B', '20181019', 'q', 'Lisa', '28', 'OsakaStore'], ['B', '20181022', 'q', 'Lisa', '28', 'OsakaStore']]

.. _autoadd_io:

Data conversion by input and output
'''''''''''''''''''''''''''''''''''''''''''''
When a list is specified by ``i=`` , many MCMD methods can read the list data as input data.
On the other hand, MCMD methods handle all the data as a text byte stream internally.
Thus, the list needs to be converted into a byte stream.
The methods which convert the input list into the byte stream is  ``readlist`` ,
the methods which convert the output byte stream into the list is  ``writelist`` .
Therefore, when the list is specified with ``i=`` , ``readlist`` will be added,
and when the output is not specified explicitly/implicitly,  ``writelist`` will be added.

  .. code-block:: python
    :linenos:
    :caption: The example of automatic addition of readlist and writelist
    :name: autoadd_list

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["customer","amount"],
    ["A",5200],
    ["B",800],
    ["B",3500],
    ["A",2000],
    ["B",4000]
    ]
    >>> f=nm.msum(k="customer",f="amount",i=dat)
    >>> f.drawModelD3("autoadd_list.html")
    >>> f.run()
    [['A', '7200'], ['B', '8300']]

  .. figure:: figure/autoadd_list.png
    :scale: 40%
    :align: center
    :name: autoadd_list.png
    :target: ../_static/autoadd_list.html

    The processing flow readlist and writelist are automatically added

Same as above, the methods that convert CSV files into a byte stream and vice versa are  ``readcsv`` and ``writecsv``, respectively.
However, when MCMD methods are used in an ordinary way such as specifying a file names with ``i=`` ``o=`` , this conversion is processed within the methods, thus
``readcsv`` or ``writecsv`` will not be automatically added.
The typical example that ``writecsv`` is automatically added is when we specify ``o=filename`` in the middle of the flow.
:numref:`autoadd_csv` shows the example.
It is a simple flow that just connects two ``mcut`` with no meaning.
The first  ``mcut`` outputs the half-processed data into the CSV file  ``tmp.csv``,
addition of ``m2tee`` branches the stream into two (described later), and after buffered by ``mfifo`` (described later),
it connects one branch to  ``writecsv`` and the other to  ``mcut``.


  .. code-block:: python
    :linenos:
    :caption: Example of automatic addition of writecsv
    :name: autoadd_csv

    >>> nm.mcut(f="customer,amount",i=dat,o="tmp.csv").mcut(f="customer").drawModelD3("autoadd_csv.html")

  .. figure:: figure/autoadd_csv.png
    :scale: 40%
    :align: center
    :name: autoadd_csv.png
    :target: ../_static/autoadd_csv.html

    The processing flow that writecsv is automatically added

Addition of m2cat by merging process flows
'''''''''''''''''''''''''''''''''''''''''''''
When you want to merge the outputs of two processing flows (merging rows), you can realize that by giving multiple processing flow objects to ``i=`` of MCMD methods like ``i=[obj1,obj2,...`` .  
At that time, as the method that merges data output by multiple flows,  ``m2cat`` is automatically added.
In :numref:`autoadd_m2cat` , the two processing flow objects ``f1`` and ``f2`` constructed by one ``mcut`` are specified as input data for the method ``msum`` .
In this case,  ``m2cat`` is inserted before ``msum`` .


  .. code-block:: python
    :linenos:
    :caption: Example of automatic addition of m2cat
    :name: autoadd_m2cat

    >>> f1=nm.mcut(f="customer,amount",i=dat)
    >>> f2=nm.mcut(f="customer,amount",i=dat)
    >>> f3=nm.msum(k="customer",f="amount",i=[f1,f2])
    >>> f3.drawModelD3("autoadd_m2cat.html")
    >>> f3.run()
    [['A', '14400'], ['B', '16600']]

  .. figure:: figure/autoadd_m2cat.png
    :scale: 40%
    :align: center
    :name: autoadd_m2cat.png
    :target: ../_static/autoadd_m2cat.html

    The processing flow that m2cat is automatically added

The addition of m2tee, mfifo by flow branching
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Opposite to the automatic addition of ``m2cat`` , when an output of one flow is connected as inputs of multiple flows,
``m2tee`` and ``mfifo`` are automatically added.
``m2tee`` has a function of branching input stream into multiple streams,
``mfifo`` has a function of buffering to avoid dead lock(First In First Out buffer).
:numref:`autoadd_mtee` shows the process of calculating the composition ratio of ``amount`` by customer.
The point is the output of  ``mcut`` on the first line is connected to two methods ``msum`` (the second line) and ``mjoin`` (the third line).
Along with it, the data flow is branched by ``m2tee`` being inserted after ``mcut``.


  .. code-block:: python
    :linenos:
    :caption: Example of automatic addition of m2tee and mfifo
    :name: autoadd_mtee

    >>> f=nm.mcut(f="customer,amount",i=dat)
    >>> total=nm.msum(k="customer", f="amount:totalAmount",i=f)
    >>> f <<= nm.mjoin(k="customer", m=total, f="totalAmount")
    >>> f <<= nm.mcal(c='${amount}/${totalAmount}', a="share")
    >>> f.drawModelD3("autoadd_mtee.html")
    >>> f.run()
    [['A', '5200', '7200', '0.7222222222'], ['A', '2000', '7200', '0.2777777778'], ['B', '800', '8300', '0.09638554217'], ['B', '3500', '8300', '0.421686747'], ['B', '4000', '8300', '0.4819277108']]

  .. figure:: figure/autoadd_mtee.png
    :scale: 40%
    :align: center
    :name: autoadd_mtee.png
    :target: ../_static/autoadd_mtee.html

    The processing flow that m2tee, mfifo are automatically added
    

After branching, ``mfifo`` is added for each. What would happen if this buffer is not there?
``m2tee`` is simply copying one input to two outputs by a row, so if there is congestion at either output destination, it needs to wait.
Here, for simplicity, let's say it can process the next line only after it has output the input line to both.
This means if one of the methods does not come to receive the data, ``m2tee`` falls into the wait state.
On the other hand, ``mjoin`` after branching is merging the results of  ``msum`` , it becomes the wait state until the output of ``msum`` comes.
The other thing to keep in mind is that  ``mfifo`` , ``msum`` , ``mjoin`` are run in parallel when executed,
therefore, it is not decided which method is executed at what timing.

Considering these together, when  ``mtee`` gives the first row of a customer, ``mjoin`` stops to wait for the output from  ``msum`` .
On the other hand, ``msum`` can't pass the result to ``mjoin`` until it processes all the rows of the customer.
However, as ``mtee`` is stopping to wait for  ``mjoin``, ``msum`` loses the data supply from  ``mtee``.
Such a situation where the processing cannot proceed as a whole because each method waits for data from the other, which is called a deadlock. Practically, 
as ``m2tee`` has some range of buffer, deadlock does not occur instantly, however,
when the number of data per customer increases, the buffer of ``m2tee`` is filled and there is a possibility that a deadlock will occur.


``mfifo`` is added to avoid such a deadlock.
You can think ``mfifo`` has infinit buffer inside the method.
In fact, it has a constant large size memory and when it is filled, it changes to a file buffer.
By doing so, ``m2tee`` does not care about the process placed after branching, it simply copies into the infinite buffer,
which can prevent data congestion, and then deadlock is avoided as a result.

Actually, those logics which cause deadlocks are not detected, even the logic is not a problem, 
``mfifo`` is always added whenever the data is branched by ``mtee`` .
``mfifo`` itself is very fast unless its buffer is filled, as it makes the data flow from right to left inside the memory,
thus, even it is automatically added in such a redundant way, it is worth to do.

Other than the above branching examples, there is a branching using redirect. Same as the above examples, 
``m2tee`` and ``mfifo`` are automatically added in this case.
:numref:`autoadd_redirect` shows the example.
In this example, at first, by the method  ``mselstr`` , data are divided into customer  ``A`` and others,
from the records of customers other than A, select the records that  ``amount`` is equal or greater than 1000,
and after merging with the data of customer  ``A`` , it calculates the total of  ``amount`` .
The point of this example is that at the processing of ``mselstr``, data are divided into two branches that are the output matching the condition and the output unmatching the condition.
The ``u=`` stream is realized by the function ``redirect``.
However, the function ``redirect`` does not process anything by itself,
it only changes the connection of the stream, thus it is not displayed in the processing flow graph.
Same as the examples above, you can see that  ``m2tee`` and ``mfifo`` are automatically added after the branching.


  .. code-block:: python
    :linenos:
    :caption: The example of using redirect
    :name: autoadd_redirect

    >>> custA  =nm.mselstr(f="customer",v="A",i=dat)
    >>> custB  =custA.redirect("u")
    >>> custB <<=nm.mselnum(f="amount",c='[1000,]')
    >>> cat  =nm.m2cat(i=[custA,custB])
    >>> cat<<=nm.msum(k="customer",f="amount")
    >>> cat.run()
    >>> cat.drawModelD3("autoadd_redirect.html")
    [['A', '7200'], ['B', '7500']]

  .. figure:: figure/autoadd_redirect.png
    :scale: 40%
    :align: center
    :name: autoadd_redirect.png
    :target: ../_static/autoadd_redirect.html

    The processing flow with m2tee, mfifo automatically added by redirect

