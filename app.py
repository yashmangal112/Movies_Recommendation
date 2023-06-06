import numpy as np
import pandas as pd
import streamlit as st
import pickle
import difflib
from sklearn.metrics.pairwise import cosine_similarity



#loading the saved model
similarity = pickle.load(open('C:/Users/hp/Desktop/movie_model_deployment/movies_prediction.sav', 'rb'))

movies_data = pd.read_csv('C:/Users/hp/Desktop/movie_model_deployment/movies.csv')
list_of_all_titles = movies_data['title'].tolist()

def prediction(movie_name):
    # movie_name = input(' Enter your favourite movie name : ')
  
    
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if find_close_match: 
        close_match = find_close_match[0]

        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

        similarity_score = list(enumerate(similarity[index_of_the_movie]))

        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

        # print('Movies suggested for you : \n')
        st.success('Movies suggested for you :')
        return sorted_similar_movies

    else: 
        st.error("This movie is not in our huge database.\nPlease find another movie", icon='🚨')
        # return ("This movie is not in our database.  \nPlease find another movie")





def main():
        # st.balloons() 
        st.title('Favorite Movie Recommandation System')
        input = 'Enter A Hollywood Movie Name'
        bold_input = f'**{input}**'
        movie_name = st.text_input(bold_input)
        j = st.number_input('Number of movies you want', min_value=1, max_value=4803, value=30, format='%.2i')
        # st.success('The current number is {j}')

        

        #& code for prediction
        title_from_index = ""

        #Creating a button

        if st.button('find movies'):
             if movie_name == "":
                  st.warning('please enter a hollywood movie', icon='⚠️')
             else:     
                title_from_index = prediction(movie_name)
             
             if title_from_index: 
                 st.balloons()  
                 i=1
                 for movie in title_from_index:
                     index = movie[0]
                     title_from_index = movies_data[movies_data.index==index]['title'].values[0]
                    # return title_from_index
                     if i<=j:
                         st.write(i, '.', title_from_index)
                         # st.success(i)
                         i+=1

            #  else:
            #      st.error("This movie is not in our database.\nPlease find another movie", icon='🚨')                         


if __name__ == '__main__':
     main()
