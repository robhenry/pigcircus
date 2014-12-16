pigcircus
=========

A set of Python UDF to extend the functionality of Apache Pig

These python UDFs can be particularly helpful for people who are migrating from Hive to Pig. Hive has a very rich set of UDF to provide additional functionality. Most of the UDF here have been inspired whilst porting Hive scripts over to Pig. 

Pig version 0.8 > supports UDFs written in Python. Pig uses Jython to dynamically compile the python to Java bytecode. This allows for the highest possible performance.

It’s worth nothing that Jython only supports Python version 2.5 so you won't find Python 3 features here.
