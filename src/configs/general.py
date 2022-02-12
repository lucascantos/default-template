import os

DOMAIN = os.environ.get("DOMAIN", "localhost")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

"""
Log Levels:
10: DEBUG
20: INFO
30: WARNING
40: ERROR
50: CRITICAL
"""
