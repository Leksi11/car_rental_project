Quick Start Guide
=================

First, clone the repository from Github.


Virtual environments and Settings Files
---------------------------------------
 
First, you must know your Python 3 path::
 
    $ which python3
 
which is something similar to /usr/local/bin/python3.
 
Next, create a Development virtual environment with Python 3 installed::
 
    $ mkvirtualenv --python=/usr/local/bin/python3 cr_dev
 
where you might need to change it with your python path.
 
Go to the virtual enviornment folder with::
 
    $ cd $VIRTUAL_ENV/bin
 
and edit the postactivate file.:
 
    $ vi postactivate
 
You must add the lines: ::
 
    export DJANGO_SETTINGS_MODULE="taskbuster.settings.development"
 
Repeat the last steps for your testing environment::
 
    $ mkvirtualenv --python=/usr/local/bin/python3 cr_test
    $ cd $VIRTUAL_ENV/bin
    $ vi postactivate
 
where you have to add the lines::

    export DJANGO_SETTINGS_MODULE="taskbuster.settings.testing"
 
Next, install the packages in each environment::
 
    $ workon tb_dev
    $ pip install -r requirements/development.txt
    $ workon tb_test
    $ pip install -r requirements/testing.txt
 
 
 
Internationalization and Localization
-------------------------------------
 
Settings
********
 
The default language for this Project is **English**, and we use internatinalization to translate the text into Russian.
 
If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable in the file *settings/base.py*. The language codes that define each language can be found |codes_link|.
 
.. |codes_link| raw:: html
 
    <a href="http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx" target="_blank">here</a>
 
For example, if you want to use German you should include::
 
    LANGUAGES = (
        ...
        'de', _("German"),
        ...
    )
 
You can also specify a dialect, like Luxembourg's German with::
 
    LANGUAGES = (
        ...
        'de-lu', _("Luxemburg's German"),
        ...
    )
 
Note: the name inside the translation function _("") is the language name in the default language (English).

 
 
Translation
***********
 
Go to the terminal, inside the taskbuster_project folder and create the files to translate with::
 
    $ python manage.py makemessages -l ru
 
Next, go to the locale folder of your language::
 
    $ cd car_rental/locale/ru/LC_MESSAGES
 
  You have to edit the file *django.po* and translate the strings.
 
Once the translation is done, compile your messages with::
 
    $ python manage.py compilemessages -l ru
 
 
 
Tests
*****
 
 
 
 
Useful commands
---------------
 
A list of all the commands used to run this template::
 
    $ workon cr_dev
    $ workon cr_test
 
    $ python manage.py makemessages -l ru
    $ python manage.py compilemessages -l ru