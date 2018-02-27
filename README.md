### requirements

 - python2.7
 - virtualenv
 - postgresql

### run

#### setup postgreSQL locally

Setup process for postgreSQL is out of scope of this document 

#### make and activate virualenv

in the folder with sources: 

```bash
$ virtualenv -p python2.7 .venv
...
$ source .venv/bin/activate
...
$ cd kb_test
```

#### setup instance (with activated virtualenv)

 - configure DB connection  / debug mode via changing kb_test/setting_local.py

 - create required tables
 
    `$ ./manage.py migrate`

 - setup first user account
 
    `$ ./manage.py createsuperuser`

#### run application

```bash
$ ./manage.py runserver
```

You will get application runninig on <http://127.0.0.1:8000/>

**NB: for proper static files (css styles and js code) resolving please do not turning off DEBUG mode.**

**Production deployment is out of scope oof this document.**

#### administration interface

 - default admin interface available via <http://127.0.0.1:8000/admin/>
 - current article list available via <http://127.0.0.1:8000/admin/app/article/>
 - user management available via <http://127.0.0.1:8000/admin/auth/user/>

