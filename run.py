from app import create_app, logger
from config import config, Env

app = create_app(config.ENV)

if __name__ == '__main__':
    logger.info("Project config:", config.__dict__)
    logger.debug("Hello")
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=(config.ENV != Env.PROD)
    )
    print("server started on port %s...", config.PORT)
