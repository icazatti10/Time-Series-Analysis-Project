from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

def residual_plot(residual, lags: int, title: str, xlabel: str = "Date", ylabel:str = "Residual"):
    plt.figure(figsize=(12,4))
    plt.plot(residual)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

    fig, axs = plt.subplots(1, 2, figsize=(14, 5))

    plot_acf(residual, lags=lags, ax=axs[0])
    axs[0].set_title("ACF of Residual")

    plot_pacf(residual, lags=lags, ax=axs[1], method="ywm")
    axs[1].set_title("PACF of Residual")

    plt.tight_layout()
    plt.show()