import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega3 & blueberry Oatmeal')
streamlit.text('🥗 kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled Free_Range Egg') 
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:",list(my_fruits_list.index))
streamlit.dataframe(my_fruit_list)

