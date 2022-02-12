from src.configs.sentry import STAGE, SENTRY_DSN
from src.helpers.logger import log


def init_sentry_sdk(sentry_dsn=SENTRY_DSN):
    if sentry_dsn is not None:
        import sentry_sdk
        from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

        sentry_sdk.init(
            dsn=sentry_dsn,
            environment=STAGE,
            # This automatically reports all uncaught exceptions from lambda functions
            integrations=[AwsLambdaIntegration()],
            # This allows us to capture User PII such as user ids, usernames,
            # cookies, authorization headers, IP addresses if present
            send_default_pii=True,
        )
    else:
        log.warning("Missing Sentry DSN from enviroment variables.")
