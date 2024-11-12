import pytz
from datetime import datetime, timedelta

class TimeZoneAdjustment:
    def __init__(self, config):
        self.config = config

    def adjust_time(self):
        local_datetime = self.config.get_local_datetime()
        timezone = pytz.timezone(self.config.timezone)
        now = timezone.localize(local_datetime)
        if self.config.dst_start <= now <= self.config.dst_end:
            now += timedelta(hours=1)
        return now