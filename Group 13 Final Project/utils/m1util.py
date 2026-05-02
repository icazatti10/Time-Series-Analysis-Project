from statsmodels.gam.api import BSplines


def get_spline(pts, df=10, degree=3, **kwargs):
    if isinstance(df, int):
        df = [df]
    if isinstance(degree, int):
        degree = [degree]
    return BSplines(pts, df=df, degree=degree, **kwargs)
