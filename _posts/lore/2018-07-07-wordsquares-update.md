---
layout: post
title: Wordsquares Update
category: lore
permalink: /lore/wordsquares-update/
---

Various updates on the Wordsquares front.  

- Letter-based: an improvement on the original C++ implementation (which, I realised later, has a huge mistake in it, which I am too busy to correct now, namely that the whole calculation of the square letters & word superset for the current square being searched is not used in the program!) was to switch from a word-based to a letter-based implementation, namely where, starting from the 'first word', on row 0, one could check for *letter* availability, instead of word availability, in the following way: starting at row 1, one goes through all the possible letters (of the square letters, calculated beforehand) for this particular slot (row 1, column 0), checking for each one if 1) there are words starting with this letter in our row 1 words (using prefix search in our Dawg), 2) if there are words starting with the prefix composed of letter (0,0) (first letter of the first word) and the current letter in our superwords for column 0; if both conditions are met, recurse, and start the process again for row 1, column 1. Visually:
Check for all letters in (0,1) = 'a', check for column words starting with 'ba', row words starting with a; if ok, move to next column, this time check for prefix 'lb' vertically and 'ab' horizontally, etc. (a little trick with indexes is required when reaching the end of the row, as well as when, going back in the recursion, we go back to the final row, but nothing too devilish): 

    ```
    b l a h ->  b l a h
    a ? ? ?     a b ? ?
    ?             ?    
    ?             ?    
    ``` 

    A full square is found when we reach the bottom right corner (at which point we write a line to the file). The recursion processd ensures that we go through all possibilities.  
- Diagonals: given the downright obscene amount of squares obtained with my larger (litscape, see next point) dictionary, I updated my code in the master branch to include a starker constraint. The program will only save squares that also have words in the diagonals (which I implemented within the recursion process, instead of at the very end - I am not certain of the gain in computation time, as that means many more Dawg look-ups, but the idea was indeed not to go through all the possible squares, but to skip to the next iteration as soon as no word is present in either of the diagonals). This allowed me to reduce the quantity of 4-squares from an estimated of several hundred millions to a bit more than 200k, which is somewhat manageable for now (750k for 5-squares). Visually again, this means:

  <pre>
    b l a h -> b l a h 
    a u ? ?    a u l ? 
      ? ?        ? ?   
      ?   ?    ?   ?   
  </pre>
- Dictionaries: my default dictionary at first, or, I should say, my default lists of words, was drawn from [litscape](https://www.litscape.com/), and is fairly big (250k+ words). I encountered problems when producing 3-squares, as a lot of the words seemed either nonsensical, or too rare, or generally rather irrelevant to what I wanted. I began realising the difference that the input dictionary, and with that got a glimpse into what data people talk about when they stress the importance (and toil) of 'cleaning up data'. I then rebuilt some databases using another source, the 20k most frequent words in the Google word database, found [in this repo](https://github.com/first20hours/google-10000-english), and could get interesting results (e.g. 6-lettered squares, which would have taken me quite a long time to generate with the larger dictionary). It is tricky to think of an 'ideal' dictionary, even if it would be nice to be able to access e.g. the list of entries in the Oxford or Cambridge English Dictionaries (let alone the OED). The advantage to use internet-scraped word lists, such as Google's, is that you get recent slang words and proper nouns (with a huge bias toward figures that people talk about a lot online).   
- Multicores: still obsessed with database building, I realised that letting my computer run for days and days (1-2 weeks to build the 750k+ 5-squares) was not so good for my workflow and mental state. In an ideal world, I would either have two computers, the one doing the crunching being safely out of sight, or I would use the Cloud. Having spoken with friends who are experienced in this field, I realised that for a job like this one [multiprocessing](https://docs.python.org/2/library/multiprocessing.html) was the way to go (multiprocessing allows you to bypass the Global Interpreter Lock, which prevents more than one Python process to be computed at any one time, whereas multithreading allows you to have a more flexible temporality, e.g. make an API call, go on with your computation, and use the result when it is available, which does not imply parallelizing operations at a processor level). I found some quick tutorial/references [here](https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing), [here](https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b) and [here](https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python#3046201) and implemented it, hopefully correctly, harnessing all the cores of my machine. Using this seems to speed things up even more on my quad-core Lenovo, but I haven't actually made rigorous tests. The idea, in theory, would be to submit that as a script to a supercomputer, where I could divide my lists into 10, 20 (one chunk per core, even if the word look-ups are made on the total words), and go through big dictionaries fast.
