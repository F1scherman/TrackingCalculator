import psycopg2
class cADB():
    """A class for managing the calculator ads database"""
    def __init__(self):
        self._conn = psycopg2.connect("dbname=calculatorAds user=postgres password=postgres")
        self._cur = self._conn.cursor()
        self._currentUser = 1

    def update(self, column):
        """Column should specify which operation is being updated"""
        self._cur.execute('SELECT '+ column +' FROM public."userLog" WHERE "UserID" = %s;',(self._currentUser,))
        temp = self._cur.fetchone()[0] + 1
        self._cur.execute('UPDATE public."userLog" SET ' + column + '= %s WHERE "UserID" = %s;',(temp , self._currentUser))
        self._conn.commit()

    def get(self):
        self._cur.execute('SELECT ("pi","tan","log","ln","e","roots","sin") FROM public."userLog" WHERE "UserID" = %s;',(self._currentUser,))
        return self._cur.fetchone()[0]
    
    def __del__(self):
        self._conn.commit()
        self._cur.close()
        self._conn.close()

