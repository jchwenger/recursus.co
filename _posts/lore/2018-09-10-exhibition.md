---
layout: post
title: Exhibition
category: lore
permalink: /lore/exhibition/


show:
 - image_path: /assets/show/full1_horiz.jpg
   title: full1
 - image_path: /assets/show/full2_horiz.jpg
   title: full2
 - image_path: /assets/show/side1_vert.jpg
   title: side1
 - image_path: /assets/show/side2_vert.jpg
   title: side2
 - image_path: /assets/show/third1_vert.jpg
   title: third1
 - image_path: /assets/show/third2_vert.jpg
   title: third2
 - image_path: /assets/show/third3_vert.jpg
   title: third3

maps:
 - image_path: /assets/show/map2_horiz.jpg
   title: map2
 - image_path: /assets/show/map4_horiz.jpg
   title: map4
 - image_path: /assets/show/map3_vert.jpg
   title: map3
 - image_path: /assets/show/map1_vert.jpg
   title: map1

preparations:
 - image_path: /assets/show/hunglitup_horiz.jpg
   title: hunglitup
 - image_path: /assets/show/hunglitup2_horiz.jpg
   title: hunglitup2
 - image_path: /assets/show/hunglitup3_vert.jpg
   title: hunglitup3
 - image_path: /assets/show/closeupAIT1_vert.jpg
   title: closeupAIT1
 - image_path: /assets/show/closeupleft1_vert.jpg
   title: closeupleft1
 - image_path: /assets/show/closeupsq1_vert.jpg
   title: closeupsq1
 - image_path: /assets/show/closeupAIT2_horiz.jpg
   title: closeupAIT2
 - image_path: /assets/show/closeupsub1_horiz.jpg
   title: closeupsub1
 - image_path: /assets/show/closeupsubsq1_vert.jpg
   title: closeupsubsq1

configuration: 
 - image_path: /assets/show/prep1_horiz.jpg
   title: prep1
 - image_path: /assets/show/prep2_horiz.jpg
   title: prep2
 - image_path: /assets/show/prep3_horiz.jpg
   title: prep3
 - image_path: /assets/show/prep4_vert.jpg
   title: prep4

hurdles:
 - image_path: /assets/show/prep6hung_horiz.jpg
   title: prep6hung
 - image_path: /assets/show/prep7hung_vert.jpg
   title: prep7hung
 - image_path: /assets/show/prep8hung_vert.jpg
   title: prep8hung
 - image_path: /assets/show/prep9hung_vert.jpg
   title: prep9hung

tech:
 - image_path: /assets/show/prep_horiz.jpg
   title: prep
 - image_path: /assets/show/prep5wires_horiz.jpg
   title: prep5wires
 - image_path: /assets/show/wiresbottom_horiz.jpg
   title: wiresbottom
 - image_path: /assets/show/wirestopclose_horiz.jpg
   title: wirestopclose
 - image_path: /assets/show/wirestop_horiz.jpg
   title: wirestop

---

<link href="/assets/lightbox.min.css" rel="stylesheet">

  <div class="desc"><h4>The show</h4></div>
  <div class="photo-gallery-container">
  <div id="masonry1">
  {% for image in page.show %}
  {% if image.image_path contains 'vert' %}
  <div class="photo-gallery">
   <a href="{{ image.image_path }}" data-lightbox="Show">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% elsif image.image_path contains 'horiz' %}
  <div class="photo-gallery-wide">
   <a href="{{ image.image_path }}" data-lightbox="Show">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% endif %}
  {% endfor %}
  </div>
  </div>

  <div class="photo-gallery-container">
  <hr>
  <div class="desc"><h4>Map & catalogue</h4></div>
  <div id="masonry2">
  {% for image in page.maps %}
  {% if image.image_path contains 'vert' %}
  <div class="photo-gallery">
   <a href="{{ image.image_path }}" data-lightbox="Maps">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% elsif image.image_path contains 'horiz' %}
  <div class="photo-gallery-wide">
   <a href="{{ image.image_path }}" data-lightbox="Maps">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% endif %}
  {% endfor %}
  </div>
  </div>

  <div class="photo-gallery-container">
  <hr>
  <div class="desc"><h4>Almost there...</h4></div>
  <div id="masonry3">
  {% for image in page.preparations %}
  {% if image.image_path contains 'vert' %}
  <div class="photo-gallery">
   <a href="{{ image.image_path }}" data-lightbox="Preparations">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% elsif image.image_path contains 'horiz' %}
  <div class="photo-gallery-wide">
   <a href="{{ image.image_path }}" data-lightbox="Preparations">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% endif %}
  {% endfor %}
  </div>
  </div>

  <div class="photo-gallery-container">
  <hr>
  <div class="desc"><h4>Layout</h4></div>
  <div id="masonry4">
  {% for image in page.configuration %}
  {% if image.image_path contains 'vert' %}
  <div class="photo-gallery">
   <a href="{{ image.image_path }}" data-lightbox="Layout">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% elsif image.image_path contains 'horiz' %}
  <div class="photo-gallery-wide">
   <a href="{{ image.image_path }}" data-lightbox="Layout">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% endif %}
  {% endfor %}
  </div>
  </div>

  <div class="photo-gallery-container">
  <hr>
  <div class="desc"><h4>Hurdles</h4></div>
  <div id="masonry5">
  {% for image in page.hurdles %}
  {% if image.image_path contains 'vert' %}
  <div class="photo-gallery">
   <a href="{{ image.image_path }}" data-lightbox="Hurdles">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% elsif image.image_path contains 'horiz' %}
  <div class="photo-gallery-wide">
   <a href="{{ image.image_path }}" data-lightbox="Hurdles">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% endif %}
  {% endfor %}
  </div>
  </div>

  <div class="photo-gallery-container">
  <hr>
  <div class="desc"><h4>Technical details</h4></div>
  <div id="masonry6">
  {% for image in page.tech %}
  <div class="photo-gallery-last">
   <a href="{{ image.image_path }}" data-lightbox="Details">
    <img src="{{ image.image_path }}">
   </a>
  </div>
  {% endfor %}
  </div>
  </div>
  
<script src="/assets/js/jquery-3.3.1.min.js"></script>
<script src="/assets/js/imagesloaded.pkgd.min.js"></script>
<script src="/assets/js/masonry.pkgd.min.js"></script>
<script src="/assets/js/lightbox.min.js"></script>

<!-- Lightbox options -->
<script>
    lightbox.option({
      'wrapAround': true,
      'fitImagesInViewport': true
    })
</script>

<!-- Masonry */ -->
<script>
  $(function() {
    var $container = $('#masonry1');
    $container.imagesLoaded( function() {
      $container.masonry({
        itemSelector: ['.photo-gallery', '.photo-gallery-wide'],
        columnWidth: '.photo-gallery'
      });
    });
  });

 $(function() {
    var $container = $('#masonry2');
    $container.imagesLoaded( function() {
      $container.masonry({
        itemSelector: ['.photo-gallery', '.photo-gallery-wide'],
        columnWidth: '.photo-gallery'
      });
    });
  });

  $(function() {
    var $container = $('#masonry3');
    $container.imagesLoaded( function() {
      $container.masonry({
        itemSelector: ['.photo-gallery', '.photo-gallery-wide'],
        columnWidth: '.photo-gallery'
      });
    });
  });

  $(function() {
    var $container = $('#masonry4');
    $container.imagesLoaded( function() {
      $container.masonry({
        itemSelector: ['.photo-gallery', '.photo-gallery-wide'],
        columnWidth: '.photo-gallery'
      });
    });
  });

  $(function() {
    var $container = $('#masonry5');
    $container.imagesLoaded( function() {
      $container.masonry({
        itemSelector: ['.photo-gallery', '.photo-gallery-wide'],
        columnWidth: '.photo-gallery'
      });
    });
  });

  $(function() {
    var $container = $('#masonry6');
    $container.imagesLoaded( function() {
      $container.masonry({
        itemSelector: ['.photo-gallery-last'],
        columnWidth: '.photo-gallery-last'
      });
    });
  });
</script>
