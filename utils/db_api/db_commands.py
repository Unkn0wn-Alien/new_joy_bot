from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from config import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL UNIQUE,
        username varchar (255) NULL,
        language varchar (255) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT NOW()
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, telegram_id, username, language, created_at):
        sql = "INSERT INTO users (telegram_id, username, language, created_at) VALUES ($1, $2, $3, $4) RETURNING *"
        return await self.execute(sql, telegram_id, username, language, created_at, fetchrow=True)

    async def update_user_language(self, language_user, telegram_id):
        sql = "UPDATE users SET language=$1 WHERE telegram_id=$2"
        return await self.execute(sql, language_user, telegram_id, execute=True)

    async def select_language(self, telegram_id):
        sql = "SELECT language FROM users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def select_telegram_id(self):
        sql = "SELECT telegram_id FROM users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
