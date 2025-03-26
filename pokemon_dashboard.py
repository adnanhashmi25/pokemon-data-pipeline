import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Pokémon data
CSV_FILE = "pokemon_data.csv"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CSV_FILE)
        return df
    except FileNotFoundError:
        st.error("⚠ Pokémon data file not found. Run the ETL script first!")
        return pd.DataFrame()  # Return an empty DataFrame if file is missing

# Streamlit UI
st.title("🐉 Pokémon Data Dashboard")

def dashboard():
    df = load_data()

    if not df.empty:
        # Display Data Table
        st.subheader("📊 Pokémon Data Table")
        st.write(df)

        # Filters
        st.sidebar.header("🔍 Filter Pokémon")
        search_name = st.sidebar.text_input("Search by Name")
        min_height = st.sidebar.slider("Minimum Height", min_value=int(df["height"].min()), max_value=int(df["height"].max()), value=int(df["height"].min()))
        max_height = st.sidebar.slider("Maximum Height", min_value=int(df["height"].min()), max_value=int(df["height"].max()), value=int(df["height"].max()))

        filtered_df = df[
            (df["name"].str.contains(search_name, case=False, na=False)) &
            (df["height"] >= min_height) &
            (df["height"] <= max_height)
        ]

        st.write(filtered_df)

        # Chart: Height vs Weight
        st.subheader("📈 Height vs. Weight Distribution")
        fig, ax = plt.subplots()
        ax.scatter(df["height"], df["weight"], alpha=0.5)
        ax.set_xlabel("Height")
        ax.set_ylabel("Weight")
        ax.set_title("Pokémon Height vs. Weight")
        st.pyplot(fig)

    else:
        st.warning("⚠ No data available. Run the ETL process first!")

