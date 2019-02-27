
.. _実行:

run and runs
=======================
As explained in the chapter of " :doc:`flow` ", the method ``run`` or ``runs`` are used 
to execute processing flows that registered with a processing flow object.
Processing methods composing the processing flow are unfolded on threads [#f3]_ [#f4]_, and pipelines are built between methods.
Then given input data flows into pipelines, the processing method on each thread processes the flowing data.
Like this, all threads are executed by the MISD(Multiple Instruction Single Data) type of parallel processing.
A disadvantage of parallel processing of MISD type is that if there is a relatively slow processing method in the processing flow, it becomes a bottleneck.
However, the large scale processing introduced in the chapter "  :doc:`flow` " 
can be efficiently realized by combining with SIMD(Single Instruction Multiple Data) type parallel processing. 

run: Member method
-----------------------
``run`` constructs the processing flow after adding the processing method(s) that are automatically added before executes.
After that, each processing method is unfolded on threads and executed,
however, when the number of processing methods is large, not all of them are executed at the same time.
Because of the factors such as compression of memory, the increase of the working files, etc., that lower the processing speed and suppress the efficiency.
Moreover, there is also a limit on the number of open files available for one process (pipe is also a special type of file, it is counted as two open files with read/write).
Therefore, we have empirically set the limit on the number of threads that can be executed simultaneously.
The average memory usage of the processing method is about 47 MB, 
and the value obtained by dividing the actual memory size by 47 MB is assigned as the number of concurrent executable threads.
It does not check what other process are running, it is calculated only from the physical memory capacity.
For example, on the machine with 4GB memory, the upper limit of the number of concurrent executable threads becomes 86 (=4084/47).
It is possible to change this upper limit, and there are two ways.
One is by setting up the amount to the environment variable ``KG_RUN_LIMIT``,
the other is to give the  ``runlimit`` as the argument to ``run`` ( :numref:`run_limit` ).
When both are given at the same time,  the argument of ``run`` takes precedence.


  .. code-block:: python
    :linenos:
    :caption: The two methods to change the upper limit of the number of concurrent executable threads
    :name: run_limit

    >>> import os
    >>> import nysol.mcmd as nm
    >>> os.environ['KG_RUN_LIMIT'] = '500' # Setting by the environment variable
    >>> nm.mcut(f="a",i=dat).run(runlimit=500) # Setting by the argument of run
 
When the number of processing methods executed on a processing flow object exceeds the upper limit,
it cuts the flow at the "appropriate point" of the processing flow (disconnect the pipe connection),
and switch the output direction of the result of the disconnected point to the working file. 
The processing after the disconnected points will be executed after all the previous threads are processed
by reading the working file, the processing will be continued like this.
As an extreme example, if we set the argument as ``runlimit=1``, all methods are disconnected,
and all the methods are operated in a single thread, starting the processing methods closest to the input file,
these data transfers between the processing methods are realized by input to / output from working files.
As a result, file I/O occurs very often which makes the processing slow.

By the way, where is the "appropriate point" to disconnect the processing flow?
Processing flows of MCMD can be drawn by the DAG (Directed Acyclic Graph) (Please see the chapter " :doc:`flow` " for details).
So it generally decides the disconnected points by the following heuristic.
Beginning with input data, it circulate along with the directed line in the width priority,
and assigns numbers to the visited nodes.
When the number exceeds the upper limit, it disconnects methods with smaller numbers than that as one block.
By repeating this operation, it divides the entire processing flow into multiple blocks, and then they are executed in threads sequentially in parallel processing.
If you want to check the number of threads started during the execution, you can use the command ``top``.

There will be a way to detect the disconnect point to improve further the efficiency of processing other than the above method. 
However, there are many elements we need to consider such as processing efficiency of algorithm of each method, 
whether any working files are used or not, penalty for disconnect after the flow branching, etc. 
It is a future task to detect the optimum disconnect point considering these elements.

Thread stack size
''''''''''''''''''''''''
Processing methods are executed in threads, however each thread has the upper limit of stack size,
therefore memory errors can occur due to this limitation.
Processing methods are written in C++, the auto variables of local functions get allocated on the stack in C++.
The reason is that the stack is faster than the static area and the heap area.
The heap is used for the processing requires the large memory within the processing methods such as the data buffer and sorting buffer,
but for example, the string list specified by the  ``v=``  of  ``mselstr`` uses the stack.
If you specify like ``v=a1,a2,a3,...,a1000000``  [#f1]_ , it will run out of the stack area of the thread immediately.

The upper limit of the stack size per thread is 1048576( :math:`2^{20}` ) bytes.
This value can be changed by setting the environment variable  ``KG_THREAD_STK`` ( :numref:`run_stack` ).
However, it will be an error unless you specify the number which is equal or more than 16384 and multiples of 16 [#f2]_ .

  .. code-block:: python
    :linenos:
    :caption: Change the stack size of a thread
    :name: run_stack

    >>> import os
    >>> os.environ['KG_THREAD_STK'] = '2097152'
 
runs: class method
------------------------
While ``run``  method introduced above is a member method of the processing flow object that is called when output is only one,
``runs`` is used to execute processing flows that have multiple outputs (Please refer to " :doc:`flow` " for details).
In precise, when DAG has multiple sync nodes,  ``runs`` is used.
There is no problem to execute the flow by  ``runs`` which can be executed by ``run``.
However, on the contrary, if you execute the flow with multiple outputs by multiple  ``run`` methods, even the result is same, processing efficiency differs.
Basically, what ``run``  does is almost same as  ``run``  does,
however, ``runs`` integrates the specified multiple processing flow objects and reconstructs DAG, that is the difference.
Therefore, if you execute by using multiple ``run`` , the flows which can be shared when they are integrated are executed separately and duplicately, thus the efficiency decreases. 


Return value
------------------------
The return value of ``run`` is the file name if ``o=file name`` is specified at the final output.
When ``o=`` is omitted or  ``o=list`` is specified, the result is returned by a list.
``runs`` have multiple final outputs, it returns the result by a list with the same rule as  ``run``.
:numref:`run_ret` shows examples.

  .. code-block:: python
    :linenos:
    :caption: Examples of specifying o= and return values
    :name: run_ret

    dat1=[
    ["key","val"],
    ["a",1],
    ["a",2],
    ["b",3],
    ["b",4],
    ]

    # When a file name is specified by o=, it returns the file name.
    ret=nm.mcut(f="key,val",i=dat1,o="out1.csv").run()
    print(ret)
    # out1.csv

    # When a list is specified by o=, it returns result data as a list.
    out1=[]
    ret=nm.mcut(f="key,val",i=dat1,o=out1).run()
    print(ret)
    # [['a', '1'], ['a', '2'], ['b', '3'], ['b', '4']]

    # When o= is omitted, it returns the result as a Python list
    ret=nm.mcut(f="key,val",i=dat1).run()
    print(ret)
    # [['a', '1'], ['a', '2'], ['b', '3'], ['b', '4']]

    # When executed with runs, it returns a list of output file names
    fa=None
    fb=None
    fa <<= nm.mselstr(f="key",v="a",i=dat1)
    fb <<= fa.redirect("u")
    fa <<= nm.msum(k="key",f="val",o="out1.csv")
    fb <<= nm.msum(k="key",f="val",o="out2.csv")
    ret=nm.runs([fa,fb])
    print(ret)
    # ['out1.csv', 'out2.csv']

    # When a list output and a file output are mixed in runs
    out1=[]
    fa=None
    fb=None
    fa <<= nm.mselstr(f="key",v="a",i=dat1)
    fb <<= fa.redirect("u")
    fa <<= nm.msum(k="key",f="val",o=out1)
    fb <<= nm.msum(k="key",f="val",o="out2.csv")
    ret=nm.runs([fa,fb])
    print(ret)
    # [[['a', '3']], 'out2.csv']

Message Control
------------------------
As a common parameter to ``run`` and ``runs``, you can specify ``msg=`` that can control whether or not to output messages.
If you specify ``msg="on"``, END messages are displayed when each method on the processing flow ends.

  .. code-block:: python
    :linenos:
    :caption: Setting of MCMD import and input data
    :name: run_msg

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]
    nm.mcut(f="customer,amount",i=dat).run(msg="on")
    #END# kgload -nfn; IN=0 OUT=6; 2018/09/10 08:56:55; 2018/09/10 08:56:55
    #END# kgcut f=customer,amount; IN=5 OUT=5; 2018/09/10 08:56:55; 2018/09/10 08:56:55
    #END# kgload; IN=0 OUT=0; 2018/09/10 08:56:55; 2018/09/10 08:56:55
    nm.mcut(f="customer,amount",i=dat).run(msg="off")
    # When you give other string than "on" or omit it, END message will not be displayed.

Furthermore, by setting the environment variable  ``KG_VerboseLevel``, you can control messages more finely.
The setting values and their descriptions are shown in  :numref:`run_setverbose` below.
When ``msg="on"`` is not specified, messages are shown according to the setting of ``KG_VerboseLevel=2``.
It means only error and warning messages are displayed.
This value can not be changed.
What you can change is behavior when you specify  ``msg="on"``,
and messages are displayed according to the environment variable  ``KG_VerboseLevel``.

===== ========================================================
Value Description
===== ========================================================
0  	  Do not output any messages
1  	  \+ error message
2  	  \+ warning message output (other than msg="on")
3  	  \+ end message output
4  	  \+ msg message output (default of msg="on")
===== ========================================================
 
  .. code-block:: python
    :linenos:
    :caption: Example of changing the message display level
    :name: run_setverbose

    import os
    os.environ['KG_VerboseLevel'] = '0' # when run(msg="on") is specified, it does not display any messages
 
.. rubric:: Footnotes

.. [#f3] It uses |pthread| internally.
.. [#f4] ``cmd`` and ``runfunc`` ( :doc:`special` ) are started as a process by using fork in threads.
.. [#f1] For such a processing, you can store the multiple strings of conditions in a Python list or CSV, and use ``mcommon``.
.. [#f2] When this constraint is violated, it is automatically adjusted on some OS, but if it is on mac, it stops with ``stack size change error``.

  .. |pthread| raw:: html

    <a href="https://en.wikipedia.org/wiki/POSIX_Threads" target="_blank">POSIX thread</a>

