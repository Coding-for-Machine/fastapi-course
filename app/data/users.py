import os
from typing import Optional
import asyncpg
from dotenv import load_dotenv

load_dotenv()

async def connact_db():
    await asyncpg.conncat
async def create_user_table(conn):
    pass
    """
    CREATE TABLE IF NOT EXIST users (
        id SERIAL PIRAMERY KEY,
        email VARCHAR(250) UNIQUE NOT NULL,
        password TEXT CHECK (password>8),
        first_name VARCHAR(250) NOT NULL,
        last_name VARCHAR(250) NOT NULL,
        is_active BOOLEIAN DEFAULT TRUE,
        is_staf BOOLEIAN DEFAULT FALSE,
        is_supper BOOLEIAN DEFAULT FALSE,
        is_delete BOOLEIAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

async def create_user_profile_table(conn):
    pass


async def main():
    pass

import asyncio
asyncio.run(main())