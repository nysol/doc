
Special processing methods
===============================

What each method of MCMD does is to execute some "processing" 
for data received as a byte stream and outputs the result as a byte stream.
If so, it is not strange that those "processing" can be executed by Python functions or OS commands.
The methods supporting such functions are ``runfunc`` and ``cmd`` that are explained below.

runfunc: Execution of a function
--------------------------------------
``runfunc`` is a method for making Python functions behave as if MCMD methods.
The basic usage is described in  :numref:`special_runfunc1`.
The point is to use the methods ``mstdin`` and ``mstdout`` that are used in the function ``bigAmount``,
each method has a function of reading standard input and writing to standard output, respectively.
Like this example, if the function has the function of reading standard input as input data and writing the standard output as output data,
by using the function ``runfunc``, it can be handled in the same way as MCMD processing methods.
In :numref:`special_runfunc1`, by ``runfunc`` , the output of  ``mcut`` is connected to the standard input of the function of ``bigAmount``,
and also the standard output of the bigAmount function is connected to ``msum``.


  .. code-block:: python
    :linenos:
    :caption: Basic usage of the runfunc method
    :name: special_runfunc1

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]   

    def bigAmount(lowerBound):
      f = None
      f <<= nm.mstdin()
      f <<= nm.mselnum(f="amount",c="[lowerBound,]")
      f <<= nm.mstdout()
      f.run()

    sel=None
    sel <<= nm.mcut(f="customer,amount",i=dat)
    sel <<= nm.runfunc(bigAmount,lowerBound=4000)
    sel <<= nm.msum(k="customer",f="amount")
    print(sel.run())
    # [['A', '7200'], ['B', '8300']]

Implement the function without using MCMD
''''''''''''''''''''''''''''''''''''''''''''''''''
In :numref:`special_runfunc1`, although the example implemented using the MCMD processsing method  ``mstdin`` ``mstdout``,
there is no problem even if you use the general library with standard input/output that are available in Python.
:numref:`special_runfunc2` is :numref:`special_runfunc1` with a rewrite of ``bigAmount`` function.
In that program, ``stdin`` of the sys library is used as the standard input , and print is used to write to standard output.
Because all of them are native code of Python, the degree of freedom is very high.
However, in such a case, please note that you need to write the parsing logic of CSV data yourself.
When the CSV is simple, there is no problem, but it is quite troublesome when you need to handle strings with double quotations and commas.


  .. code-block:: python
    :linenos:
    :caption: Implementation without using MCMD
    :name: special_runfunc2

    import sys
    def bigAmount2(lowerBound):
      header = True
      for line in sys.stdin:
        if header:
          print(line.strip())
          header = False
        else:
          tokens = line.strip().split(",")
          if int(tokens[1])>=lowerBound:
            print(",".join(tokens))

Implementation using MCMD iterator
''''''''''''''''''''''''''''''''''''''''''''''
Lastly, as a writing method lies between :numref:`special_runfunc1` and :numref:`special_runfunc2` ,
as :numref:`special_runfunc3` shows, we introduce how to write the Python logic that leaves parsing CSV to the MCMD method ``mstdin`` and uses MCMD iteration afterward.
The point is that since MCMD iterator ignores column header, we don't need to think about the header row in the ``for`` statement,
while it needs to output the column header to output to the next method.
The code below outputs the column header at the beginning.

  .. code-block:: python
    :linenos:
    :caption: The Example combining mstdin and iteration
    :name: special_runfunc3

    def bigAmount(lowerBound):
      print("customer,amount")
      for line in nm.mstdin():
        if int(line[1])>=lowerBound:
          print(",".join(line))

If you want to retrieve column names from the data, you can connect to the iterator ``getline`` after ``mstdin``
and specify the option to output the column header by  ``header=True`` there.
The treatment of the column header is the same as  :numref:`special_runfunc2` .

  .. code-block:: python
    :linenos:
    :caption: How to get field names from data in iteration
    :name: special_runfunc4

    def bigAmount(lowerBound):
      header = True   
      for line in nm.mstdin().getline(header=True):
        if header:      
          print(",".join(line))
          header = False  
        else:
          if int(line[1])>=lowerBound:
            print(",".join(line))

Debug of runfunc
''''''''''''''''''
The method ``runfunc()`` only executes the specified function by leaving it to Python,
even some error occurs inside the function, it only detects the fact the error occurred and it does not sense its detail.
For example,  :numref:`special_debug1` contains the code of  :numref:`special_runfunc3` described above with the additional syntax error,
and the error messages output at run time are as shown in  :numref:`special_debug2`.
Like this, we can know that error occurs in "runfunc" but we cannot find out more than that.


  .. code-block:: python
    :linenos:
    :caption: Example of putting an error in a function (debug1.py) 
    :name: special_debug1

    import sys
    import nysol.mcmd as nm

    def bigAmount(lowerBound):
      print("customer,amount")
      for line in nm.mstdin():
        if int(line)>=lowerBound: # Error of not specifying an element of line
          print(",".join(line))

    sel=None
    sel <<= nm.mcut(f="customer,amount",i=dat)
    sel <<= nm.runfunc(bigAmount,lowerBound=4000)
    sel <<= nm.msum(k="customer",f="amount")
    print(f.run(msg="on"))

  .. code-block:: bash
    :linenos:
    :caption: The result of :numref:`special_debug1` execution
    :name: special_debug2

    $ python debug1.py
    #END# kgload; IN=0 OUT=5; 2018/09/05 10:18:51; 2018/09/05 10:18:51
    #END# kgcut f=customer,amount; IN=5 OUT=5; 2018/09/05 10:18:51; 2018/09/05 10:18:51
    #ERROR# error occured in the function, check the detail error message using try-exception in the function. (kgpyfunc); kgpyfunc; ; 2018/09/05 10:18:51; 2018/09/05 10:18:51
    #ERROR# ; kgshell (script RUN KGERROR runmain on kgshell); 2018/09/05 10:18:51
    RuntimeError: runmain on kgshell
    []

How can we track details of the error that occurs inside of the function? That can be resolved by inserting of ``try`` 〜 ``exception``.
The code is shown in  :numref:`special_debug3` .
Although it calls the traceback function in the ``exception`` , you need to set the output destination to the standard error output, that is the point.
Since standard input / output are treated as data by ``runfunc`` method.
Also, when you want to display the contents of the variables for debugging, you also need to output not to the standard output but to the error output.
The code below outputs the argument ``lowerBound`` to the standard error output by using the method ``sys.stderr``.

The messages at run time are as shown in  :numref:`special_debug4` ,
these show us there is a problem in the seventh line, and also the contents of ``lowerBound`` at the beginning.


  .. code-block:: python
    :linenos:
    :caption: Example of implementation of the function that enables error tracking (debug2.py)
    :name: special_debug3

    def bigAmount(lowerBound):
      try:
        sys.stderr.write(str(lowerBound)+"\n")
        print("customer,amount")
        for line in nm.mstdin():
          if int(line)>=lowerBound:
            print(",".join(line))
      except Exception as e:
        with open('/dev/stderr', 'w') as fpe:
          traceback.print_exc(file=fpe)

  .. code-block:: bash
    :linenos:
    :caption: Execution result of  :numref:`special_debug3`
    :name: special_debug4

    $ python debug2.py
    4000
    #END# kgcut f=customer,amount; IN=5 OUT=5; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    #END# kgload; IN=0 OUT=5; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    Traceback (most recent call last):
    File "special_runfunc.py", line 7, in bigAmountBug
    if int(line)>=lowerBound:
    TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
    #END# kgpyfunc; ; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    #END# kgsum f=amount k=customer; IN=0 OUT=0; 2018/09/05 10:32:47; 2018/09/05 10:32:47
    #END# kgload; IN=0 OUT=0; 2018/09/05 10:32:47; 2018/09/05 10:32:47

runfunc is in test operation
'''''''''''''''''''''''''''''''''''''
The method runfunc is so powerful that it can turn the processing functions frequently used by individuals and corporations into methods,
therefore it can promote the modularization of programs.
However, on the other hand, it is also possible to execute runfunc from runfunc.
Even when such a nesting is deep, it tries hard to process internally,
however, we haven't been able to fully operate and verify it yet.
As for now, please consider this method as a test operation.


cmd: Execution of commands
-------------------------------------
While ``runfunc`` realizes the processing by Python function, ``cmd`` method realizes by OS commands.
Many UNIX-like operating systems receives data from standard input, and carries out some process inside the command, and write to the standard output.
Basic usage is shown in  :numref:`special_cmd1` .
Here, after selecting the columns ``customer`` and ``amount``, it connects to the command ``tr`` (Not a very meaningful example).
``tr`` command replaces specific characters in an input byte stream by a character basis.
The example below replaces the character ``A`` with ``C``.
As a result, total is calculated on the data where customer ``A`` has been replaced with ``C``.
However, note that column names, data bodies, moreover, comma-separated items are just passed into the ``cmd`` method as a data stream without distinction.
For example, in the example below, if column names include ``A`` , which will be replaced with  ``C``, so it won't process as intended.
If it is only the matter of the column header, as shown in  :numref:`special_cmd2` , suppress the column header by the previous method ``mcut`` ( ``nfno=True`` ),
then, after the execution of the command, add the column header row by the method  ``mcut`` .


  .. code-block:: python
    :linenos:
    :caption: Import of mcmd and setting of input data
    :name: special_cmd1

    import nysol.mcmd as nm
    dat=[
    ["customer","date","amount"],
    ["A","20180101",5200],
    ["B","20180101",800],
    ["B","20180112",3500],
    ["A","20180105",2000],
    ["B","20180107",4000]
    ]

    f=None
    f <<= nm.mcut(f="customer,amount",i=dat)
    f <<= nm.cmd("tr 'A' 'C'")
    f <<= nm.msum(k="customer",f="amount")
    print(f.run())
    # [['B', '8300'], ['C', '7200']]


  .. code-block:: python
    :linenos:
    :caption: Example of skipping the column header
    :name: special_cmd2

    f=None
    f <<= nm.mcut(f="customer,amount",nfno=True,i=dat)
    f <<= nm.cmd("tr 'A' 'C'")
    f <<= nm.mcut(f="0:customer,1:amount",nfni=True)
    f <<= nm.msum(k="customer",f="amount")
    print(f.run(msg="on"))
    # [['B', '8300'], ['C', '7200']]


Retrieve the file list
'''''''''''''''''''''''''''
There are many useful commands on UNIX-like OS.
Such as awk which treats structured data table freely, grep which select rows by pattern matching,
and sed which replaces string by the regular expression, etc.
By using the cmd method, it is possible for people familiar with UNIX commands to collaborate these commands with MCMD methods.
In the following, we introduce the program which processes the list of files by using three commands  ``ls`` ``tail`` , and ``sed``.
:numref:`special_ls` is the code.
``ls -l``  outputs the file information such as permissions, sizes, file names into the standard output.
Since the number of files is output on the first line, it skips the line by the command ``tail`` (read from the seconde line).
Then, the multiple space characters which are delimiters of the output of ``ls`` are replaced with comma by the command  ``sed``.
You can complete the file list just by adding column header by the method ``mcut``.


  .. code-block:: python
    :linenos:
    :caption: Example of retrieving file list by ls command
    :name: special_ls

    f=None
    f <<= nm.cmd("ls -l")
    f <<= nm.cmd("tail +2")
    f <<= nm.cmd("sed 's/  */,/g'")
    f <<= nm.mcut(nfni=True,f="0:permission,1:link,2:user,3:group,4:volume,5:month,6:day,7:time,8:filename")
    print(f.run())
    # [['-rw-r--r--', '1', 'foo', 'staff', '4997', '8', '3', '16:44', 'dat.csv'], ['-rw-r--r--', '1', 'foo', 'staff', '104', '9', '6', '10:56', 'dat2.csv'], ...]


Conversion of multibyte characters
'''''''''''''''''''''''''''''''''''''''''''
Lastly, :numref:`special_nkf` shows the example of |nkf| command which is used to convert multibyte characters for data cleaning.
Note that since this is a coding example only to operate, data ``dat.csv`` does not contain multibyte characters,
however, it is assumed that the file is written in Shift_JIS code.
Also, |nkf| needs to have been installed as an OS command.


  .. code-block:: python
    :linenos:
    :caption: Example of converting Shift_jis code to utf-8 code by nkf
    :name: special_nkf

    >>> import nysol.mcmd as nm
    >>> with open('dat.csv','w') as f:
    >>>   f.write(
    '''customer,quantity,amount
    A,20180101,5200
    B,20180101,800
    B,20180112,3500
    A,20180105,2000
    B,20180107,4000
    ''')

    >>> f=None
    >>> f <<= nm.cmd("nkf -Sw dat.csv")
    >>> f <<= nm.mcut(f="customer,amount")
    >>> f <<= nm.msum(k="customer",f="amount")
    >>> print(f.run())
    [['A', '7200'], ['B', '8300']]

  .. |nkf| raw:: html

    <a href="https://en.wikipedia.org/wiki/Network_Kanji_Filter" target="_blank">nkf</a>

