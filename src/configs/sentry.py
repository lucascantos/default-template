import os

STAGE = os.environ.get("STAGE", "development")
SENTRY_DSN = os.environ.get("SENTRY_DSN")
