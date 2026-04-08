import configparser
import mysql.connector
config=configparser.ConfigParser()
config.read("C:\\Users\\91741\\PycharmProjects\\BackEnd _Testing\\API_DataDriven_MYSQL\\Utilities\\configuration.ini")
def create_book_url():
    base_url=config.get("API","base_url")
    cb_url=config.get("API","createbook_endpoint")
    return base_url+cb_url
def delete_book_url():
    base_url=config.get("API","base_url")
    db_url=config.get("API","deletebook_endpoint")
    return base_url+db_url
def getconnection():
    host=config.get("SQL","host")
    user=config.get("SQL","user")
    password=config.get("SQL","password")
    database=config.get("SQL","database")
    return mysql.connector.connect(host=host,user=user,password=password,database=database)
def payload_details_db():
    conn=getconnection()
    cursor=conn.cursor()
    cursor.execute("select * from Books")
    row=cursor.fetchone()
    conn.close()
    return row
def createbook_payload():
    data=payload_details_db()
    create_payload = {

        "name": data[0],
        "isbn": data[1],
        "aisle": data[2],
        "author": data[3]
    }
    return create_payload
def deletebook_payload(id):
    delete_payload = {

        "ID": id

    }
    return delete_payload