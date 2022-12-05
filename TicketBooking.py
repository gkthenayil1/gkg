# streamlit run C:\Users\Admin\OneDrive\Documents\TicketBooking.py
import streamlit as st
import pandas as pd
import numpy as np
st.title('TicketBooking')

global f
f = 0
screen_list=["screen1","screen2"]
movie_list=["churuli","kochal"]
pandas_movie_list=pd.Series(movie_list)
timing_list=["12.00 : 02:45","03.00 : 05.45","06.00 : 08.45"]
pandas_timing_list=pd.Series(timing_list)
pandas_row_list=pd.Series(['A','B','C','D','E','F','G','H'])
pandas_seat_list=pd.Series(['1','2','3','4','5','6','7','8','9','10'])

#this movie function is used to select movie name
def movie():
	global f
	f = f+1
	st.write("which movie do you want to watch?")
	for i in range(len(movie_list)):
		st.write(i+1," :  "+ movie_list[i])
	
	
	
	
	
	
movie()
#movies = int(st.number_input("choose your movie: "))
movies=st.selectbox("choose your movie: ", pandas_movie_list)
#movies=int(movies)
#x = ds[ds == 11].index[0]
st.write("The movie is in", screen_list[pandas_movie_list[pandas_movie_list==movies].index[0]] )	

st.write("At what timing do you want to watch")	

time=st.selectbox("choose your time: ", pandas_timing_list)

st.write("In which row do you want to watch")	
rows=st.selectbox("choose your row: ", pandas_row_list)
st.write("How many seats do yo want to book")	
no_seats=st.selectbox("number of seat: ", [1,2,3])
seat_list=[]
st.write("please select your seat")
for j in pandas_seat_list:
	
	#selected_seat=st.number_input(f"seat number-{j}", min_value=1, max_value=20,  step=1)
	st.columns(1)
	selected_seat = st.checkbox(j)
	if selected_seat:
		seat_list.append(j)
st.write("YOU have selected following seats in row ", rows)
for j in seat_list:
	st.write(j)



