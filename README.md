useful.py
=========

A script that takes all the ids and classes from an html file and puts them as a block comment at the top of your css/js for easy reference

USAGE
========

python useful.py sourceFile targetFile

You can also pass multiple target files.

python useful.py sourceFile targetFile1 targetFile2...

you can use as many target files as you want but it is memory intensive to do so.
It may crash.

OUTPUT

========

The output will look like

/*
ID's:
    Id1
    Id2
    Id4

Classes:
    class1
    class2
    class3
*/

Your js/css here.
