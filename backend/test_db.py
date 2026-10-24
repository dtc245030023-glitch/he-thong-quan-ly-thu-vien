
from sqlalchemy import text
from database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        print("KET NOI POSTGRESQL THANH CONG!")
        print(result.scalar())
except Exception as error:
    print("KET NOI THAT BAI!")
    print(error)
