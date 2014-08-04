pythonservices
==============

Python related web services


Setup Python

Tutorial : https://pypi.python.org/pypi

1. 	Setup Python
	- Install Python : http://www.python.org/download/
	- Setup path variables
		export PYTHON_HOME=C:\Python27
		export PATH=$PYTHON_HOME:$PYTHON_HOME\Scripts:$PATH
	- Setup MinGW compiler for libraries
		https://gist.github.com/mmlin/1059280

2.  Install PyDev in existing eclipse
	http://www.vogella.com/articles/Python/article.html
	eclipse update site: http://pydev.org/updates/
	
3.	Install PIP
	http://www.pip-installer.org/en/latest/installing.html
	$ python ez_setup.py
	$ python get-pip.py
	
4. Libraries
	a.	Boto optional AWS SDK
		$ git clone git://github.com/boto/boto.git
		$ cd boto & python setup.py install
	b. Bottle and Flask
		pip install bottle
		pip install flask
	c. MySQLdb (http://blog.mysqlboy.com/2010/08/installing-mysqldb-python-module.html,  http://sourceforge.net/projects/mysql-python/) 
     Installed an executable version for windows from sourceforge
		$ easy_install MySQL-python
	d. pip install paste
	   pip install unidecode
		
5. Create a database with the *.sql schema file

6. Configure with the db credentials and host name in config.cfg
    py main.py
	
	Test GET: http://localhost:8080/users/
