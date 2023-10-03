class GpxStatsException(Exception):
    pass


class InvalidFile(Exception):
    def __str__(self) -> str:
        return "The provided filename is not a valid GPX-file."
