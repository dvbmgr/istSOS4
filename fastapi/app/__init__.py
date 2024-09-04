import os

HOSTNAME = os.getenv("HOSTNAME", "http://localhost:8018")
SUBPATH = os.getenv("SUBPATH", "/istsos4")
VERSION = os.getenv("VERSION", "/v1.1")
DEBUG = int(os.getenv("DEBUG"), 0)
VERSIONING = os.getenv("VERSIONING", "false") == "true"
POSTGRES_DB = os.getenv("POSTGRES_DB", "istsos")
POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "database")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
PG_MAX_OVERFLOW = int(os.getenv("PG_MAX_OVERFLOW", 0))
PG_POOL_SIZE = int(os.getenv("PG_POOL_SIZE", 10))
PG_POOL_TIMEOUT = float(os.getenv("PG_POOL_TIMEOUT", 30))
COUNT_MODE = os.getenv("COUNT_MODE", "FULL")
COUNT_ESTIMATE_THRESHOLD = int(os.getenv("COUNT_ESTIMATE_THRESHOLD", 10000))
TOP_VALUE = int(os.getenv("TOP_VALUE", 100))
PARTITION_CHUNK = int(os.getenv("PARTITION_CHUNK", 10000))
EXPAND_MODE = os.getenv("EXPAND_MODE", "BASIC")
