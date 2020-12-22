# SAOL wordlist extractor
#   Exploit that the .obb file from SAOL Android app is a
#   SQLite database to extract a wordlist
import sqlite3
import sys

create_table_query = '''
                     CREATE TEMPORARY TABLE t_wordlist(c_word VARCHAR);
                     INSERT INTO t_wordlist SELECT compact FROM saol_wcs
                     WHERE word="";
                     INSERT INTO t_wordlist SELECT word FROM saol_wcs
                     WHERE (word!="")
                     AND (word NOT LIKE "-%")
                     AND (word NOT LIKE "%-");
                     '''
select_column_query = 'SELECT DISTINCT c_word FROM t_wordlist'

print('acquiring wordlist...')
cursor = sqlite3.connect(sys.argv[-1]).cursor()
cursor.executescript(create_table_query)
result = cursor.execute(select_column_query)

print('writing wordlist to file...')
with open('./output/saol_wordlist.txt', 'w') as f:
    [f.write(row[0].upper()+'\n') for row in result]
print('done.')
