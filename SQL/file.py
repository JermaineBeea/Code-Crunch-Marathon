import subprocess

script = """ sqlite3 crime_database.db .dump > data_base.sql"""

subprocess.run(script, shell =True, executable='/bin/bash')