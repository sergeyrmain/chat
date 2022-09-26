from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PORT: int = Field(env='PORT', default=8000)
    SERVER: str = Field(env='SERVER', default='')
    FORMAT: str = Field(env='FORMAT', default='utf-8')
    BUFFER_SIZE: int = Field(env='BUFFER_SIZE', default=1024)



settings = Settings()
