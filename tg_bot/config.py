# tg_bot/config.py

import os
from tg_bot.sample_config import Config as BaseConfig


class Config(BaseConfig):
    # ===== REQUIRED =====
    API_KEY = os.environ.get("TOKEN")

    OWNER_ID = 6618789194
    OWNER_USERNAME = "kouxik1"

    # ===== DATABASE (DISABLED as requested) =====
    SQLALCHEMY_DATABASE_URI = None

    # ===== BASIC SETTINGS =====
    LOAD = []
    NO_LOAD = [
        "rss",
        "translation",
    ]

    WEBHOOK = False
    URL = None

    PORT = 5000

    # ===== OPTIONAL =====
    SUDO_USERS = [6618789194]
    SUPPORT_USERS = []
    WHITELIST_USERS = []

    WORKERS = 4
    STRICT_GBAN = False
    DEL_CMDS = False
    ALLOW_EXCL = True


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
