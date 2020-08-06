from youtube_search import YoutubeSearch
import pandas as pd
import matplotlib.pyplot as plt

def getData(text):
    results = YoutubeSearch(text, max_results=120).to_dict()
    df = pd.DataFrame(results)
    df = df.drop(df.columns[[0, 1]], axis=1)
    df['url_suffix'] = 'https://www.youtube.com' + df['url_suffix'].astype(str)
    views = [str(i).split()[0] for i in df['views']]
    views2 = []
    for i in views:
        t= ''
        for j in i:
            if j.isdigit():
                t+=j
        views2.append(int(t))
    df['views'] = views2
    return df

def sortData(df,by,ascending):
    return df.sort_values(by=by,ascending=ascending)

