# Movie Recommendation System

This project implements a machine learning-driven web page that recommends Hollywood movies using cosine similarity predictions. The recommendation system provides a comprehensive list of over **4500+ movies**, ranked from highest to least recommended based on their similarity scores.

## Features

- Utilizes cosine similarity to calculate the similarity between movies and generate accurate recommendations.
- Provides a wide range of movie recommendations from the extensive collection of 4500+ Hollywood movies.
- Offers a user-friendly web interface powered by the Streamlit framework.
- Implements data preprocessing techniques to ensure accurate and relevant recommendations.
- Makes use of libraries such as Pandas, Difflib, Pickle, and Streamlit to facilitate the implementation.

## Installation

1. Clone the repository.
2. Install the required dependencies by running the command `pip install -r requirements.txt`.

## Usage

1. Ensure that the dataset and model files are in the correct location.
2. Run the application using the command `streamlit run app.py`.
3. Access the application through the provided URL in the console.

## How It Works

1. The movie recommendation system preprocesses the movie dataset to extract relevant features.
2. The cosine similarity algorithm is applied to calculate the similarity between movies based on these features.
3. The system generates a comprehensive list of recommendations, sorted from the highest to the least recommended.
4. If a user enters a wrong movie name, the system automatically corrects it using Difflib and recommends favorite movies.
5. The Streamlit framework facilitates the creation of a user-friendly web interface to interact with the recommendation system.

## Screenshots

![Screenshot 1](https://github.com/yashmangal112/Movies_Recommendation/assets/104120843/867f907b-9d59-4d4a-9fcb-3a93e6c81a07)
![Screenshot 2](https://github.com/yashmangal112/Movies_Recommendation/assets/104120843/a7b5f595-78fc-4dc5-ae6b-0a2ca69b4733)
> Sample screenshot showing the movie recommendation web page.


![Screenshot 3](https://github.com/yashmangal112/Movies_Recommendation/assets/104120843/53cb1a46-95d5-446f-8515-c2696e3723ce)
> Automatically corrects wrong movie names and recommends favorite movies.


## Acknowledgements

This project makes use of the following libraries and frameworks:

- **Pandas**: Data manipulation and preprocessing.

- **Difflib**: String similarity calculation.
- **Pickle**: Model loading and saving.
- **Streamlit**: Web application framework for user interface development.

---

Thank you for visiting our movie recommendation system! We hope you find it useful and enjoy discovering new favorite movies. If you have any questions or suggestions, please feel free to reach out.
