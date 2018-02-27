import MySQLdb
import time

while True:
    db = MySQLdb.connect("localhost", "mauro", "12345", "temps")
    curs = db.cursor()
    try:
        curs.execute("""INSERT INTO thetemps values(0, CURRENT_DATE(), NOW(), 28)""")
        db.commit()
        print "Data commited"
    except:
        print "Error"
        db.rollback()
        db.close()
        time.sleep(1)
