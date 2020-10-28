---
layout: post
title: Wordsquares Mining
category: lore
permalink: /lore/wordsquares-mining/ 
---

This is proving to be more difficult than expected.

Slightly haunted by My previous attempt using machine learning to mine wordsquares (using the [t-SNE](https://distill.pub/2016/misread-tsne/) algorithm). That hadn't yielded the results I was hoping for, and for that reason (and others, less respectable ones) I left that aside, going for randomness and persistance instead.

Where am I now? I am searching for squares that have *literary* relevance (beauty, intricacy, force, subtlety, etc.). I work like a 'normal' writer, except for the fact that the texts are already written in front of me. As I mentioned already, the database act as an 'external imagination': in a more regular setting, I would look for the appropriate formulations, images, etc., and 'pick' the one I will present as the final text. In this case, I also pick, except the possibilities are 'physically' set, out there (as, you might argue, they are as well, except unwritten, in the cloud of virtual texts, in the former case).
 
When working for the pop-up exhibit this Spring (I 'only' had 200+k 3-squares at hand, then), I found out that the only way that ended up working was what I would now call 'manual' search: singular words picked by me, acting as a first search step, which reduces the amount of possibilities, and calls for a second choice, another words, which, in that case, usually reduced the number of possibilities enough so that I could then go and peruse the remaining squares, make up my mind if any was any good, if yes select, if not backtrack and use some other word, etc. I also 'studied' my database, discovering that some squares were symmetrical, others had words in the diagonals, etc. A lot of the more 'formal' attempts I made, focussing on the letter composition of squares in my machine learning project, did not yield much for my aims: in the end, meaning, and the images it carries, is all too important, and a lot of the 'formally salient' squares were just nonsensical or trivial. The same happens here, and it seems I made little progress since then.

Something I had briefly dabbled with previously, but introduced more seriously this time, is the use of preestablished dictionaries and list of frequencies in the mining process. The lists I have used so far are:  
- the Unix word list: I found it on my Linux Mint in the folder usr/share/dict/;
- the [Wordnet word list](https://stackoverflow.com/questions/34083039/nltk-wordnet-list-of-long-words#34086215), part of the [NLTK Python library](http://www.nltk.org/);
- A text version of the [Webster Dictionary](https://github.com/adambom/dictionary);
- The [20k most frequent words in Google](https://github.com/first20hours/google-10000-english), that allows me to rank squares by the frequency score of their containing words;  
- And the [full, 300+k version of it](http://norvig.com/ngrams/count_1w.txt), more of the same;
- The [10k most common words in the Wiki frequency list](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000), also for frequency scores.

I introduced them to try and limit the amount of abstruse words that litter my database (yes, I should have picked a smaller word list to begin with...). The remarkable thing, however, is that a lot of these squares do display interesting word combinations, alongside very rare, irrelevant or sometimes just banal other ones, squares which would not have been generated had I not had lexical oddities in my list in the first place.

I keep making interesting 'theoretical' discoveries relating to my database. For instance, for the current 5-squares (I am working on lists generated from the [litscape](https://www.litscape.com/) word list), *none* of them contain only words present in any of the dictionaries used, even the larger ones. There is always at least one which is too rare for them (even for the Wordnet list, containing 147+k entries).  Also, in the case of 4-squares, no square reaches the full word diversity score (12 different words), and the ones with the most reach 10. 


The major question I am faced with is the one of meaning, or rather 'evocative power', and what I 'allow' to exist in the space of the 'viable' squares. It appears to me now almost as a question of 'elasticity': is my (literary, poetic) consciousness capable of extending itself to these weird corners, without losing its consistency altogether (that would be, for instance, the position which would take *any* square and posit it as valid, thus eliminating all notion of aesthetic standard or comparison). It seems that it might prove difficult to find squares for which I 'click' as easily as with the subwords (ones that display an obvious meaning pattern, or a directly perceivable image, message, etc.), but perhaps I could still maintain the idea of an aesthetic standard, my 'line' or 'style', what I find worthy of exhibition, while lowering the bar only a little: agreeing with myself that I can have *corners*, as it were, of the squares, that I cannot fully account for (a word that means little in this context, or that I cannot expect even a learned viewer to have heard of, especially in an exhibition context, where dictionary look-ups are unlikely...).  
