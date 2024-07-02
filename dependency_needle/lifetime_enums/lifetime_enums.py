from enum import Enum


class LifeTimeEnums(Enum):
    """Life time enums used when registering an interface."""

    # New object for each dependant class.
    SCOPED = "scoped"
    # Same object for each dependant class across a single request.
    TRANSIENT = "transient"
    # Same object for each dependant class for any request.
    SINGLETON = "singleton"
    # New object received in time of instantiation.
    JUST_IN_TIME = "just_in_time"
