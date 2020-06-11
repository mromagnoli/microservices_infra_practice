from .dev_env import DevelopmentConfig, TestingConfig

CONFIGS = {
    "production": None,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}
