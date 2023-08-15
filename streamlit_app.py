import streamlit;
streamlit.title('My better half new Healthy Dinner');

streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg, 🍌🥭 some bananas, mango, graps and cherries 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

fruits_selected=streamlit.multiselect("Pick some fruits:", my_fruit_list , ['Apple','Banana'] )


# Filter the DataFrame based on selected fruits
fruits_to_show = my_fruit_list[my_fruit_list['Fruit'].isin(fruits_selected)]
streamlit.dataframe(fruits_to_show)

