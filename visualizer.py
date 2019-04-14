import pandas as pd


def print_df(alerts):

    print(pd.DataFrame(alerts, columns=["time", "Source IP", "Source Port", "Destination IP", "Destination Port",
                                        "Event", "Classification"]))
