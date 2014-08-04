__author__ = 'Rahul Vishwakarma'

import json
import MySQLdb
from bottle import route,request
import ConfigParser

# Initializing the configuration
config = ConfigParser.ConfigParser()
config.read('config.cfg')

username = config.get("mysqld", "user")
password = config.get("mysqld", "pass")
hostname = config.get("mysqld", "host")
portnum = config.get("mysqld", "port")
dbname = config.get("mysqld", "dbname")

print 'Loaded configuration for mysql @ '+ hostname+':'+portnum

# Get connection for the db operations
def getDbConnection():
    try:
        mysql = MySQLdb.connect(user=username,passwd=password,
                            db=dbname,host=hostname)
        return mysql.cursor()
    except MySQLdb.Error, e:
        print "MySQL Error %d:  %s" % ( e.args[0], e.args[1] )

# Curl testing command
# curl -s http://localhost:8080/users
@route('/users', method='GET')
def getallusers():
    try:
        mysql_cursor = getDbConnection()
        args = 'SELECT `user_id`,`user_name`,`first_name`,`last_name`,`email`,`password`,`organization`,`enabled`,`phone` FROM `data`.`user`';
        mysql_cursor.execute(args)
        results=mysql_cursor.fetchall()
    except MySQLdb.Error, e:
        print "MySQL Error %d:  %s" % ( e.args[0], e.args[1] )
    result = json.dumps(results, default=lambda o: o.__dict__)
    return result


# Curl testing command
# curl -s http://localhost:8080/users/2
@route('/users/:userid', method='GET')
def getuser(userid):
    try:
        mysql_cursor = getDbConnection()
        args = 'SELECT `user_id`,`user_name`,`first_name`,`last_name`,`email`,`password`,`organization`,`enabled`,`phone` FROM `data`.`user` WHERE `user_id`=%s' % (userid)
        # args = "CALL getUser('%s');" % (userid)
        mysql_cursor.execute(args)
        results=mysql_cursor.fetchall()
    except MySQLdb.Error, e:
        print "MySQL Error %d:  %s" % ( e.args[0], e.args[1] )
    result = json.dumps(results, default=lambda o: o.__dict__)
    return result


# Curl command for testing:
# curl -s -F "uname=rhltest" -F "fname=rahul" -F "lname=vishwakarma" -F "email=rvk@gmail.com" -F "password=rv" -F "organization=luhar" -F "enabled=1" -F "phone=134524"  http://localhost:8080/users
@route('/users', method='POST')
def createUser():
    name = request.forms.uname
    firstname = request.forms.fname
    lastname = request.forms.lname
    email = request.forms.email
    password = request.forms.password
    organization = request.forms.organization
    enabled = request.forms.enabled
    phone = request.forms.phone

    if name and firstname and password and email and phone :
        try:
            mysql_cursor = getDbConnection()
            #args = "CALL createUser('%s','%s','%s','%s','%s');" % (name , userid , password , email , language)
            args = "INSERT INTO `data`.`user` (`user_name`,`first_name`,`last_name`,`email`,`password`,`organization`,`enabled`,`phone`) VALUES('%s','%s','%s','%s','%s','%s','%s','%s') ;" % (name , firstname, lastname , email, password, organization, enabled, phone)
            mysql_cursor.execute(args)
            mysql.commit();
        except MySQLdb.Error, e:
            print "MySQL Error %d:  %s" % ( e.args[0], e.args[1] )
            if mysql:
                mysql.rollback()

        if mysql:
            mysql.close()

        return "Sucesfully inserted"

# Curl command for testing:
# curl -X UPDATE -F "uname=rhltest" -F "fname=rahul" -F "lname=vishwa" -F "email=rv@gmail.com" -F "password=rv" -F "organization=luhar" -F "enabled=1" -F "phone=134524" http://localhost:8080/users/2
#
@route('/users/:userid', method='UPDATE')
def updateUser(userid):
    name = request.forms.uname
    firstname = request.forms.fname
    lastname = request.forms.lname
    email = request.forms.email
    password = request.forms.password
    organization = request.forms.organization
    enabled = request.forms.enabled
    phone = request.forms.phone

    if name and firstname and password and email and phone :
        try:
            mysql_cursor = getDbConnection()
            # args = "CALL updateUser('%s','%s','%s','%s','%s');" % (name , userid , password , email , language)
            args = "UPDATE `data`.`user` SET `user_name` = '%s', `first_name` = '%s',`last_name` = '%s', `email` = '%s',`password` = '%s',`organization` = '%s', `enabled` = '%s', `phone` = '%s' WHERE `user_id` = '%s';" % (name , firstname, lastname , email, password, organization, enabled, phone, userid)
            mysql_cursor.execute(args)
            mysql.commit();
        except MySQLdb.Error, e:
            print "MySQL Error %d:  %s" % ( e.args[0], e.args[1] )
            if mysql:
                mysql.rollback()

        if mysql:
            mysql.close()

        return "Sucesfully updated"


# Curl testing command
# curl -X DELETE  http://localhost:8080/users/testuser543fd-p
@route('/users/:userid', method='DELETE')
def deleteuser(userid):
    try:
        mysql_cursor = getDbConnection()
        args = "DELETE FROM `data`.`user` WHERE `user_id` = '%s';" % (userid)
        mysql_cursor.execute(args)
        mysql.commit();
    except MySQLdb.Error, e:
        print "MySQL Error %d:  %s" % ( e.args[0], e.args[1] )
        if mysql:
            mysql.rollback()

    if mysql:
        mysql.close()

    return "Successfully deleted"

