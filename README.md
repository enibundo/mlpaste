mlpaste.py -- Paste stuff.
=======================================================

[0] What is mlpaste.py
----------------------
This is a simple script to paste data to http://paste.pocoo.org/.
I had already done something like this mlpaste.ml which had a couple of bugs and since I started messing around with Python, I thought to bring the old idea to Python as well. 

[1] Using mlpaste.py
---------------------

* `python mlpaste.py` `file1` ,..., `fileN` -- Pastes the file from `file1` to `fileN` and displays results urls
                                       
* `python mlpaste.py` `-l LANGUAGE` `file` -- Will use the right coloration of the language `LANGUAGE` for `file` and will display url.

This is the first version of this script, so if you see anything wrong with it write me.
You can use this freely, modify it and distribute it as you wish.

--eni