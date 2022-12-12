import logging
from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "uvicorn.logging.DefaultFormatter",
                "fmt": "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "default": {
                "formatter": "default", "class": "logging.StreamHandler", "stream": "ext://sys.stderr"
            }
        },
        "loggers": {
            "fastapi_crud_router": {
                "handlers": ["default"],
                "level": "DEBUG"
            }
        }
    }
)

logger = logging.getLogger("fastapi_crud_router")
