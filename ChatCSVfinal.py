import streamlit as st

def main():
    st.title("Select Script to Execute")

    selected_script = st.selectbox("Select Script", ["Quering the CSV", "Plot Graph From CSV"])

    if selected_script == "Quering the CSV":
        st.info("Executing Quering the CSV...")
        import try2
        try2.main()
    elif selected_script == "Plot Graph From CSV":
        st.info("Executing Plot Graph From CSV...")
        import tryplot
        tryplot.main()

if __name__ == "__main__":
    main()
