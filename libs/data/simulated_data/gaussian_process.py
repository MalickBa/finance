import pandas as pd


def gaussian_return_with_autocorrel(n_assets=20, volatility=0.1, time_scale=0.5):
    """
    Modeling asset prices
    :param n_assets: number of assets to simulate
    :param volatility: volatility level
    :param time_scale: auto-correlation time scale
    :return:
    """
    date_ranges = pd.date_range(datetime.datetime(1996, 1, 1), datetime.datetime(2018, 1, 1), freq='B')
    n_days = len(date_ranges)
    year = 252.
    sigma = volatility / sqrt(year)
    name_assets = ['asset_' + str(n + 1) for n in range(n_assets)]
    mu = pd.Series(0.05 * rand(n_assets) / year, index=name_assets)
    dB = pd.DataFrame(randn(n_days, n_assets), columns=name_assets, index=date_ranges)
    dB = dB.ewm(time_scale).mean()
    dB /= dB.std()
    ret = mu + sigma * dB
    return ret
