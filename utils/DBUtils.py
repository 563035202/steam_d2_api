import mysql.connector


class DBUtils():
    conn = None
    def __init__(self):
        config = {
            'user': 'root',
            'password': '******',
            'host': '127.0.0.1',
            'port': 3306,
            'database': 'mosesdb',
            'charset': 'utf8'
        }
        self.conn = mysql.connector.connect(**config)

    def close(self):
        self.conn.close()
        self.conn = None

    def insertHeros(self, tup):
        lname = tup[0]
        name = tup[1]
        id = tup[2]
        sql = "insert into d2heros(id, `name`, localized_name) values ("+str(id)+",\'"+name+"\',\'"+lname+"\')"
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except Exception, e:
            print e
        finally:
            cursor.close()
        pass

    def insertLeagues(self, tup):
        # league_name, league_id, tournament_url, itemdef, description
        league_name = tup[0]
        league_id = tup[1]
        tournament_url = tup[2]
        itemdef = tup[3]
        description = tup[4]
        sql = "insert into d2leagues(league_name, league_id, tournament_url, itemdef, description) values (\'"+league_name+"\',"+str(league_id)+",\'"+tournament_url+"\',"+str(itemdef)+",\'"+description+"\')"
        print sql
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except Exception, e:
            print e
        finally:
            cursor.close()
        pass

