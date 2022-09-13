from __future__ import annotations

from ...types import PandasDataFrame, PandasGroupedFrame, Column, Func

def summarize(
    df: PandasDataFrame | PandasGroupedFrame,
    over: dict[Column, tuple[Column, Func]],
) -> PandasDataFrame:
    if not isinstance(over, dict):
        raise TypeError(
            "into_over_funcs type is invalid, must be dict[str, tuple[str, Callable[..., Any]]]"
        )
    if isinstance(df, PandasGroupedFrame):
        df = df.agg(**over)
        df = df.reset_index()
    else:
        df = df.agg(**into_over_funcs)  # type: ignore
        df = df.T  # type: ignore
        df = df.reset_index(drop=True)  # type: ignore
        df = df.fillna(method="ffill")  # type: ignore
        df = df.fillna(method="bfill")  # type: ignore
        df = df.head(1)  # type: ignore
    return df
