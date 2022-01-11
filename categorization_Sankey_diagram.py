# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go

import warnings
warnings.simplefilter("ignore")


import random


def get_source(orig, target):
    source = []
    num = 0
    for i in range(len(orig)):
        for j in range(len(target)):
            source.append(num)
        num += 1
    return source

def get_target(orig, target):
    target_list = []
    for i in range(len(orig)):
        num = len(orig_categories)
        for j in range(len(target)):
            target_list.append(num)
            num += 1
    return target_list

def value_list(df, orig_cats, new_cats):
    lst = []
    output = []
    for col in new_cats:
        for cat in orig_cats:
            lst.append(len(recaba[((recaba.Category == cat) & (recaba["%s" % col] == 1))]["PremiseID"]))
    print("list: ", lst)
    steps = len(new_cats)
    long = len(lst) // len(new_cats)
    for i in range(0,long):
        for step in range(0, steps):
            output.append(lst[i+step*long])
    print("output: ", output)
    return output

def nodes_colors(orig_cats, new_cats, colors):
    num_origs = len(orig_cats)
    num_news = len(new_cats)
    clrs = []
    num_nodes = num_origs + num_news
    for i in range(1, num_nodes+1):
        clrs.append(colors[-i])
    return clrs

def link_colors(orig_cats, new_cats, colors):
    num_origs = len(orig_cats)
    num_news = len(new_cats)
    clrs = []
    num_nodes = num_origs * num_news
    for i in range(0, num_nodes):
        clrs.append(colors[i])
    return clrs

if __name__ == '__main__':

    named_colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue",
                    "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgrey", "darkgreen",
                    "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey",
                    "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro",
                    "ghostwhite", "gold", "goldenrod", "gray", "grey", "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush",
                    "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgrey", "lightgreen", "lightpink", "lightsalmon",
                    "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon",
                    "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred",
                    "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod",
                    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue",
                    "rebeccapurple", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow",
                    "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]

    service_columns = ["tag_servetogo_label",  "tag_genfood_label", "tag_smallrefresh_label", "tag_delivery_label"]

    enjoy_columns = ["tag_enjsweet_label", "tag_enjcoffee_label", "tag_enjtea_label", "tag_enjcockatails_label", "tag_enjwine_label", "tag_enjbeer_label"]

    activity_columns = ["tag_actnight_label", "tag_adult_label", "tag_actallday_label"]


    df = pd.read_excel("D:/SharpGrid/Categorization/OnTradeModel.xlsx")

    orig_categories = df[df.RootCategory == "ReCaBa"].Category.unique().tolist() # ["Cukrárna", "Kavárna", "Hospoda", "Restaurace", "Čajovna", "Fastfood", "Pizzerie", "Klub", "Bar", "Bistro", "Závodní Jídelna", "Vinárna", "Motorest", "Erotické kluby"]
    new_categories = enjoy_columns # [col for col in df.columns if 'tag_enj' in col]

    recaba = df[df.RootCategory == "ReCaBa"]
    # values_list = [random.randint(0, 99) for p in range(0, len(orig_categories) * len(new_categories))]
    # print("values_list: ", values_list)

    NODES = dict(  # 0                 1                          2        3       4           5
        # label=["United States of America", "People's Republic of China", "Japan", "Gold", "Silver", "Bronze"],
        label=orig_categories+new_categories,
        color=nodes_colors(orig_categories, new_categories, named_colors)) #["seagreen", "dodgerblue", "orange", "gold", "silver", "brown", "yellow", "hsl(71%,60%,19%)"], )

    LINKS = dict(source=get_source(orig_categories, new_categories),  # The origin or the source nodes of the link
                 target=get_target(orig_categories,new_categories),  # The destination or the target nodes of the link
                 value=value_list(recaba, orig_categories, new_categories),  # The width (quantity) of the links
                 # Color of the links
                 # Target Node:    3-Gold          4 -Silver        5-Bronze
                 color=link_colors(orig_categories, new_categories, named_colors)) #["lightgreen", "lightgreen", "lightgreen",  # Source Node: 0 - United States of America
                        #"lightskyblue", "lightskyblue", "lightskyblue",  # Source Node: 1 - People's Republic of China
                        #"bisque", "bisque", "bisque"], )  # Source Node: 2 - Japan

    data = go.Sankey(node=NODES, link=LINKS)
    fig = go.Figure(data)
    fig.update_layout(title="Rozpad kategorií do Ocassions", font_size=13, width=1150, height=750)
    fig.update_traces(valueformat='3d', selector=dict(type='sankey'))
    fig.update_layout(hoverlabel=dict(bgcolor="lightgray", font_size=16, font_family="Rockwell"))
    fig.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
