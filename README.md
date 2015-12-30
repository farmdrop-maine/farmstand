Bazaar
==============
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/farmdrop-maine/farmstand?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build
Status](https://travis-ci.org/farmdrop-maine/farmstand.svg?branch=master)](https://travis-ci.org/farmdrop-maine/farmstand)

Bazaar is a multi-vendor store front and inventory manager designed for use with
farm vendors who have a diversity of stock, sale prices and use scenarios. Once
an order is placed, including products from multiple vendors, a single payment
is processed and all the different vendors drop their products off at a central
location for pick up.

Start your engines, err projects!
---------------------------------

Your first order of business is to rename some things. Unless your project
is also called farmstand, you'll likely want to rename things. The easiest way
to get started is:

make name="<myproject_name>" rename

That should do all the important replacements. The final step will be removing
the .git folder and initializing your own repository and lastly tweaking the
setup.py file, else you're likely to give me credit for your project and to 
provide a pretty terribly confusing description to PyPI if your project ever
lands there.

Easy bootstrapping!
-------------------

Powered by the ubiquitous Makefile ... this should be pretty easy:

1. make install
2. make run
3. open your browser to: http://127.0.0.1:45000


Librarys, librarys, librarys!
-----------------------------

Of course, we could provide a vagrant file and a provisoner and all 
that jazz. But I'd rather provide a make file for installing everything
into a venv and let you muck about with libraries. Those of you on
Linux shouldn't have too much trouble installing the requisite development
libraries below. The names are for debian-based distros, but they 
exist for all major distros. 

On Mac it may be a little tricker. Homebrew will get you quite far, but
first you have to install the bloated XCode and the CLI tools.

The libraries are:

  * libmemcached-dev
  * libfreetype6-dev
  * libjpeg-dev

