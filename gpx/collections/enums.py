from enum import Enum


class ActivityType(Enum):
    CYCLING = "cycling"

    @classmethod
    def from_str(cls, activity_type: str):
        activity_type = activity_type.lower()

        return cls(activity_type)
