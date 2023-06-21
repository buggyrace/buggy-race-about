---
title: Custom racetracks
nav_order: 90
layout: home
parent: Running races
has_children: false
---

# Managing and customising racetracks

{: .navigation}
**Admin** → **Races** → **View racetracks**
  

Racetracks are nominally where the buggy race takes place. In practice, they
consist of a couple of files — one the background image and the other an SVG
file describing the geometry of the path that the buggies will follow. Although
these two files can be independent, in practice they are usually closely
related because the SVG path follows the track that is depicted in the image.
This page describes what you need to know in order to make your own.

The race server is pre-loaded with a few example tracks. If you're creating
your own custom tracks you might not want to use these, so you can suppress
them by setting the config setting `IS_SHOWING_EXAMPLE_RACETRACKS` to `No`
in the "Races" group. Otherwise, you'll see a button marked **Add missing
racetracks** if any of the example tracks are not in the database.

You can edit existing racetracks or add your own — but note that any new files
(JPG or SVG) that you make are _not_ stored on the race server. You have to host
them, and provide the URLs here.

## Basic components: image, path, length

The racetrack consists of:

* **URL of racetrack image**  
  The image must be a landscape image twice as wide as it is tall (2:1 aspect
  ratio). Any graphic format supported by browsers will do, although ideally
  it should be optimised for size. The example racetracks on the server have
  URLs that point to the server because those track image files are pre-loaded.
  
  The example files are 1024 × 512 (pixel dimensions) JPEG files.

* **URL of path SVG**  
  The path is overlaid on the background image in the replay animation. See
  more about the SVG specifics below: it must be a closed (loop) `path` in
  a 200 × 100 viewport — those dimensions matter because they effect the length
  of the path (currently there is no scaling factor).

* **Lap length**  
  This should be the calculated length of the path in the SVG. It's stored
  explicitly to avoid having to calculate it every time it's needed. The
  **View** option on the server will show the result of the calculation so you
  can check it. Make sure you save the same value.

## Races copy racetrack URLs

When you [create or edit a race](creating) and select a racetrack, you are
really just _copying_ the data from the racetrack (the two URLs and the implicit
lap length) into the race. If you subsequently edit the racetrack, the **race**
won't change.

## How to make your own SVG

[Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG)
(SVG) are a web-based standard graphic format. Many drawing applications let
you draw a shape and then export to SVG. The unusual thing about the racetrack
path is that the file you create ultimately doesn't display anything — because
the path should be invisible. It might be easier to use your drawing package to
make the path with a stroke colour, and then edit it afterwards to change it.
SVG files are text files, so you can go into a text editor and change the
`stroke` attribute to `none`, for example.

## Detailed requirements of the SVG

{: .note}
Since the length of the path is significant — the "unit" of distance is used in
the calculation of how far the buggies move, for example, it's a good idea to
work on a 200 × 100 layout as there's currently no "scale" option.

The racetrack's path SVG must contain a _single_ `path` element that describes
a closed loop. The `fill` and `stroke` should be `none` as it's not used for
display — it's used as the path the buggies are mapped onto during the replay
animation.

The start point of the path is significant — it's where buggies start and end
their laps. Buggies will follow the path in the direction described, that is,
whether it is a clockwise or anticlockwise track will depend on how you've
made the SVG.

{: .screenshot}
![Viewing the SVG as admin on the server](/docs/img/screenshots/racetrack-svg-viewer.jpg)

{: .caption}
You can inspect the SVG path — which is normally invisible — with the **Show**
buttons when viewing the racetrack on the server. Different colours are offered
so the track is clear against whatever background image you're using.

### Example SVG path

This example is from `racetrack-03-path-429.svg`, one of the example paths on
the race server. Note the `viewBox` attribute, and that the file contains only
one `path` element. The length of the path turns out to be `429` — you can
verify this on the server when viewing racetracks.

The buggy race software anticipates only one `translate` transformation in the
path's `transform` attribute (it's used when determining how to place the
buggies as well).


<pre style="white-space: pre-wrap;border:1px solid #ccc;padding:1em;"><code class="language-svg">&lt;?xml version="1.0" encoding="UTF-8" standalone="no"?&gt;
&lt;svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 200 100" text-rendering="geometricPrecision" shape-rendering="geometricPrecision" style="white-space: pre;"&gt;
    &lt;path d="M0,0C18.6,0,37.2,0,55.8,0C67,0,73.6,8.2,73.6,17C73.6,29.4667,73.6,39.2085,73.6,51.6752C73.6,63.0752,65.2,69.8,55.8,69.8C27.4,69.8,-1,69.8,-29.4,69.8C-40.2,69.8,-49.6,62.0752,-49.6,51.6752C-49.6,39.2085,-49.6,29.4667,-49.6,17C-49.6,8,-41.8,0,-29.4,0C-19.6,0,-9.8,0,0,0Z" fill="none" stroke="none" stroke-width="0" transform="translate(89.8,15.2)"/&gt;
&lt;/svg&gt;
</code></pre>


---

