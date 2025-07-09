from typing import List

import pymysql.cursors
from dbutils.pooled_db import PooledDB
from models.user import UserModel
from utils.config import Config


class MySQL:
    def __init__(self) -> None:
        config = Config.DB
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=10,
            mincached=2,
            maxcached=5,
            maxshared=3,
            blocking=True,
            maxusage=None,
            ping=1,
            host=config.HOST,
            database=config.DATABASE,
            user=config.USER,
            password=config.PASSWORD,
            cursorclass=pymysql.cursors.DictCursor,
        )

    def create_user(self, user: UserModel):
        sql = """
            INSERT INTO users (id, first_name, last_name, email, username, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            user.id,
            user.first_name,
            user.last_name,
            user.email,
            user.username,
            user.password,
        )

        conn = self.pool.connection()
        try:
            with conn.cursor() as cursor:
                affected_rows = cursor.execute(sql, params)
            conn.commit()
        finally:
            conn.close()

        return affected_rows

    def get_all_user(self) -> List[UserModel]:
        sql = "SELECT * FROM users"
        conn = self.pool.connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                records = cursor.fetchall()
        finally:
            conn.close()

        return [UserModel(**record) for record in records]

    def get_user(self, id=None, username=None) -> UserModel | None:
        if id:
            sql = "SELECT * FROM users WHERE id = %s"
            params = (id,)
        elif username:
            sql = "SELECT * FROM users WHERE username = %s"
            params = (username,)
        else:
            raise Exception("id or username must be specified!")

        conn = self.pool.connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                record = cursor.fetchone()
        finally:
            conn.close()

        if record is None:
            return None
        return UserModel(**record)
