import typing as ty

from .protocols import CompareableP

CompareableT = ty.TypeVar("CompareableT", bound=CompareableP)
