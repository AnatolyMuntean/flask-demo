# Python3 Demo
Dummy Python web-application that covers most of the Flask framework basic functionality.

## Usage
Run directly by typing in terminal `./run.py`

**OR**

Run as a WSGI application, for apache2 users you would need to install `libapache2-mod-wsgi` and enable it - `a2enmod wsgi`.

In your virtual host (change values in square brackets to yours):
```
<VirtualHost *:80>
        ...

        WSGIDaemonProcess [APP_NAME] user=[USER] group=[GROUP] threads=5
        WSGIScriptAlias / [PATH_TO_YOUR_SOURCES]/sample.wsgi
        <Directory "[PATH_TO_YOUR_SOURCES]">
                WSGIProcessGroup [APP_NAME]
                WSGIApplicationGroup %{GLOBAL}
                AllowOverride All
        </Directory>

        ...
</VirtualHost>
```

Create the database (SQLite) by running in terminal `./db_create.py`.

When running as WSGI application and after making changes to sources, make sure to run `./reload.sh`.

## Credits
Based on this tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

