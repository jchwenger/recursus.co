---
layout: post
title: Webscraping
permalink: /webscraping/ 
---

Quick dreams of scraping. 

Early on when encountering the miasmatic field of 'data science', I remember being struck by recurring quips such as: 'it's the data, stupid!'. Implying that, more often than not, problems arise less from the actual model, or algorithm, that has been devised, but by the dataset used, how 'clean' it is, how well prepared or curated. And quite a few practitioners seem to confirm that they spend a lot of their time simply preparing data, normalizing it, making sure it has the right characteristics & format, etc. 

I noticed such a thing working on both Wordsquares and Subwords: the type of word lists I am using is crucial, and can bring a lot of surprises. I noticed, for instance, that a large 3 letter words list I used, which contains oodles of abbreviations or rare/dialectal words I had never encountered before (and I am quite the dictionary junkie), did not contain the word 'sex'. Looking for lists that might be less littered with abstruse vocables, I feared that I would miss out on potential rare but glittering items, that could lead to beautiful pieces.

While thinking about what could be the best lists out there, I came across Allison Parish's [web scraping class](https://github.com/aparrish/dmep-python-intro/blob/master/scraping-html.ipynb) (the contents of which I am still to assimilate properly), that made me think I could not be far from being able to suck words from good dictionaries (Oxford, Cambridge, etc.) directly from their websites...

More references:
- The [Python library Beautiful Soup for web scraping](https://www.crummy.com/software/BeautifulSoup/);
- A [chapter recommended by Parish on the matter](https://automatetheboringstuff.com/chapter11/);
- What a few pages with lists of words look like: [Cambridge](https://dictionary.cambridge.org/dictionary/english/), [Dictionary.com](https://www.dictionary.com/list/a/1), the [French CNRTL](http://www.cnrtl.fr/definition/).
