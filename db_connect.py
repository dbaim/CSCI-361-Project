import config
from pathlib import Path
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text, create_engine


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


eng = get_engine(config.username, config.pwd, config.hostname, config.port_id, config.database)
base = declarative_base()


def init_db():
    filepath = Path('project_db.sql')
    with eng.begin() as conn:
        for query in [x.strip() for x in filepath.read_text().split(';') if x.strip()]:
            conn.execute(text(query))

    print('All tables were created successfully')


def fill_db():
	filepath = Path('mock.sql')

	with engine.connect() as conn:
		for query in [x.strip() for x in filepath.read_text().split(';') if x.strip()]:
			conn.execute(text(query))

	print('All rows were inserted successfully')


init_db()
fill_db()
