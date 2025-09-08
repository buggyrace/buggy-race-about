---
title: Custom racetracks
nav_order: 90
layout: home
parent: Racing
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

You can edit existing racetracks or add your own. If the config setting
`IS_STORING_RACE_ASSETS_IN_DB` is set to `Yes` (the default) — then you can
upload the JPG and SVG files needed. Storing your own race assets on the race
server is simplest, but note that they are stored (as binary objects) in the 
database. Alternatively, you can host yourself on a webserver with a friendly
CORS policy, and provide the URLs.

## Basic components: image, path, lengths, and start offset

Each racetrack consists of:

* **URL of racetrack image**  
  The image must be a landscape image twice as wide as it is tall (2:1 aspect
  ratio). Any graphic format supported by browsers will do, although ideally
  it should be optimised for size. The example racetracks on the server have
  URLs that point to the server because those track image files are pre-loaded.
  
  The example files are 1024 × 512 (pixel dimensions) JPEG files.
  
  If you upload a JPG image to store in the database, note that the race server
  will make it available through a URL path that is slightly different from
  that used by the example ("built-in") racetracks.

* **URL of path SVG**  
  The path is overlaid on the background image in the replay animation. See
  more about the SVG specifics below: it must be a closed (loop) `path` in
  a 200 × 100 viewport. The direction of the race (the way the buggies will
  move around the track: clockwise or anticlockwise) is implicit in the order
  in which the points within the path have been specified. The start and finish
  line is, by default, where the path start point is specified.
  
  If you upload a SVG file to store in the database, note that the race server
  will make it available through a URL path that is slightly different from
  that used by the example ("built-in") racetracks.


* **SVG path length**  
  The calculated length of the SVG path is needed when displaying and animating
  the race. For efficiency, it's handled as a stored value, rather than being
  calculated every time its needed. The **View** option on the server will show
  the result of the calculation so you can check it (and, if necessary, edit the
  record to add it).

* **Lap length**  
  This is the length of the racetrack in "game" units (perhaps those are metres,
  although currently it's not strictly enforced) — that is, regardless of the
  length of the graphical representation of the racetrack's SVG path. Use this
  to keep all the racetracks in your project to be comparable size. If a
  racetrack doesn't have an explicit lap length, it will default to using the
  SVG path length (in which case, game units _are_ SVG units).

* **Start offset**  
  By default, the start (and finish) line of the racetrack is the position of
  the SVG path's first point. But if you want to change this, the start offset
  is how far around the track (in "game" units) the start (and finish) line is.
  Currently this simply affects how the race is displayed in the
  [race-player](../glossary#race-player).
   
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
If you're using the default [race-player](../glossary#race-player), your SVG
**must** be within a viewbox that's 200 × 100 — for example:  
`viewBox="0 0 200 100"`  
You cannot use a `scale` transform to fix this; the `viewBox` attribute must
describe a 200 × 100 box (transform won't work because the JavaScript currently
parses the SVG).

The racetrack's path SVG must contain a _single_ `path` element that describes
a closed loop. The `fill` and `stroke` should be `none` as it's not used for
display — it's used as the path the buggies are mapped onto during the replay
animation. If you do set either of these attributes to a colour, the racetrack
will still work... but it's probably better to keep visual representation of
the track in the bitmap image that is layered beneath it.

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

* Previous: [Editing races](editing)
