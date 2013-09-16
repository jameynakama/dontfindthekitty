(Definitely) Don't Find The Kitty
================

**Version** whatever.man.0.1

This is (will be) a multi-platform port (Mac, Linux, Windows) of my old game of
the [same name](http://royal-paw.com/games/dont-find-the-kitty/).

Don’t Find The Kitty is a simple point-and-click game inspired by [Robot Finds
Kitten](http://www.robotfindskitten.org/). You must capture all the zoo’s moody
animals, besides the kitty, of course. You can play with 10, 25, or 50 animals,
as well as try Game B, where the animals give you hints about the kitty’s
attributes.

The Story
----------------

All of Planet Zoo’s animals have fled from their cages, and it’s up to you,
Melchior Eastwick, to capture them! However, the zoo’s trouble-making cat is
also on the loose, whose capture could bring an early and disastrous end to the
fiscal year! Do you have what it takes to capture all the animals and avoid
impending doom for your shareholders?

Building
----------------

### Requirements

- pygame
- pygcurse
- cx_Freeze

Building should be straightforward, as much as

`$ python setup.py bdist_mac`

Of course, this is for mac. There are other cx_Freeze commands for building on
Linux and Windows.

Unfortunately, cx_Freeze does not install correctly through pip, and pygcurse is
not available through pip. To remedy this, I built cx_Freeze from source and
installed into the virtualenv manually, and I moved pygcurse into the virtualenv
manually.
