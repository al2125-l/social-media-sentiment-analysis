import streamlit as st
import pandas as pd
from textblob import TextBlob

st.title("💬 Social Media Sentiment Analysis")

st.write("Upload a CSV file containing tweets or posts to analyze sentiment.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Sample Data", df.head())

    if 'text' in df.columns:
        df['polarity'] = df['text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        df['sentiment'] = df['polarity'].apply(lambda p: 'Positive' if p > 0 else ('Negative' if p < 0 else 'Neutral'))
        st.write("### Sentiment Results", df[['text', 'sentiment']])
        st.bar_chart(df['sentiment'].value_counts())
    else:
        st.error("CSV must contain a 'text' column.")
else:
    st.info("Upload a file to begin analysis.")
