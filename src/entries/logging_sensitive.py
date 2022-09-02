import logging
from pathlib import Path

import bunyan
from pydantic import BaseModel, SecretStr, SecretBytes


SECRETS_STORE_DIR = 'secrets-store'


class BaseSecretsModel(BaseModel):
    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value() if v else None,
            SecretBytes: lambda v: v.get_secret_value() if v else None,
        }

class BasicAuth(BaseSecretsModel):
    user: str
    password: SecretStr

class PostgresqlConnectionModel(BaseSecretsModel):
    driver: str
    user: str
    password: SecretStr
    host: str
    port: int
    dbname: str


def main():
    secrets_dir = Path(SECRETS_STORE_DIR)

    credentials = PostgresqlConnectionModel.parse_file(
        secrets_dir.joinpath('postgresql-connection')
    )
    logging.info(
        'Connection to Posgresql database...', 
        extra=credentials.dict()
    )

    credentials = BasicAuth.parse_file(
        secrets_dir.joinpath('web-basicauth')
    )
    logging.info(
        'Authenticating with web service...', 
        extra=credentials.dict()
    )



if __name__ == '__main__':
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = bunyan.BunyanFormatter()
    
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)
    
    main()