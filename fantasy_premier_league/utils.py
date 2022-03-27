from datetime import datetime


class Utils:
    @staticmethod
    def parse_utc_datetime(datetime_str: str) -> datetime:
        isoformat_datetime = datetime_str.replace('Z', '+00:00')
        return datetime.fromisoformat(isoformat_datetime)

    @staticmethod
    def format_datetime_as_utc(datetime: datetime) -> str:
        return datetime.isoformat().replace('+00:00', 'Z')