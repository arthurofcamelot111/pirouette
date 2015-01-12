from collections import namedtuple
import sqlite3


class Data:

	def __init__(self):
		self._data = dict.fromkeys(
				[str(i) for i in range(0, 101)],
				dict()
				)

	def load(self, database_filename):
		conn = sqlite3.connect(database_filename)
		cur = conn.cursor()

		for row in cur.execute("SELECT * FROM tblNumber"):
			number = row[0]
			d = self._data[number]
			d["is_master"] = bool(row[1])
			d["meaning"] = row[2]
			d["tarot"] = row[3]

		for row in cur.execute("SELECT * FROM tblColorMusic12"):
			number = row[0]
			d = self._data[number]
			d["color"] = row[1]
			d["color_hex"] = row[2]

		for row in cur.execute("SELECT * FROM tblMusicKeys12"):
			number = row[0]
			d = self._data[number]
			d["music_note"] = row[1]
			d["octave_freq"] = row[2:]
	
	def get_data(self, number, attribute):
		return self._data[number][attribute]



from pprint import pprint
'''
data = Data()
data.load("correspondences.db")
for i in range(0,101):
	for attr in ('is_master', 'meaning', 'tarot', 'color', 'color_hex', 'music_note', 'octave_freq'):
		d = data.get_data(str(i), attr)
		print(attr, end=': ')
		print(d, end=', ')
	print()
'''
data = Data()
data.load("correspondences.db")
pprint(data._data['9'])