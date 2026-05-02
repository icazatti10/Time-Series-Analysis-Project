import matplotlib.pyplot as plt


def ts_plot(x, y, title: str, xlabel: str, ylabel: str, figsize=(12, 4)):
    fig = plt.figure(figsize=figsize)
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(False)
    plt.show()

    return fig
