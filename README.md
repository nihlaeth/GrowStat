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

```sh
git clone https://github.com/nihlaeth/GrowStat.git
pip install ./GrowStat
cd Growstat
pserve development.ini
```
If this doesn't work, create a clean virtualenv (`virtualenv myenv
--no-site-packages`), and try installing GrowStat there and running it.
If that also fails, the build is broken; please inform the developer.

To access growstat, direct your browser to 127.0.0.1:8080 if you're accessing it locally or hostname:8080 if you are connecting remotely.

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
* add harves weight view and template
* add pic upload view and template
* add log recording page and template
* make watering configurations traceable over time (track changes to the settings)

Edit pages:
* All of them, including delete pages.

Data views:
* add timeline view and template
* add useful analytic pages

Less priority:
* authentication system
* backup & backup restore function

Maybe fun for later:
* notifications
* sharing options
* multiuser functionality
* admin system and permissions config
* wildcard domain support

Contributors
------------

* Nihlaeth
* Sietse
