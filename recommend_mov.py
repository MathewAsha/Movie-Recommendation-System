import pickle
import pandas as pd

with open('movies_list.pkl', 'rb') as file:
    new_data = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)


def recommand(movies):
    index=new_data[new_data['Title']==movies].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    #print("Here are some of the recommended movie options!")
    movie_list = []
    for i in distance[0:5]:
        movie_list.append(new_data.iloc[i[0]].Title)
    return movie_list
