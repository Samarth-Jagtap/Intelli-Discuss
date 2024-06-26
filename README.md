# Intelli-Discuss

This repository provides a step-by-step guide and a template for setting up an advanced document analysis and query system. It processes both PDFs and CSVs, enabling efficient extraction, search, and visualization of information.

Last update: June 26th, 2024

## Table of Contents

- [Motivation](https://github.com/RamiKrispin/lang2sql#motivation)
- [Scope and General Architecture](https://github.com/RamiKrispin/lang2sql#scope-and-general-architecture)
- [System Requirements](https://github.com/Samarth-Jagtap/Intelli-Discuss?tab=readme-ov-file#system-requirements)
- [Running the Code](https://github.com/Samarth-Jagtap/Intelli-Discuss?tab=readme-ov-file#running-the-code)
- [Summary](https://github.com/RamiKrispin/lang2sql#summary)
- [Resources](https://github.com/RamiKrispin/lang2sql#resources)
  
# System Architecture

### 1. General Architecture

#### User Input: Users enter text messages or posts in the designated input field.

#### LLM Processing: The user's input is processed by the LLM to potentially:

- Enhance the content.
- Generate creative text formats.
- Provide informative responses based on the platform's context.

#### Backend Processing: The user's input is sent to the backend for:

- Storing the message or post in a database.
- Analyzing the content for sentiment or other purposes.
- Filtering or moderating content if necessary.

#### Frontend Update: 

The frontend is updated to reflect the user's input or any actions taken on the backend.

#### Generated Response: 

The LLM might generate a response to the user's input, which could be displayed in the frontend. This response could be informative or creative, depending on the LLM's configuration and the platform's design.

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

