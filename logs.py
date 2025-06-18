import logging
import logging.config
import os

# using non-root logging
logger = logging.getLogger("data_science_project")


def setup_logging() -> None:
    '''
    Dictionary for setting advanced logging file 
    
    '''
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
                "maxBytes": 100000,
                "backupCount" : 2
            }
        },
        "loggers":{
            "root" : {"level" : "INFO", "handlers" : ["stderr","file"]}
        }
    }

    logging.config.dictConfig(config=logging_config)

def logging_main() -> None:
    if not os.path.exists("logs/"):
        os.makedirs("logs/",exist_ok=True)
    '''
    Function for check if logging is working in logs.py file
    '''
    setup_logging()
    logger.info("Logging in Logs.py setup")
  

if __name__ == "__main__":
    logging_main()