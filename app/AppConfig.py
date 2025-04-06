from config.Config import Env


class AppConfig:
    """Base flask app config"""

    DEBUG = False
    TESTING = False  # dead: disable
    # Add any shared configurations here


class DevAppConfig(AppConfig):
    """Development config."""

    DEBUG = True
    # Add development-specific configurations


class QaAppConfig(AppConfig):
    """Development config."""

    DEBUG = True
    # Add development-specific configurations


class ProductionConfig(AppConfig):
    """Production config."""

    DEBUG = False
    # Add production-specific configurations


class TestingConfig(AppConfig):
    """Testing config."""

    DEBUG = True
    TESTING = True  # dead: disable
    # Add testing-specific configurations


# Config dictionary to map environment names to config classes
_config_by_name: dict[Env, AppConfig] = {
    Env.DEV: DevAppConfig(),
    Env.QA: QaAppConfig(),
    Env.PROD: ProductionConfig(),
    Env.TEST: TestingConfig(),
}


def get_config_by_name(name: Env) -> AppConfig:
    return _config_by_name[name]
