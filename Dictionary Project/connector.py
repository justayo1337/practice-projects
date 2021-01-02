import mysql.connector

con = mysql.connector.connect(

user='ardit700_student',
password='ardit700_student',
host="108.167.140.122",
database="ardit700_pm1database"
)

class connector():
    def __init__(self):
        self.cursor = con.cursor()
        
    def getWord(self,w):
    
        query= self.cursor.execute(f"Select definition from Dictionary where expression='{w}' ")
        results=self.cursor.fetchall()

        print(results)
