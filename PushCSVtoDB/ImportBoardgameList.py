import psycopg2

conn = psycopg2.connect("host='nutty-custard-apple.db.elephantsql.com' dbname=ouvnaciy port=5432 user=ouvnaciy password='7Zs2dJTdfUAuUBqAh-_H8QUMOsqR6m3o'")
cur = conn.cursor()
with open('DistinctGames.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    #next(f)  # Skip the header row.
    cur.copy_from(f, '"Collections_boardgame"', sep='|', columns=('"Name"','"BGGRef"'))
    
conn.commit()