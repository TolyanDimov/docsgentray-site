from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    app_name: str = 'DocsGenTray API'
    secret_key: str = 'change-me'
    jwt_algorithm: str = 'HS256'
    access_token_minutes: int = 60
    database_url: str = 'postgresql+psycopg2://postgres:postgres@db:5432/docsgentray'
    redis_url: str = 'redis://redis:6379/0'
    admin_email: str = 'admin@example.com'


settings = Settings()
