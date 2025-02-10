from sqlalchemy import create_engine
import os
from pathlib import Path
from dotenv import load_dotenv

# 環境変数の読み込み
# load_dotenv()
base_path = Path(__file__).parents[1] #backendディレクトリへのパス
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)


# データベース接続情報
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

#SSL証明書のパス
ssl_cert = str("DigiCertGlobalRootG2.crt.pem")

# MySQLのURL構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(f"Attempting to connect to: {DATABASE_URL}")

# エンジンの作成
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl":{
            "ssl_ca": ssl_cert
        }
    },
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600
)
