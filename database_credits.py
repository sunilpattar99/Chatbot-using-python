import mysql.connector

def credit(firstname,lastname,email,password,contact_no,plan ):

    data = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password="",
        database = "chatbot_final"
    )

    cur = data.cursor()
    qq = "insert into user (firstname,lastname,email,password,contact_no,plan) values (%s,%s,%s,%s,%s,%s)"
    cur.execute(qq , (firstname,lastname,email,password,contact_no,plan))
    data.commit()






