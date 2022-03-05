
import pandas as pd 
df = pd.read_csv('raw_extract.csv')
#print(df)
df_new = df.groupby('subreddit')['title'].apply('. '.join)
#print(df_new)
df_new.to_csv('grouped_subreddits.csv', mode='a', header=True)

