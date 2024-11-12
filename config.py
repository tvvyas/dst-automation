from datetime import datetime

class Configuration:
    def __init__(self):
        self.timezone = ""
        self.dst_start = ""
        self.dst_end = ""
        self.notification_preferences = []

    def set_configuration(self, timezone, dst_start, dst_end, notification_preferences):
        self.timezone = timezone
        self.dst_start = dst_start
        self.dst_end = dst_end
        self.notification_preferences = notification_preferences

    def get_local_datetime(self):
        return datetime.now()