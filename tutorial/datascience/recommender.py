import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

column_names = ['user_id', 'item_id', 'rating', 'timestamp']

df = pd.read_csv('u.data', sep='\t', names=column_names)

print(df.head())

movie_titles =  pd.read_csv('Movie_Id_Titles')

df = pd.merge(df, movie_titles, on='item_id')

print(df.head())

sns.set_style('white')

print(df.groupby('title')['rating'].mean().sort_values(ascending=False))


print(df.groupby('title')['rating'].count().sort_values(ascending=False))


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

ratings['num_of_ratings'] = df.groupby('title')['rating'].count()
print(ratings)

ratings['num_of_ratings'].hist(bins=70)
plt.show()

ratings['rating'].hist(bins=70)
plt.show()

sns.jointplot(x='rating', y='num_of_ratings', data=ratings, alpha=0.5)

plt.show()

moviemat = df.pivot_table(index='user_id', columns='title', values='rating')

print(moviemat.head())

print(ratings.sort_values('num_of_ratings', ascending=False))

starwars_user_ratings = moviemat['Star Wars (1977)']
liar_liar_user_ratings = moviemat['Liar Liar (1997)']

print(starwars_user_ratings.head())

print(liar_liar_user_ratings.head())


similar_to_star_wars = moviemat.corrwith(starwars_user_ratings)
similar_to_liar_liar = moviemat.corrwith(liar_liar_user_ratings)


cor_starwars = pd.DataFrame(similar_to_star_wars, columns=['Correlation'])
cor_starwars.dropna(inplace=True)

print(cor_starwars.head())

cor_starwars = cor_starwars.join(ratings['num_of_ratings'])

print(cor_starwars.head())

corr_filtered = cor_starwars[cor_starwars['num_of_ratings'] > 100].sort_values('Correlation', ascending=False).head()

print(corr_filtered.head())

cor_liar_liar = pd.DataFrame(similar_to_liar_liar, columns=['Correlation'])
cor_liar_liar .dropna(inplace=True)

cor_liar_liar = cor_liar_liar.join(ratings['num_of_ratings'])
cor_liar_liar_filtered = cor_liar_liar[cor_liar_liar['num_of_ratings'] > 100].sort_values('Correlation', ascending=False).head()

print(cor_liar_liar_filtered)

