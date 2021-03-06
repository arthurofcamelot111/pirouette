from collections import namedtuple
import sqlite3


class Data:

    def __init__(self):
        self._data = dict.fromkeys(
                        [str(i) for i in range(0, 101)],
                        None
                        )

    def load(self, database_filename):
        conn = sqlite3.connect(database_filename)
        cur = conn.cursor()

        for row in cur.execute("SELECT * FROM tblNumber"):
            number = row[0]
            self._data[number] = dict()
            d = self._data[number]
            d["number"] = number
            d["is_master"] = row[1] is "TRUE"
            d["meaning"] = row[2]
            d["tarot"] = row[3]

        for row in cur.execute("SELECT * FROM tblColor"):
            number = row[0]
            d = self._data[number]
            d["color"] = row[1]
            d["hex"] = row[2]
            d["rgb"] = tuple(row[3:6])

        for row in cur.execute("SELECT * FROM tblMusicKeys12"):
            number = row[0]
            d = self._data[number]
            d["music_note"] = row[1]
            d["octave_freq"] = row[2:]
    
    def get_data(self, number, attribute):
        return self._data[number][attribute]
