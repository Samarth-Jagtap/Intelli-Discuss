import streamlit as st
import pandas as pd
from pandasai.llm.google_gemini import GoogleGemini
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
from pandasai import SmartDataframe

# Load environment variables
load_dotenv()

# Retrieve Google API key from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")

if google_api_key is None:
    st.error("Google API key is not set. Please set the environment variable GOOGLE_API_KEY.")
    st.stop()  # Stop the execution if API key is missing

# Function to interact with Gemini and generate plot
def generate_plot(df, prompt):
    gemini = GoogleGemini(api_key=google_api_key)
    pandas_ai = SmartDataframe(df, config={"llm": gemini})
    result = pandas_ai.chat(prompt)

    st.write("Response from Gemini:", result)  # Display the response for debugging

    # Determine plot type and data columns from Gemini's response
    plot_type = "bar" if "bar" in result else "line" if "line" in result else "scatter"
    x_column = "Country or region" if "country" in result else "Date" if "date" in result else None
    y_column = "Score" if "score" in result else None

    # Check if the necessary columns for plotting are found
    if x_column and y_column:
        plt.figure(figsize=(10, 6))
        try:
            if plot_type == "bar":
                df.plot(kind="bar", x=x_column, y=y_column)
            elif plot_type == "line":
                df.plot(kind="line", x=x_column, y=y_column)
            elif plot_type == "scatter":
                df.plot(kind="scatter", x=x_column, y=y_column)

            plt.title("Graph generated based on query: " + prompt)
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            st.pyplot(plt.gcf())  # Correctly display the plot in Streamlit
        except Exception as e:
            st.error(f"An error occurred while plotting: {e}")
    else:
        st.error("Could not determine the columns to plot. Please refine your query.")

# Main function for Streamlit app
def main():
    st.title("CSV Graph Generator")
    st.subheader("Upload your CSV file and plot a graph")
    
    input_csv = st.file_uploader("Upload CSV", type=['csv'])

    if input_csv:
        data = pd.read_csv(input_csv)
        st.success("CSV file uploaded successfully!")
        st.write(data.head())  # Display the first few rows of the DataFrame
        
        user_query = st.text_input("Enter your query")

        if user_query and st.button("Generate Graph"):
            st.info("Processing query...")
            generate_plot(data, user_query)

if __name__ == "__main__":
    main()
