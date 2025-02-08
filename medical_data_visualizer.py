
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1  importing the data from medical_examination.csv
df = pd.read_csv("medical_examination.csv")
# print(df)


# 2 calculating the overweight and add the overwight column

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 3 ."""Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1"""

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars = ['cardio'], value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index()
    

    # 7
    df_cat = df_cat.rename(columns = {0: 'total'})
    graph = sns.catplot(data = df_cat, kind = 'bar', x = 'variable', y = 'total', hue = 'value', col = 'cardio')



    # 8
    fig = graph.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()


    # 13
    mask = np.triu(np.ones_like(corr,dtype = bool))



    # 14
    fig, ax  = plt.subplots(figsize = (16,10))

    # 15

    sns.heatmap(corr,mask = mask, square = True, linewidths = 0.5, annot = True, fmt = "0.1f")


    # 16
    fig.savefig('heatmap.png')
    return fig
