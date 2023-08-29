from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
        "    )
        """   

        CURSOR.excute(sql)   

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.excute(sql, (self.name, self.album)) 
        
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]   

  
    