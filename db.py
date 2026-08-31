from sqlalchemy import create_engine, URL
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="2zGuyjMPQR3qiFF.root",
    password="zO0zhbO228oLdT09",
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    port=4000,
    database="test",
    query={
        "ssl_verify_cert": "true",
        "ssl_verify_identity": "true",
    }
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


try:
    with engine.connect() as connection:
        print("DATABASE CONNECTED SUCCESSFULLY!")

except Exception as e:
    print("DATABASE CONNECTION FAILED:")
    print(e)