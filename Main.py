import streamlit as st
from PIL import Image
import app1
import ChatCSVfinal

# Set the page config for the entire app
st.set_page_config(page_title='Intelli-Discuss', layout='wide', initial_sidebar_state='expanded')

# Custom CSS to adjust the sidebar and main content
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            padding-top: 1rem; /* Adjust the top padding to move content up */
        }
        .main-content {
            padding: 2rem;
        }
        .main-content h1 {
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
        }
        .main-content p, .main-content ul {
            font-size: 1.2rem;
            text-align: justify;
            margin-bottom: 1.5rem;
        }
        .main-content ul {
            padding-left: 2rem;
        }
        .about-section {
            margin-top: 2rem;
            font-size: 1rem;
            text-align: justify;
        }
        .about-section h3 {
            text-align: center;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Intelli-Discuss")

# Insert image at the top of the sidebar
image = Image.open("Logo.png")
st.sidebar.image(image, caption='Intelli-Discuss', use_column_width=True)

# Radio buttons to choose the application
app_option = st.sidebar.radio(
    "Choose an application",
    ("Home", "Chat with PDF Documents", "CSV ChatApp")
)

if app_option == "Home":
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.markdown('<h1>Welcome to the Intelli-Discuss </h1>', unsafe_allow_html=True)
    st.markdown("""
        <p>This application offers multiple tools to help you with different tasks:</p>
        <ul>
            <li><strong>Chat with PDF Documents</strong>: Upload a PDF and chat with an AI about its content.</li>
            <li><strong>CSV ChatApp</strong>: Upload a CSV file and interact with its data through an AI.</li>
        </ul>
        <p>Use the sidebar to navigate between these tools.</p>
    """, unsafe_allow_html=True)

    # About Section
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<h3>About</h3>', unsafe_allow_html=True)
    st.markdown("""
        <p>This application was developed by Vishal Ranjan and Samarth Jagtap. 
        For more information, visit our <a href="https://github.com/your-repo" target="_blank">GitHub</a>.</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif app_option == "Chat with PDF Documents":
    # Run the app module
    app1.main()

elif app_option == "CSV ChatApp":
    # Run the app module
    ChatCSVfinal.main()

else:
    st.write("Invalid selection")
