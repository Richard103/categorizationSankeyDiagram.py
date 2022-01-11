# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go

import warnings
warnings.simplefilter("ignore")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


import random
values_list = [random.randint(0,99) for p in range(0, 16)]
print(values_list)

def get_source(number):
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    df_medals = pd.read_excel("D:/Datasets/Sankey_Diagrams/Medals.xlsx")
    print(df_medals.info())
    df_medals.rename(
        columns={'Team/NOC': 'Country', 'Total': 'Total Medals', 'Gold': 'Gold Medals', 'Silver': 'Silver Medals',
                 'Bronze': 'Bronze Medals'}, inplace=True)
    # df_medals.drop(columns=['Unnamed: 7','Unnamed: 8','Rank by Total'], inplace=True)

    df_medals

    orig_categories = ["Cukrárna", "Kavárna", "Hospoda", "Restaurace", "Čajovna", "Fastfood", "Pizzerie", "Klub", "Bar",
                       "Bistro",
                       "Závodní Jídelna", "Vinárna", "Motorest", "Erotické kluby"]
    new_categories = ["tag_alcohol_label", "tag_servemeal_label", "tag_actnight_label",
                      "tag_enjcoffeesweettea_label"]

    NODES = dict(  # 0                 1                          2        3       4           5
        # label=["United States of America", "People's Republic of China", "Japan", "Gold", "Silver", "Bronze"],
        label=orig_categories[:4]+new_categories[:3],
        color=["seagreen", "dodgerblue", "orange", "gold", "silver", "brown", "yellow", "pink"], )

    LINKS = dict(source=[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3],  # The origin or the source nodes of the link
                 target=[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6],  # The destination or the target nodes of the link
                 value=values_list,  # The width (quantity) of the links
                 # Color of the links
                 # Target Node:    3-Gold          4 -Silver        5-Bronze
                 color=["lightgreen", "lightgreen", "lightgreen",  # Source Node: 0 - United States of America
                        "lightskyblue", "lightskyblue", "lightskyblue",  # Source Node: 1 - People's Republic of China
                        "bisque", "bisque", "bisque"], )  # Source Node: 2 - Japan

    data = go.Sankey(node=NODES, link=LINKS)
    fig = go.Figure(data)
    fig.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
