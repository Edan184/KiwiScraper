import psycopg2

# this is just a demo of how to insert data into database 

# replace values with your local postgres values
# wont work with current values

conn = psycopg2.connect(
    host="localhost",
    database="<DB-NAME>",
    user="postgres",
    password="<DB-PASSWORD>")

cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS sayings;
    DROP TABLE IF EXISTS authors;

    CREATE TABLE IF NOT EXISTS authors(
        author_id SERIAL PRIMARY KEY,
        author VARCHAR(50) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS sayings(
        quote_id SERIAL PRIMARY KEY,
        quote VARCHAR(250) NOT NULL,
        author INTEGER references authors(author_id) NOT NULL
    );

    """
)

# dummy data 

quote_authors_mapping = [
    # author, quote
    ('Jeffrey Zeign', 'I am motivational'),
    ('Ziggly Zoogo', 'Never again'),
    ('Zibaba', 'I am Zibaba, you will never see me again'),
    ('Jeffrey Zeign', 'Never too late to start'),
    ('Jeffrey Zeign', 'We do not ever give up!')

]

for row in quote_authors_mapping:
    author_name = row[0]
    quote = row[1]

    cur.execute(
            """
            INSERT INTO authors (author)
            VALUES (%s)
            RETURNING author_id;
            """,
            (author_name, )
        )
    author_id = cur.fetchone()[0]
    cur.execute("INSERT INTO sayings (quote, author) VALUES (%s, %s)", (quote, author_id))


cur.close()
conn.commit()
conn.close()
