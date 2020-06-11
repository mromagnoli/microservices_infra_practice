from typing import Optional


class Config:
    """Base config."""

    SECRET_KEY: Optional[str] = None
    DEBUG: bool = False
    TESTING: bool = False
