from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_db: str
    postgres_username: str
    postgres_password: str
    postgres_host: str = "db"
    postgres_port: str = "5432"
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"

    @property
    def connection_string(self):
        return "".join(
            (
                "postgresql://",
                f"{self.postgres_username}:{self.postgres_password}@",
                f"{self.postgres_host}:{self.postgres_port}/",
                f"{self.postgres_db}",
            )
        )


settings = Settings()
