from typing import Optional

from typing_extensions import TypeVar

T = TypeVar("T")


def required(obj: dict, key: str, default: Optional[T] = None, message: Optional[str] = None) -> T:  # dead: disable
    """
    Check if a key is present in the dictionary and has a non-null value.
    If the key is not present or has a null value, raise an exception with the provided message.
    """
    if key not in obj or obj[key] is None:
        if default is not None:
            return default
        raise ValueError(message or f"Field {key} cannot be null in {obj.__class__}")
    return obj[key]


def optional(obj: dict, key: str, default: Optional[T] = None) -> Optional[T]:  # dead: disable
    """
    Check if a key is present in the dictionary and has a non-null value.
    If the key is not present or has a null value, return the default value.
    """
    if key not in obj or obj[key] is None:
        return default
    return obj[key]
