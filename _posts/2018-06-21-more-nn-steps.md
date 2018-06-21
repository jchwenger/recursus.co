---
layout: post
title: More NN Steps
permalink: /more-nn-steps/ 
---

Back into the neural foundry. Found [this repo](https://github.com/nlintz/TensorFlow-Tutorials), which is a fine, simple piece of help to accompany Mital's tougher tutorials (still at session 3 unfortunately, on [autoencoders](https://en.wikipedia.org/wiki/Autoencoder)).

Going through a few of those I discovered a technique called 'dropout', which helps reducing overfitting (the situation where the networks creates a model which is too close to the data, thus not producing a general enough abstraction): in dropout some units (neurons) are randomly deactivated in the network, forcing it to keep working only with a reduced capacity. This has the effect of making the network 'rely' less on each and every one of its neurons, making it both more robust and less prone to overfitting.

<div class="video-container">
<iframe max-width="100%" height="auto" src="https://www.youtube.com/embed/NhZVe50QwPM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

<div class="video-container">
<iframe max-width="100%" height="auto" src="https://www.youtube.com/embed/LhhEv1dMpKE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

<div class="video-container">
<iframe max-width="100%" height="auto" src="https://www.youtube.com/embed/D8PJAL-MZv8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

<div class="video-container">
<iframe max-width="100%" height="auto" src="https://www.youtube.com/embed/ARq74QuavAo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

<div class="video-container">
<iframe max-width="100%" height="auto" src="https://www.youtube.com/embed/UcKPdAM8cnI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>
<div>&nbsp;</div> 
Also, I went back to something that I am still to grasp more fully, the concept of momentum in gradient descent:

<div class="video-container">
<iframe max-width="100%" height="auto" src="https://www.youtube.com/embed/k8fTYJPd3_I" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>
