import pandas as pd

from ..checks import _check_columns, _check_index, _check_type
from ..core import DataFrame, _wrap


def load(path: str, **kwargs) -> DataFrame:
    _check_type(path, str)
    data = pd.read_csv(path, **kwargs)
    _check_index(data)
    _check_columns(data)
    return _wrap(data)
