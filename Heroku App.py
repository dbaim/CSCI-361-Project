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
    filepath = Path('db_init.sql')
    with eng.begin() as conn:
        for query in [x.strip() for x in filepath.read_text().split(';') if x.strip()]:
            conn.execute(text(query))

    print('All tables were created successfully')


@click.command(name='view doctor info')
def query_1(name):
    with eng.connect() as conn:
        dis = conn.execute(text("""
        SELECT D.login, D.name, D.degree
        FROM Doctor D 
        WHERE D.name = '{name}'
        """)).mappings()
    print([{column: dcode[column] for column in dis.keys()} for dcode in dis])


init_db()