import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

formats = {
    "url": "%Y-%m-%dT%H:%M",
    "dashed": "%Y-%m-%d-%H-%M",
    "default": "%Y-%m-%d %H:%M",
    "br": "%d/%m/%Y %H:%M",
    "de": "%d.%m.%Y %H:%M",
    "date_br": "%d/%m/%Y",
    "date_de": "%d.%m.%Y",
    "date_default": "%Y-%m-%d",
}


def date_string(dt=datetime.utcnow(), format: str = "default"):
    """
    Returns datetime in a string format chosen by default names or custom
    :params dt: datetime input
    :params format: format of string
    """
    if format in formats:
        format = formats[format]
    else:
        format = format
    try:
        return dt.strftime(format)
    except Exception as e:
        raise ValueError(e)


def normalize_timestamp(timestamp: str):
    """
    Split a timestamp and return datetime.strptime.
    :params timestamp: string of format YYY-mm-dd HH:MM
    """
    headers = ["year", "month", "day", "hour", "minute"]
    splitted = re.split("-|:| |T", timestamp)
    splitted = [int(i) for i in splitted]
    if len(headers) != len(splitted):
        if len(splitted) == 3:
            splitted.extend([12, 0])
        else:
            raise ValueError("wrong string format")
    return datetime(**dict(zip(headers, splitted)))


def to_datetime(timestamp: str, format: str = "url"):
    """
    Converts timestamp string to datetime
    :params timestamp: string with datetime format
    :params format: string with format. If format is None, it will try all formats
    """
    if format is not None:
        return datetime.strptime(timestamp, formats[format])
    else:
        dt = None
        for format_string in formats.values():
            try:
                return datetime.strptime(timestamp, format_string)
            except ValueError:
                # Such unsighty usage of try/except
                pass
    raise ValueError(f"Could not find a format for the input {timestamp}")


def relative_date(**kwargs):
    """
    Return a datetime relative to UTC now
    :params kwargs: args of the relative_delta function. eg. hours=2
    """
    now = datetime.utcnow()
    return now + relativedelta(**kwargs)