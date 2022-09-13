from __future__ import annotations

from ...types import PandasDataFrame, PandasGroupedFrame, Column

def rank(
    df: PandasDataFrame | PandasGroupedFrame,
    column: Column,
    into: Column,
    descending: bool = False,
) -> PandasDataFrame:
    df = df.copy()
    df[into] = df[column].rank(method="dense", ascending=not descending)
    return df
