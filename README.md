# Intelli-Discuss

This repository provides a step-by-step guide and a template for setting up an advanced document analysis and query system. It processes both PDFs and CSVs, enabling efficient extraction, search, and visualization of information.

Last update: June 26th, 2024

## Table of Contents

- [Motivation](https://github.com/RamiKrispin/lang2sql#motivation)
- [System Architectures](https://github.com/Samarth-Jagtap/Intelli-Discuss#system-architectures)[
- [System Requirements](https://github.com/Samarth-Jagtap/Intelli-Discuss?tab=readme-ov-file#system-architectures)
- [Running the Code](https://github.com/Samarth-Jagtap/Intelli-Discuss?tab=readme-ov-file#running-the-code)
- [Summary](https://github.com/RamiKrispin/lang2sql#summary)
- [Resources](https://github.com/RamiKrispin/lang2sql#resources)
  
# System Architectures

### 1. General Architecture

Our system is designed to seamlessly process user input, leveraging advanced language model (LLM) capabilities and backend processing to enhance user interaction. 

Here's a step-by-step breakdown of how it works:
  
- **User Input:** Users engage with the platform by entering text messages or posts in the designated input field.

- **LLM Processing:** Once the input is received, the Language Learning Model (LLM) takes over to:
  
  - **Enhance the content:** Improve the quality, clarity, and coherence of the user's input.
  - **Generate creative text formats:** Create unique and engaging text formats, such as stories, poems, or formatted responses.
  - **Provide Informative Responses:** Offer insightful and contextually relevant replies based on the platform's specific requirements.
    
- **Backend Processing:** The processed input is then sent to the backend for further actions, including:
  - **Data Storage:** Storing the message or post in a secure database for future reference or analysis.
  - **Content Analysis:** Analyzing the content for sentiment, trends, or other relevant metrics.
  - **Content Moderation:** Filtering or moderating the content to ensure it meets community guidelines and standards.

- **Frontend Update:** The frontend dynamically updates to reflect the user's input and any actions taken by the backend. This ensures a seamless and responsive user experience.
  
- **Generated Response:** The LLM might generate a response to the user's input, which is then displayed on the frontend. This response could be:
  - **Informative:** Providing useful information, answers to questions, or relevant suggestions.
  - **Creative:** Offering unique and engaging content, enhancing user interaction and engagement.

<figure>
<img src="images/ChatPDF Architectiure.png" width="100%" align="center"/></a>
<figcaption> Figure 1 - General Architecture describing the main function </figcaption>
</figure>
<br>
<br />


# System Requirements:

Before installing Intelli-Discuss, ensure your system meets the following hardware and software prerequisites:

### 1. Hardware Requirements:

- Minimum of 8 GB RAM (16 GB recommended for large datasets)
- At least 10 GB of free disk space
- Modern multi-core processor

### 2. Software Requirements:

- Operating System: Windows 10 or later, macOS 10.15 or later, Linux (Ubuntu18.04 or later)
- Python 3.8 or later
- PostgreSQL 12 or later
- pip (Python package installer)

# Running the Code.

### 1. Installing Dependencies: 

First, you need to install the required dependencies. Intelli-Discuss relies on several Python packages that need to be installed in your environment.
- Ensure you are in the root directory of the ’intelli-discuss’ repository.
- It is recommended to create a virtual environment to manage dependencies:
- To create a virtual environment type this in your terminal
```
   python -m venv <name_of_environment>
```
- Make sure to check if the created environment is activated or not 

### 2. Install the required packages using ’pip’:

Install the necessary dependencies by running:

```
pip install -r requirements.txt
```
- This command will read the ’requirements.txt’ file and install all the necessary dependencies for Intelli-Discuss.

### 3. Setting Up Environment Variables: 

Intelli-Discuss requires certain environment variables to be set up for proper configuration. 

Follow these steps to configure them:

- Copy Past a `.env` file in the root directory of the project.
- Add the necessary environment variables to the `.env` file. Replace the placeholder values with your actual configuration details.
- Load the environment variables in your application. This is typically done automatically when you run the application, as the code uses libraries like ’dotenv’ to load these variables.

Once the environment variables are set up, your Intelli-Discuss environment is configured and ready to use.

# Final Steps

After completing the setup, follow these steps to finalize and run your project:

### 1. Copy and Paste Code Files

Ensure the following code files are copied into your project directory:

- `try2.py`
- `tryplot.py`
- `ChatCSVfinal.py`
- `app1.py`
- `Main.py`

### 2. Copy Logo Files

Also, ensure that all logo files are copied into the appropriate directory in your project.

### 3. Save All Files

Make sure all the copied files are saved properly in your project directory.

### 4. Run the Program

To run the whole program successfully, execute the following command:

 ```
 Streamlit run Main.py
```

 This command will start the Streamlit application and allow you to interact with your project.

