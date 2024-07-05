#!/usr/bin/env python3
"""A module that defines a `filter_datum()` function."""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Obfuscates a log message.
    Args:
        fields: All fields to obfuscate.
        redaction: The field that will be obfuscated.
        message: A log line.
        separator: A character that separates all fields in the log line.
    """
    pattern: str = f'({"|".join(fields)})=[^{separator}]+'
    replacement: str = fr"\1={redaction}"
    obfuscated_msg: str = re.sub(pattern, replacement, message)
    return (obfuscated_msg)
