---
layout: post
title: Cloud Computing
permalink: /cloud-computing/ 
---

For the first time in years, I feel the computational resources I have access to are not sufficient to achieve my goals. 

I am still planning on completing this third part, '[AIT](https://github.com/jchwenger/ait)', neurally to generate prose texts, and it does feel that the quality of the results, especially the amount of 'human' editing that will be required, will depend on the computational power I will be able to access, more specifically: if I will be able to use GPUs to hone my lstm model.

So far I looked into Google Colaboratory, Google Cloud Computing, and Amazon AWS (I also know of [FloydHub](https://www.floydhub.com/) and [Heroku](https://www.heroku.com/), but apart from [this article](https://medium.com/@rupak.thakur/aws-vs-paperspace-vs-floydhub-choosing-your-cloud-gpu-partner-350150606b39) my research has not been extensive).

As often happens, I stumble across splinters of the future more easily than simple, helpful insights for the preset. Thus, I know now what is likely the next step after [GPUs](https://en.wikipedia.org/wiki/Graphics_processing_unit), themselves already the major facilitator technology for the whole deep learning frenzy: [TPUs](https://cloud.google.com/tpu/), otherwise known as 'Tensor Processing Unit', developed by Google and, surprise, optimised for TensorFlow. I saw that it was possible to rent them, or even cluster of those, on the Google Cloud Platform. Of use if I ever want to take neural text generation to the next level. For squares as well, that is, for (textual) database generation. 

But most of all, for sanity. Having one's laptop hotly crunching next to one day and night all too often induces a [Fuselian](https://en.wikipedia.org/wiki/Henry_Fuseli) feel of horror.
![Fuseli Nightmare]({{ "/assets/fuseli-nightmare-41-4-bqscan.png" | absolute_url }})
