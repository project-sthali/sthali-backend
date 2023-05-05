from asyncpg import create_pool

from config import CONFIG, DBConfig


class Database:
    @staticmethod
    async def create_pg_pool(config: DBConfig):
        pg_pool = await create_pool(host=config.host,
                                    port=config.port,
                                    user=config.username,
                                    password=config.password,
                                    database=config.database,
                                    min_size=1,
                                    max_size=5)
        return pg_pool

    def __init__(self, config: DBConfig) -> None:
        self.pool = self.create_pg_pool(config)


DB = Database(CONFIG.db)
