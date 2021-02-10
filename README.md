<h1>Django Project - Board, Signup, Login, Logout</h1>

<h2>Description</h2>
This is a Django framework-based project was created for individuals to implement bulletin boards, sign up, logins, and logouts.

<h2>Technology<h2>
<ul>
  <li>Framework: Django 2.0.13, boostrap 4
  <li>Language: Pyhone 3.7
  <li>Database: SQLite3(dev), MySQL(prod)
  <li>OS: Window10
  <li>IDE: PyCharm community version
  <li>Library: requirements.txt
</ul>
 <h2>Directory Structure</h2>

<pre>
BLOG
    accounts
    blog
        settings.py
        urls.py
        wsgi.py
    blogapp
    static
    templates <br>
.gitignore
main.py
manage.py
requirements.txt
</pre>

<h2>Execution</h2>
<b font-size:30px>Repogitory Clone</b>
<pre>
$ git clone https://github.com/wjsgur8530/Board.git
</pre>

<b font-size:30px>Install PIP</b>
<pre>
$ pip install -r requirements.txt
</pre>

<b font-size:30px>Running Virtual Environment</b>
<pre>
$ #create env
$ cd env
$ cd Scripts
$ activate
</pre>

<b font-size:30px>DATABASE</b>
<pre>
# blog/settings.py SQLite3
Use: SQLite3

# blog settings.py MySQL
Use Mysql: Change name, ID, password, port
</pre>

<b font-size:30px>DB Migration</b>
<pre>
$ py manage.py makemigrations
$ py manage.py migrate
</pre>

<b font-size:30px>Create Superuser</b>
<pre>
$ py manage.py createsuperuser
</pre>

<b font-size:30px>Runserver</b>
<pre>
$ py manage.py runserver
</pre>

<h2>License</h2>
<ul>
  <li>Copyright 2021 JeonHyuk
</ul>
