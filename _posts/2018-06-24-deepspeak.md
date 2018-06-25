---
layout: post
title: DeepSpeak
permalink: /deepspeak/
---

An idea is taking shape: transposing DeepDream to text (see [this page](https://distill.pub/2017/feature-visualization/) for a break-down of what happens in deep neural nets, the foundation for DeepDream images). 

It could be called 'DeepSpeak' (Orwellian [wink](https://en.wikipedia.org/wiki/Newspeak)). 

What we need is:
- a neural network (probably LSTM, but features of ConvNets might be useful here) that can learn features from text input (and hopefully expand on [this bit of research](https://karpathy.github.io/2015/05/21/rnn-effectiveness/);
- the ability to see what is happening at a neuronal level, and tweak certain neurons so that they start activating more often or differently;
B
- a way of outputting text with the results of the tweaked network, so as to produce a 'hallucinating' result in the same way as DeepDream does with images: the network would either start twisting and inflating specific parts of a text in particular ways, e.g. transforming the vocabulary, adding sentences or phrases, or perhaps creating words on the fly ([Finnegans Wake](https://www.finwake.com/01/) comes to mind).

Treat text like an image (which we read as computer read images: element-wise, linearly): each symbol as a pixel, the whole text as one object of a certain size (total number of characters). Perfectly possible to translate symbols into numbers (which already happens under the hood). The entire text (poem, novel, play, etc.) seen in one snapshot by the network &mdash; that is, in the same way as a network 'sees' an image, and learns from it. It might be an interesting way of learning about larger 'areas' of text (e.g. aself-contained scene, departure/arrival of characters or topics, the detection of which could work in the same way as the detection of edges and shapes in ConvNets for CV). Direct links to [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) to detect the overall topic, atmosphere, characters or intrigue in a passage. 

My knowledge of networks is still incipient. I would need to learn more, a _lot_ more, about ConvNets, LSTMs, and related matters. 

Two interesting articles, that should lead to further research:
- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah;
- [Attention and Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/) by Christopher Olah and Shan Carter.

As well as [a talk summarizing the contents](https://skillsmatter.com/skillscasts/6611-visualizing-and-understanding-recurrent-networks) of the already mentioned [Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/).

