import pandas as pd


def print_df(alerts):

    # print(pd.DataFrame(alerts, columns=["time", "Source IP", "Source Port", "Destination IP", "Destination Port",
    #                                    "Event", "Classification"]))

    plopper_df = pd.DataFrame(alerts, columns=["time", "Source IP", "Source Port", "Destination IP", "Destination Port",
                                        "Event", "Classification"])

    return plopper_df
