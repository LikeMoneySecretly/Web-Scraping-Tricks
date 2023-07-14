# Web-Scraping-Tricks

Basic repository of a few of the tricks i've had to use over the years, will add more as and when I can be bothered to split them off from
their main source code and remove identifiying features that will get me sued.

# Contents (so far)
1) EventListenerKiller.py
   
   - Simple demonstration of how to remove an event listener from a website using google dev tools
     # Setup
       - Please remember that this is run using playwright connect so you will need to task manager kill the chosen browser first
       - before running it with -remote-debugging-port=9222 (in this case) added to the .exe file
       - You will need to open google dev tools for the chosen tab manually, mainly because I was too lazy to do it with code and this is only
       - a proof of concept
      # What does this code do?
         - Injects a javascript string into google dev tools to delete the chosen event listener
         - Literally the only way to do this nowadays,
     # Why is this useful?
         - Pain in the ass websites have been using event listeners since forever to detect when
         - Console commands such as querySelectorAll or getElementsByClassName are run, this simply uses the dev console
         - to remove that ability 
     
