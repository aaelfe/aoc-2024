#!/usr/bin/env python3
"""Base utilities for project scripts."""

import sys
import logging
from typing import Callable
from functools import wraps

def setup_logging(name: str) -> logging.Logger:
    """Configure and return a logger instance."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(name)

def script_handler(func: Callable) -> Callable:
    """Decorator to handle common script operations and error handling."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = setup_logging(func.__module__)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            sys.exit(1)
    return wrapper