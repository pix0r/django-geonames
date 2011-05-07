===============
django-geonames
===============

This is an experimental application for using Geonames data within
GeoDjango. 

Furthermore this is a fork of
[ramusus django-geonames](https://github.com/lazerscience/django-geonames),
containing some (osx specific) fixes:

* setup.py includes geonames/sql/* as package_data
* load_geonames checks to see if its run on OSX <= 10.6.7, 
  because `zcat` has a bug there, so we use `gzcat` instead.
  Hopefully this gets fixed with 10.7

I also encounter some weird error: `syncdb` wouldnt create the tables
specified by `geonames/models.py`. I didnt find the reason why this 
happens. However heres a workaround in case you encounter this too:

* add `geonames` to your `INSTALLED_APPS` (as you would anyway)
* now do `python manage.py sqlall geonames` and copy the sql from the output
* run `python manage.py dbshell`, paste the copied sql and execute it
* now that we have our tables created, you can follow the installation
  instructions

Installation
============

Note that running all this can take some serious time. The database is
pretty huge (~200mb WITHOUT alternateNames, which itself weights in 
at ~94mb). So you might want to do `load_geonames` over night, it did
take my macbook 18h28min to complete with a default 5200rpm drive,
you might find it a hell lot faster with a 7200rpm drive or some
SSD.

1. Add `geonames` to your `INSTALLED_APPS`
2. `python manage.py syncdb` so it creates the tables
3. `python manage.py download_geonames` will download all the data 
    you might need (and more)
4. `python manage.py compress_geonames` -- This will gzip the downloaded
    data, to minimize disk I/O during sql read.
5. `python manage.py load_geonames` -- Load the data.
6. Hours later: have fun ;-)
