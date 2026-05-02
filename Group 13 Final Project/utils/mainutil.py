import numpy as np
import pandas as pd

def to_ts(data, dates=None):
    data = data.copy()
    aDict = {'ts': np.array(data)}
    aRange = np.arange(len(data))
    aDict['pts'] = (aRange - np.min(aRange)) / np.max(aRange)
    if dates is not None:
        indexDates = pd.to_datetime(dates, errors='coerce')
    elif isinstance(data, pd.Series) and isinstance(data.index, pd.DatetimeIndex):
        indexDates = data.index
    else:
        indexDates = aRange
    return pd.DataFrame(aDict, index=indexDates).dropna()
