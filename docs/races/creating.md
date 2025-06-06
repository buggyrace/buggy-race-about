---
title: Creating a race
nav_order: 20
layout: home
parent: Racing
has_children: false
---


# Creating a race

{: .navigation}
**Admin** → **Races** → **Add new race**

To create a race, you need to provide some basic information:

* **Title**  
  Use the title to distinguish this race from any others (if you can't think of
  anything, use _First race_, _Second race_, ...).

* **Description**  
  The description is shown to students and can be as poetic as you want. If you
  are planning on adding environmental factors to the race, mention them here
  (how that is implemented will depend to some extent on what mechanism you're
  going to use to actually run it).

* **Race start time**  
  This is the timestamp of the time when entrance to the race closes. In effect,
  it's the moment when you download the race file, effectively taking a snapshot
  of the latest buggies that students have uploaded to the server. The race time
  must be unique (you can't run two races at the same time on the same race
  server).

{: .note}
When you choose a race time, you're committing to _downloading the race file_
from the server as close to this time as possible!

{: .note-two-mins-to-midnight}
The default start time — which you do not have to accept! — is **two minutes
to midnight, tomorrow**. Effectively this means "the end of the day". If you're
not going to be awake then, change this to an earlier time!

  
* **Cost limit**  
  The cost limit is a critical part of the project, because it's the fine-tuning
  that the students' buggy editors can be most helpful in allowing. To start
  with be generous, but as the project goes on, there is a case for fluctuating
  the cost limit between races. A buggy whose total cost is greater than the
  cost limit is disqualified from that race.

* **Racetrack**  
  In practice, the racetrack you choose influences the length of each circuit
  of the track (the _lap length_). This matters because students' buggies can
  and will run out of fuel (if they've opted for consumable power supplies). But
  it also serves as an important visual identifier, since the racetrack is shown
  as an aerial view in the race player. 
  The easiest way to add racetracks is to pick them from the collection on the
  server, although if you know the URLs of more you can enter them manually.
  See [more about racetracks](racetracks), including how to make your own.

{: .screenshot}
![Screenshot of picking a racetrack](/docs/img/screenshots/pick-a-racetrack.png)

{: .caption}
The Select-a-racetrack dialogue lets you pick from a collection of examples
that are available by default — or you can create your own.

{: .note}
There's a **Show used-by races** button (requires JavaScript) that will display,
in a list under each racetrack, the races that are using it. This is helpful if
you want to run each of your races on a different track. "Used by" indicates
that the race used, or will use, the _same_ URLs (image and path SVG) as the
racetrack. (If you edit racetracks after you've created a race, or duplicate
them, this may affect the "used-by" results.)


* **Is visible?**  
  Students can only see races that you have explicitly marked as "visible" on
  the server. This lets you experiment without publishing them: if you choose
  `No`, only staff accounts will be able to see them.

{: .note }
Only one not-yet-run race is shown on the race server — the _next_ one. So even
if you make ten races, only the next one will be shown (together with any that
have been run, provided you've marked them visible too).

* **Are results visible?**  
  The results of the race won't be visible to students until you choose `Yes`.
  In the admin, staff accounts can access them as soon as you have uploaded them,
  so you can check how they look before publishing them for the students.

* **Number of laps**  
  Over how many laps of the racetrack is this race to be run? If you're not
  sure you can set this when you upload the results. It's best to decide in
  advance, in case it affects students' decisions as to how they equip their
  buggies (for speed, or endurance). However, our experience is that this isn't
  a critical factor, at least at the start of the project, and we adjusted it
  to match the behaviour of the submitted buggies to avoid all races petering
  out with everyone running out of fuel, and making the replays very dull.
  Ideally you avoid this by stressing the importance of fuel to your students.

* **Is Did-Not-Finish a position?**  
  Are buggies who do not finish all the laps given a position? If so, how far
  they got (distance travelled) is used to calculate their position relative to
  other buggies. The default, _Yes_, is generous: for example, it means that
  qualification in the race guarantees a result (even if, in the extreme case,
  the buggy doesn't move forward at all). This rewards students who manage to
  qualify (which is a key test of the quality of their buggy editor) but
  doesn't penalise them for a badly designed buggy (e.g., one with no fuel).
  Set to _No_ for a harsher (but more real-world) approach to race results.

  

For more about publishing results, see
[uploading race results](uploading-results).

---

* Previous: [About races](about)
* Next: [How students enter](how-students-enter)
