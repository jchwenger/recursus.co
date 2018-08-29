---
layout: post
title: Multiprocessing
category: lore
permalink: /lore/multiprocessing/
---

Important discovery: it is possible to split tasks so that separate cores can work on them independently. I happen to have four on my machine, which is already a substantial speed increase. 

In the case of my [Wordsquares](https://github.com/jchwenger/wordsquares/tree/multicore) project, it is possible to split the word list into number-of-cores parts, and apply the process to each (whilst keeping the entire list for the actual building of the squares). This is in effect a linear increase: had I access to ten, twenty cores, I could divide the computation by that number.

Python works under what is known as the [GIL (Global Interpreter Lock)](https://en.wikipedia.org/wiki/Global_interpreter_lock), which prevents any Python operations to occur simultaneously (all operations, at the bottom level, occur one after another in a specific, traceable order). In order to work with mutliple cores, one has to use the [multiprocessing module](https://docs.python.org/3.5/library/multiprocessing.html), where it is possible to assign a number of cores, and tell Python which tasks should be taken care of by which core. (It creates entities called 'workers', which has a sweet Marxian overtone to it.)

Several articles & references, explaining the difference between multithreading and multiprocessing [here](https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing), [here](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/), [here](https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python).



