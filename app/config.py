from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Declare the parameters for the environment variables"""

    # database_name: str
    # database_hostname: str
    # database_port: str
    # database_username: str
    # database_password: str
    database_url:str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: str

    class Config:
        """Import the values to the parameters from the .env file"""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
