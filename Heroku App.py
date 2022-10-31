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


def fill_patient():
    with eng.connect() as conn:
        dis = conn.execute(text("""
        INSERT INTO patients (dob, iin, patientID, full_name, blood_group, emergency_contact_number, contact_number, email, home_address, marital_status, registration_date, doctorId, username) VALUES
        ('2002-04-10', '023303030', '330303003', 'Aaron Paul', '3P', '87773737373', '83338383', 'dsjd@fenfj.com', 'address', 'single', '2020-02-02', 'user1');
        """))


init_db()
