import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)


def addComment(id, date, ticker, post, body, sentiment):
    try:
        post = post[3:]
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO comments VALUES (?, ?, ?, ?, ?, ?)",(id, date, ticker, post, body, sentiment))
        con.commit()
    except Exception as e:
        pass

def addPost(id, comment_count, date):
    try:
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO posts VALUES (?, ?, ?)",(id, comment_count, date))
        con.commit()
    except:
        pass

def addTicker(ticker):
    try:
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute("INSERT INTO stocks VALUES (?)",([ticker]))
        con.commit()
    except:
        pass


def checkTicker(ticker):
    ticker = ticker.upper()
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("SELECT COUNT(1) FROM stocks WHERE ticker = ?",([ticker]))
    con.commit()
    val = cursorObj.fetchone()[0]
    if(val == 0):
        return False
    return True
    
def checkComment(id):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("SELECT COUNT(1) FROM comments WHERE comment_id = ?",([id]))
    con.commit()
    val = cursorObj.fetchone()[0]
    if(val == 0):
        return False
    return True

def checkPost(id):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("SELECT COUNT(1) FROM posts WHERE post_id = ?",([id]))
    con.commit()
    val = cursorObj.fetchone()[0]
    if(val == 0):
        return False
    return True

def getCommentCount(id):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("SELECT comment_count FROM posts WHERE post_id = ?",([str(id)]))
    con.commit()
    val = cursorObj.fetchone()[0]
    return val
