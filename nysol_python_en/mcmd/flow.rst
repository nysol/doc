
.. index::
   single: processing flow

.. _processing flow:

Processing flow
=======================

MCMD enables you to build complicated data processing flows by combining more than 80 different processing methods 
where each method is specialized for a single function, and those are processed in parallel.
Such an entire flow is called a **data processing flow** or simply called  **processing flow**.
And the object that handles processing flow is called a **data processing flow object**  or simply called **processing flow object** .
The processing flow is indicated by Directed Acyclic Graph( |DAG| ).
The DAG node corresponds to the processing method, and the directed link corresponds to the data flow.
Each of the graph in :numref:`flow_dag.png` is a processing flow indicated by DAG.
(a) and (b) are processing flows having a relatively simple structure, but a complicated processing flow such as shown in(c) can also be realized.
In the processing flow, a node without any input is called a source node, a node without any output is called a sink node.
In :numref:`flow_dag.png`, the source nodes are expressed by a red frame, and sink nodes are expressed by a  blue frames.
The input data has to be specified at the source node, and the output data has to be specified at the sink node
(As described later, the specification of output data can be omitted).
Also, according to the number of sink nodes, execution method of processing flow differs,
processing flow with only one sink node is executed by a member method ``run`` , when it has multiple sink nodes, it is executed by a class method ``runs`` .
Please refer to the chapter "  :doc:`run` " for details for each method.

  .. figure:: figure/flow_dag.png
    :scale: 40%
    :align: center
    :name: flow_dag.png
    
    The processing flows indicated by DAG(Directed Acyclic Graph)


In the following, we start with a simple example and explain how MCMD constructs data processing flows.

  .. |dag| raw:: html

    <a href="https://en.wikipedia.org/wiki/Directed_acyclic_graph" target="_blank">DAG</a>

.. _処理フロー_基本例: A simple example of processing flow

Implicit connection
----------------------
Let's begin with a simple data processing flow.
:numref:`flow_base` is the processing flow described in  :numref:`hello_ope` of the chapter " :doc:`Get started<hello>` ".
It uses the two-dimensional list containing three columns and five rows data as input data,
cut out only the columns of  ``customer`` and ``amount`` by the method ``mcut`` and then calculate the total value of ``amount``.

  .. code-block:: python
    :linenos:
    :caption: Simple example of processing flow
    :name: flow_base

    >>> import nysol.mcmd as nm
    >>> dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]
    >>> f=None
    >>> f <<= nm.mcut(f="customer,amount",i=dat)
    >>> f <<= nm.msum(k="customer",f="amount")
    >>> f.run()
    [['A', '7200'], ['B', '8300']]

.. index::
   single: Implicit connection

By the operator ``<<=`` , a processing method on the right side is additionally registered with the processing flow object on the left side.
When the left side is  ``None`` , a new process flow object is created and the processing method on the right hand side is registered.
Registration order is important, because when you don't specify a connection relationship (explained later), the output data of the previous method is connected as the input data of the next method.
Such a connection method is called an **Implicit connection**.
In :numref:`flow_base` , output data of ``mcut`` is implicitly connected as input data of  ``msum``.

Then, to execute the process flow created, you just need to call  ``run`` which is a member method of processing flow object ``f`` like  ``f.run()`` 

Also, if you use the method ``drawModelD3`` , you can visualize the whole processing flow( :numref:`flow_drawModel` ).
As the results shown in :numref:`flow_drawModelPNG` , the connection relationship of methods is drawn by a graph.
Methods are represented by circle nodes, and data is by square nodes.
Here, a method name with a light color indicates the processing that MCMD automatically added behind at the execution, you can ignore it here.
Please refer to the chapter " :doc:`autoadd` " for details regarding the automatic addition of processing.


  .. code-block:: python
    :linenos:
    :caption: Visualization of processing flow
    :name: flow_drawModel

    nm.drawModelsD3([f],"cust_amount.html") 

  .. figure:: figure/flowChart.png
    :scale: 40%
    :align: center
    :name: flow_drawModelPNG
    :target: ../_static/cust_amount.html

    Visualized processing flow

.. _データストリームの明示的接続方法: Explicit connection method of data stream

Explicit connection
---------------------------------
There are some ways to explicitly connect the data flow to a processing flow object.
Many processing methods provided by MCMD have common parameters for input and output.
``i=`` and ``m=`` are parameters that specify input data, and 
``o=`` and ``u=`` are parameters that specify output data.
The connection of the data stream can be realized by specifying a processing flow object as the input parameter.
Let's look at some examples.

Example of combining columns
''''''''''''''''''''''''''''''''''
:numref:`flow_share` is a process to calculate the total amount by customer( ``A`` and ``B`` ), and obtain each composition ratio. 
It specifies the flow object  ``f`` in the first row as the input data ( ``i=f`` ) of ``msum``  in the second row,
and it sets the processing content as another processing flow object ``total`` .
By specifying the object ``total`` as reference data for  ``mproduct`` in the fourth line( ``m=total`` ),
the total amount field ``totalAmount`` is combined. 
The input data for ``msum`` of the 3rd line, as it is added to the same flow object ``f``,
the output data of  ``mcut`` in the 1st line is connected as it is. 
The relationship of those connections is visualized in :numref:`flow_share.png` .
Again, there are methods :doc:`Auto Added<autoadd>`, but you can ignore them.


  .. code-block:: python
    :linenos:
    :caption: Calculation of composition ratio by customer: Data stream connection by combining columns
    :name: flow_share

    >>> f=None
    >>> f<<= nm.mcut(f="customer,amount",i=dat)
    >>> total=nm.msum(f="amount:totalAmount",i=f)
    >>> f <<= nm.msum(k="customer", f="amount")
    >>> f <<= nm.mproduct(m=total, f="totalAmount")
    >>> f <<= nm.mcal(c='${amount}/${totalAmount}', a="share")
    >>> f.drawModelD3("flow_share.html")
    >>> f.run()
    [['A', '7200', '15500', '0.464516129'], ['B', '8300', '15500', '0.535483871']]

  .. figure:: figure/flow_share.png
    :scale: 40%
    :align: center
    :name: flow_share.png
    :target: ../_static/flow_share.html

    Processing flow of combining columns

In this example, most of the connections of the processing flow object  ``f`` are implicit connections.
You can also change those to explicit connections by changing the names of objects.
:numref:`flow_explicit` shows how to do it.
The flow figure is the same as  :numref:`flow_share.png` .
It is different from :numref:`flow_share` , you can understand that connections are specified explicitly by setting ``i=`` for each method.
By the way, the object to be executed by `` run`` is the last processing method registered as the sink node.
In :numref:`flow_explicit` , if you replace  ``f4.run()`` with  ``f3.run()`` , of course, it outputs the result of ``mprodcut``.


  .. code-block:: python
    :linenos:
    :caption: Calculation of composition ratio by customer: Data stream connection by combining columns
    :name: flow_explicit

    >>> f1 = nm.mcut(f="customer,amount", i=dat)
    >>> total=nm.msum(f="amount:totalAmount", i=f1)
    >>> f2 = nm.msum(k="customer", f="amount", i=f1)
    >>> f3 = nm.mproduct(m=total, f="totalAmount", i=f2)
    >>> f4 = nm.mcal(c='${amount}/${totalAmount}', a="share", i=f3)
    >>> f4.run()
    [['A', '7200', '15500', '0.464516129'], ['B', '8300', '15500', '0.535483871']]

Example of record consolidation
'''''''''''''''''''''''''''''''''''''''''''
Divide data into groups by type, and do some processing on one and do different processing on the other, then both are merged, such a processing is often used.
:numref:`flow_merge` is the flow describing such a process.
Using ``msestr`` twice, it divides data into customer  ``A`` and customer ``B`` , then only for ``B`` , select data which amount is equal or greater than 1000,
then merge two divided data by specifying ``i=`` parameter of  ``msum`` method.
The specification of the input parameter of  ``i=`` is like  ``[custA,custB]``, it needs to be a list of processing flow objects.


  .. code-block:: python
    :linenos:
    :caption: Example of merging calculated results by customer
    :name: flow_merge

    >>> f1=None
    >>> f1 <<= nm.mcut(f="customer,amount",i=dat)
    >>> custA   = nm.mselstr(f="customer",v="A",i=f1)
    >>> custB   = nm.mselstr(f="customer",v="B",i=f1)
    >>> custB <<= nm.mselnum(f="amount",c="[1000,]")
    >>> f2=None
    >>> f2 <<= nm.msum(k="customer", f="amount", i=[custA,custB])
    >>> f2.drawModelD3("flow_merge.html")
    >>> f2.run()
    [['A', '7200'], ['B', '7500']]

  .. figure:: figure/flow_merge.png
    :scale: 40%
    :align: center
    :name: flow_merge.png
    :target: ../_static/flow_merge.html

    Process flow of record consolidation


.. index::
   single: redirect

redirect
----------------------------
In :numref:`flow_merge` , it reads ``f1``  twice as ``mselstr`` is used twice, which is not efficient.
While ``mselstr`` can specify the output destination for rows matching the conditions using  ``o=``,
it can also output the unmatched rows by using ``u=``.
By using such a function,  the same processing can be done by only one execution of ``mselstr``.
The output data of ``o=`` can be the input data for the next method which will be registered, however, how can we connect ``u=`` to the next method?
The method that can realize it is  ``redirect``.
:numref:`flow_redirect` is a rewrite of :numref:`flow_merge` using ``redirect``.
The only difference is on the 4th line, by ``custA.redirect("u")`` , it connects  ``u=`` parameter of the last method (``mselstr``) registered with  ``custA`` 
to the processing flow object ``custB``.
As you can see in :numref:`flow_redirect.png` , ``mselstr`` is executed only once, which is more efficient than  :numref:`flow_merge` .

  .. code-block:: python
    :linenos:
    :caption: Example using redirect
    :name: flow_redirect

    >>> f1=None
    >>> f1 <<= nm.mcut(f="customer,amount",i=dat)
    >>> custA  = nm.mselstr(f="customer",v="A",i=f1)
    >>> custB  = custA.redirect("u")
    >>> custB <<= nm.mselnum(f="amount",c="[1000,]")
    >>> f2=None
    >>> f2 <<= nm.msum(k="customer", f="amount", i=[custA,custB])
    >>> f2.drawModelD3("flow_redirect.html")
    >>> f2.run()
    [['A', '7200'], ['B', '7500']]

  .. figure:: figure/flow_redirect.png
    :scale: 40%
    :align: center
    :name: flow_redirect.png
    :target: ../_static/flow_redirect.html

    Example using redirect

runs: Execution of flow with multiple outputs
----------------------------------------------------
All examples of processing flow we have used so far had only one final output like (a),(b) of  :numref:`flow_dag.png` .
Here, we explain about processing flow which has multiple outputs.
:numref:`flow_multio` shows an example of such a flow.
In this example, it branches to the rows where ``customer`` field is ``A`` and the rows of others,
then aggregates the ``amount`` field for each.
For branching, we use the ``redirect`` method described above. 
First of all, to execute those cases that have multiple final outputs, use the class method ``runs`` and give the list of objects including the final outputs as a parameter  (in the example,  ``nm.runs([fa,fb])`` ).
``runs`` integrates all the processing flows given by the parameter, then identify the entire structure and executes.
Then, unfolds process methods registered with the whole processing flow on threads and executes by parallel processing.
However, there are limitations such as the upper limit for a number of threads open at the same time, please refer to "  :doc:`run` " for details.

The return value of `` runs`` is a list of output CSV file names.
Also, it can output not only to a CSV file but also to a list such as ``o = list``.


 .. code-block:: python
    :linenos:
    :caption: Execution example by `` runs`` of processing flows with multiple outputs
    :name: flow_multio

    >>> fa=None
    >>> fb=None
    >>> fa <<= nm.mcut(f="customer,amount",i=dat)
    >>> fa <<= nm.mselstr(f="customer",v="A")
    >>> fb <<= fa.redirect("u")

    >>> fa <<= nm.msum(k="customer",f="amount",o="out1.csv")
    >>> fb <<= nm.msum(k="customer",f="amount",o="out2.csv")
                  
    >>> nm.runs([fa,fb],msg="on")
    #END# kgload -nfn; IN=0 OUT=5; 2018/09/09 15:22:45; 2018/09/09 15:22:45
    #END# kgselstr f=key v=a; IN=4 OUT=2; 2018/09/09 15:22:45; 2018/09/09 15:22:45
    #END# kgfifo; ; 2018/09/09 15:22:45; 2018/09/09 15:22:45
    #END# kgfifo; ; 2018/09/09 15:22:45; 2018/09/09 15:22:45
    #END# kgsum f=val k=key o=xxa; IN=2 OUT=1; 2018/09/09 15:22:45; 2018/09/09 15:22:45
    #END# kgsum f=val k=key o=xxb; IN=2 OUT=1; 2018/09/09 15:22:45; 2018/09/09 15:22:45
    # content of out1.csv
    # key%0,val
    # a,3
    # Content of out2.csv
    # key%0,val
    # b,7

It is possible to realize the same process with ``run`` .
That code is as shown in :numref:`flow_multio2` .
The only difference is the last two lines, those  ``run`` each processing flow object with two final outputs. 
As a matter of course, output results are the same, however, the difference is as you can tell from the processing messages,
the method ``mcut`` and ``mselstr`` which are the common processes among ``fa`` ``fb`` , are executed twice.
It is because ``runs`` integrates the processing flow of both ``fa`` and ``fb`` and executes the processing,
on the other hand, ``run`` executes each path on the DAG from input to output for each ``fa`` ``fb`` ,
the common processing methods are also executed redundantly.

 .. code-block:: python
    :linenos:
    :caption: Execute the processing flow with multiple outputs by ``run`` 
    :name: flow_multio2

    >>> fa=None
    >>> fb=None
    >>> fa <<= nm.mcut(f="customer,amount",i=dat)
    >>> fa <<= nm.mselstr(f="customer",v="A")
    >>> fb <<= fa.redirect("u")

    >>> fa <<= nm.msum(k="customer",f="amount",o="out1.csv")
    >>> fb <<= nm.msum(k="customer",f="amount",o="out2.csv")

    >>> fa.run(msg="on")
    #END# kgload -nfn; IN=0 OUT=6; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    #END# kgselstr f=customer v=A; IN=5 OUT=2; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    #END# kgsum f=amount k=customer; IN=2 OUT=1; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    #END# kgload; IN=0 OUT=0; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    [['A', '20180105', '7200']]
    >>> fb.run(msg="on")
    #END# kgload -nfn; IN=0 OUT=6; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    #END# kgselstr f=customer v=A; IN=5 OUT=3; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    #END# kgfifo; ; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    #END# kgload; IN=0 OUT=0; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    #END# kgsum f=amount k=customer; IN=3 OUT=1; 2018/09/10 06:10:20; 2018/09/10 06:10:20
    [['B', '20180107', '8300']]

Application to parallel processing
------------------------------------
By using ``runs``, also SIMD (Single Instruction Multiple Data) type parallel processing can be realized.
It is that you prepare a large number of the same type of data beforehand and execute the same processing in parallel on those data.
A simple example is shown by  :numref:`flow_meach` .
Here, it stores two data sets  ``dat1`` and ``dat2`` into the array  ``dat``,
and then it processes of summing up these data sets in parallel.
Data may not be given in a list but may be a plurality of pre-divided CSV files.
It is also possible to prepare and execute hundreds of thousands of files.
In the example, it registers the processing flow which consisted only with  ``msum`` with  ``runlist`` ,
then executes these processing flows by ``nm.runs(runlist)`` at the end.
``runs`` analyzes all registered processing flows,
and recognizes processing flows that are not connected with other processing flows as islands.
Then it places those islands in threads and execute them.
Since it is executed on the premise that processing flows are independent and they do not interfere with each other,
for example, when the final file names of a plurality of processing flows are the same
(That is, the islands interfere with each other), a correct result can not be obtained.


 .. code-block:: python
    :linenos:
    :caption: Example using redirect
    :name: flow_meach

    import nysol.mcmd as nm
    dat1=[
    ["key","val"],
    ["a",1],
    ["a",2],
    ]

    dat2=[
    ["key","val"],
    ["b",3],
    ["b",4],
    ]
    dat=[dat1,dat2]

    runlist=[]
    for i in range(len(dat)):
      f=nm.msum(f="val",o="out%d.csv"%i)
      runlist.append(f)
    nm.runs(runlist)
    # contennt of out0.csv
    # key,val
    # a,3
    # Content of out1.csv
    # key,val
    # b,7
    

The case where o= is used for a processing method placed in the middle
----------------------------------------------------------------------------------
The case in which even processing flow with multiple outputs does not branch, and ``o=CSV file name`` is specified for the processing method in the middle of the processing flow,
That processing flow can be executed by  ``run``  since the process method is not the sink node.
An easy to understand example is shown in  :numref:`flow_oooo` .
It is meaningless as a whole, it is only adding items one by one with four ``msetstr`` .
Except the last  ``msetstr`` , output file names are specified with  ``o=`` ,
data in progress at each point is output to each file.
The last ``msetstr`` will output a list because ``o=`` is not specified.

 .. code-block:: python
    :linenos:
    :caption: Example using ``o=file name`` for the process method in the middle of the processing flow
    :name: flow_oooo

    >>> f=None
    >>> f <<= nm.msetstr(v="out1",a="out1",i=dat,o="out1.csv")
    >>> f <<= nm.msetstr(v="out2",a="out2",o="out2.csv")
    >>> f <<= nm.msetstr(v="out3",a="out3",o="out3.csv")
    >>> f <<= nm.msetstr(v="out4",a="out4")
    >>> f.run() 
    [['A', '20180101', '5200', 'out1', 'out2', 'out3', 'out4'], ['B', '20180101', '800', 'out1', 'out2', 'out3', 'out4'], ['B', '20180112', '3500', 'out1', 'out2', 'out3', 'out4'], ['A', '20180105', '2000', 'out1', 'out2', 'out3', 'out4'], ['B', '20180107', '4000', 'out1', 'out2', 'out3', 'out4']]
    # Content of out1.csv
    # customer,date,amount,out1
    # A,20180101,5200,out1
    # B,20180101,800,out1
    # B,20180112,3500,out1
    # A,20180105,2000,out1
    # B,20180107,4000,out1
    # Content of out2.csv
    # customer,date,amount,out1,out2
    # A,20180101,5200,out1,out2
    # B,20180101,800,out1,out2
    # B,20180112,3500,out1,out2
    # A,20180105,2000,out1,out2
    # B,20180107,4000,out1,out2
    # Content of out3.csv
    # customer,date,amount,out1,out2,out3
    # A,20180101,5200,out1,out2,out3
    # B,20180101,800,out1,out2,out3
    # B,20180112,3500,out1,out2,out3
    # A,20180105,2000,out1,out2,out3
    # B,20180107,4000,out1,out2,out3


This is the same even if you specify a list in ``o =`` . :numref:`flow_oooo2` shows the rewrite code by ``o=list`` of the same process of :numref:`flow_oooo` .

 .. code-block:: python
    :linenos:
    :caption: Example of using o=list for processing methods in the middle of the process
    :name: flow_oooo2

    >>> out1=[]
    >>> out2=[]
    >>> out3=[]
    >>> out4=[]
    >>> f=None
    >>> f <<= nm.msetstr(v="out1",a="out1",i=dat,o=out1)
    >>> f <<= nm.msetstr(v="out2",a="out2",o=out2)
    >>> f <<= nm.msetstr(v="out3",a="out3",o=out3)
    >>> f <<= nm.msetstr(v="out4",a="out4")
    >>> out4=f.run()
    >>> print(out1)
    [['A', '20180101', '5200', 'out1'], ['B', '20180101', '800', 'out1'], ['B', '20180112', '3500', 'out1'], ['A', '20180105', '2000', 'out1'], ['B', '20180107', '4000', 'out1']]
    >>> print(out2)
    [['A', '20180101', '5200', 'out1', 'out2'], ['B', '20180101', '800', 'out1', 'out2'], ['B', '20180112', '3500', 'out1', 'out2'], ['A', '20180105', '2000', 'out1', 'out2'], ['B', '20180107', '4000', 'out1', 'out2']]
    >>> print(out3)
    [['A', '20180101', '5200', 'out1', 'out2', 'out3'], ['B', '20180101', '800', 'out1', 'out2', 'out3'], ['B', '20180112', '3500', 'out1', 'out2', 'out3'], ['A', '20180105', '2000', 'out1', 'out2', 'out3'], ['B', '20180107', '4000', 'out1', 'out2', 'out3']]
    >>> print(out4)
    [['A', '20180101', '5200', 'out1', 'out2', 'out3', 'out4'], ['B', '20180101', '800', 'out1', 'out2', 'out3', 'out4'], ['B', '20180112', '3500', 'out1', 'out2', 'out3', 'out4'], ['A', '20180105', '2000', 'out1', 'out2', 'out3', 'out4'], ['B', '20180107', '4000', 'out1', 'out2', 'out3', 'out4']]


Specifying ``o=`` in the middle of the processing flow is very effective for debugging of the processing flow.
When the final result becomes something disagreeable, being able to check the course of progress will be of great help to find out where the problem is.

