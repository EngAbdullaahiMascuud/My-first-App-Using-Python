import sqlite3,os
class data:
    def __init__(self):
        self.create_table()
        pass
    def get_path(self):
        path1=os.path.abspath(__file__)
        path1=path1[:-7]+"Data.db"
        if not os.path.exists(path1):
            open(path1,"a")
        con=sqlite3.connect(path1)
        cur=con.cursor()
        return con,cur
    def create_table(self):
        con,cur=self.get_path()
        try:
            cur.execute("create table users (userid varhar(50) not null,pin varchar(4) not null)")
            con.commit()
        except:
            pass


    def insert_table(self,user,pin):
        con,cur=self.get_path()
        cur.execute("insert into users values(?,?)",(user,pin,))
        con.commit()
    def get_user(self,User):
        con,cur=self.get_path()
        cur.execute("select * from users where userid=? ",(User,))
        for i in cur:
            return i[0],i[1]
        return False,False




# x=data()
# x.insert_table("","")
