import logging
import logging.config
import os

logger = logging.getLogger("my_app")
def setup_logging():
 
    logging_config = {
        "version" : 1,
        "disable_existing_loggers": False,
        "filters": {},
        "formatters":{
            "simple" : {
                "format" : "%(asctime)s - %(levelname)s - %(message)s",
            },
            "detailed" : {
                "format" : "[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s : %(message)s",
                "datefmt" : "%Y-%m-%dT%H:%M:%S"
            }
        },
        "handlers":{
            "stderr":{
                "class":"logging.StreamHandler",
                "level" : "WARNING",
                "formatter": "simple",
                "stream" : "ext://sys.stderr",
            },
            "file": {
                "class" : "logging.handlers.RotatingFileHandler",
                "level" : "INFO",
                
                "formatter" : "detailed",
                "filename": "logs/data.log",
                "maxBytes": 10000,
                "backupCount" : 2
            }
        },
        "loggers":{
            "root" : {"level" : "INFO", "handlers" : ["stderr","file"]}
        }
    }
    logging.config.dictConfig(config=logging_config)

def main() -> None:
    setup_logging()
    logger.debug("Hello Debug here")
    logger.info("Hello info here")
    logger.critical("Hello criitcal here")
    logger.error("Errorhere")

if __name__ == "__main__":
    main()