# Python3 Demo
Dummy Python web-application that covers most of the Flask framework basic functionality.

## Usage
This is a WSGI application, for apache2 users you would need to install `libapache2-mod-wsgi` and enable it - `a2enmod wsgi`.

In your virtual host:
```
<VirtualHost *:80>
        ...

        WSGIDaemonProcess py-sample user=[USER] group=[GROUP] threads=5
        WSGIScriptAlias / [PATH_TO_YOUR_SOURCES]/sample.wsgi
        <Directory "[PATH_TO_YOUR_SOURCES]">
                WSGIProcessGroup APP_NAME
                WSGIApplicationGroup %{GLOBAL}
                AllowOverride All
        </Directory>

        ...
</VirtualHost>
```

## Credits
Based on this tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

