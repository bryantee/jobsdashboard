PREAMBLE:

This is my first github project. It's also my first real python project that isn't basically a script for executing a series of system commands. I'm working on this for a few reason:

1. Further learn Python
2. Learn how to use Git and GitHub
3. Prototype a simple program for showing open jobs for general contractors and basic status.

My ultimate goal is to turn this into a Django project which I intend to also have hosted on github. My plans are to deploy a simple working version on a Raspberry Pi on our company intranet along with Django, SQLite3 and a simple web server. The functionality being the ability to add, display and modify open jobs that we're working on at any given time. (Address, due dates, sub-contractors, job price, etc.) Although I don't intend to actually use any of this code here for anything other than conceptualizing ideas for the next project, feel free to critique me or give some tips. A pull request would be fine too. Thanks :)

USEAGE:

It's pretty straight forward. There are two files - jobs_dash.py (where jobs are instantiated and manipulated. I launch this in an interactive shell for testing.) and jobs.py (the class module). jobs_dash.py imports jobs.py when executed. That's about it. Pretty useless and basic.


-Bryan
