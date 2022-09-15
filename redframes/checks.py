from __future__ import annotations

from .types import Columns, LazyColumns, PandasIndex, Any, PandasRangeIndex, PandasDataFrame


def _check_type(argument: Any, against: type | set[type | None]):
    if isinstance(against, set):
        if len(against) == 0:
            against = {against}  # type: ignore
    if not isinstance(against, set):
        against = {against}
    optional = None in against
    just_types = against.difference({None})
    checks = [isinstance(argument, t) for t in just_types]  # type: ignore
    if optional:
        checks += [argument == None]
    if not any(checks):
        str_types = " | ".join([t.__name__ for t in just_types])  # type: ignore
        if optional:
            str_types += " | None"
        raise TypeError(f"must be {str_types}")


def _check_keys(columns: LazyColumns | None, against: Columns | PandasIndex):
    if isinstance(columns, str):
        columns = [columns]
    columns = [] if (columns == None) else columns
    bad_keys = set(columns).difference(against)  # type: ignore
    if bad_keys:
        if len(bad_keys) == 1:
            raise KeyError(f"invalid key {bad_keys}")
        else:
            raise KeyError(f"invalid keys {bad_keys}")


def _check_index(df: PandasDataFrame):
    if not (df.index.name == None):
        raise IndexError("must be unnamed")
    if not isinstance(df.index, PandasRangeIndex):
        raise IndexError("must be range")
    if not (df.index.start == 0):
        raise IndexError("must start at 0")
    if not (df.index.step == 1):
        raise IndexError("must step by 1")


def _check_columns(df: PandasDataFrame):
    if not isinstance(df.columns, PandasIndex):
        raise KeyError("must be flat")
    if df.columns.has_duplicates:
        raise KeyError("must not contain duplicate keys")
