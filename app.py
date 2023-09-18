import streamlit as st
import pickle
from utils import preprocessing_text

st.set_page_config(
    page_title="IMDB Review Sentiment Analysis",
    page_icon=":rocket:"
)

if 'model' not in st.session_state:
    model = pickle.load(open('model.sav', 'rb'))
    st.session_state['model'] = model

st.title('IMDB Review Sentiment Analysis')

review = st.text_area('Text to analyze', 
                     "")

if st.button('Analyze'):
    review_prep = preprocessing_text(review)
    result = st.session_state['model'].predict([review_prep])
    if result.tolist()[0] == 0:
        result = 'Neutral or Positive Review'
    else:
        result = 'Negative Review'
    st.write('Sentiment:', result)
else:
    st.write('waiting')