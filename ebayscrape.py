import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(df):
    plt.plot(df['month'], df['average_price'])
    plt.xlabel('Month')
    plt.ylabel('Average Price')
    st.pyplot()

def main():
    st.title("Average Price Over Time")
    file = st.file_uploader("Upload your file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        plot_graph(df)

if __name__ == '__main__':
    main()

