import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)




# st.title("Streamlit tuto !")
# st.markdown('''
# # Les commandes
# Bonjour,
# Cette page a été créée pour vous montrer en direct l'effet des commandes de base. 
# **Par exemple**, vous verrez ci-dessous le code utilisé pour afficher ces premières lignes.
# ''')

# st.code('''
# import streamlit as st

# st.title("Streamlit tuto !")
# st.markdown(\'\'\'
# # Les commandes
# Cette page a été créée pour vous montrer en direct l'effet des commandes de base. 
# **Par exemple**, vous verrez ci-dessous le code utilisé pour afficher ces premières lignes.
# \'\'\')
# ''')


# col1, col2 = st.columns([3,1])
# with col1:
#     st.markdown("## A large column ! I can display so many things")
# with col2:
#     st.markdown("Wow it's a small one 😢")
#     st.image(img, width = 200)

# st.code('''
# from PIL import Image
# img = Image.open('bender.png')
# col1, col2 = st.columns([3,1])
# with col1:
#     st.markdown("## A large column ! I can display so many things")
# with col2:
#     st.markdown("Wow it's a small one 😢")
#     st.image(img, width = 200)
# ''')