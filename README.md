GrowStat
========

*by Nihlaeth*

About GrowStat
--------------

With GrowStat you can gain insight in the efficiency of your hydroponics
system. What nutrient solution works best? Does a lower pH affect your
harvest in a positive way? Can your plants do with less water? Thanks to
GrowStat you'll never have to wonder again!

GrowStat is a web app for you to record and analyse data on your
hydroponics system. Its web framework is Pyramid, its web server is
Waitress, and its database is SQLite.

Get up and running
------------------

### Using GrowStat

```sh
# Installing
git clone https://github.com/nihlaeth/GrowStat.git
pip install ./GrowStat

# Running
cd Growstat
pserve production.ini
```

If this doesn't work, create a clean virtualenv (`virtualenv myenv
--no-site-packages`), and try installing GrowStat there and running it.
If that also fails, the build is broken; please [inform the
developer](http://github.com/nihlaeth/GrowStat/issues).

To access GrowStat, direct your browser to 
* http://127.0.0.1:6543 if you're accessing it locally or 
* http://hostname:6543 if you are connecting remotely.

### Developing GrowStat

```sh
# Installing
git clone https://github.com/nihlaeth/GrowStat.git
pip install -e ./Growstat  # install in development mode ('editable') 

# Running
cd Growstat
pserve development.ini     # has a debugging toolbar etc.
```

You should now be able to make changes to Growstat and see them
reflected instantly in your browser.

The development version of GrowStat is served on port 8080:
* http://127.0.0.1:8080 if you're accessing it locally, or 
* http://hostname:8080 if you are connecting remotely.

### Known-good package collection

This is a list of package versions with which GrowStat is known to work.
(Only listing the packages that GrowStat requires directly.)

* pyramid               (1.4.2)
* pyramid-debugtoolbar  (1.0.6)
* waitress              (0.8.5)
* pysqlite              (2.6.3)

To Do
--------
Recording pages:
* Lumen tracking capabilites
* Picture uploading
** Build in size check and limit (30MB max, 50kb min)
** Search for 'code words' in images
** Change random pixels in images to frustrate code injection - without sacrificing considerable quality loss
* Make Nutrients separate items to be added and selected

Edit pages:
* All of them, including delete pages.

Data views:
* build in calendar functions
* select plotting engine and build an api for it
* add per-plant data view
* add timeline view and template
* add useful analytic pages

Less priority:
* authentication system
* backup & backup restore function

Documentation (wiki)
* write style guide
* write manifest
* write extensive tutorial / getting started
* BETTER COMMENTING
* select open source license

For later:
* migrate to a database that doesn't suck
* notifications
* sharing options
* multiuser functionality
* admin system and permissions config
* wildcard domain support
* datalogger information import
* data export (in a format suitable for analysis software like spss)

Contributors
------------

* Nihlaeth
* Sietse
