# Intelli-Discuss

This repository provides a step-by-step guide and a template for setting up an advanced document analysis and query system. It processes both PDFs and CSVs, enabling efficient extraction, search, and visualization of information.

Last update: June 27th, 2024

# Table of Contents

- [Motivation](https://github.com/RamiKrispin/lang2sql#motivation)
- [System Architectures](https://github.com/Samarth-Jagtap/Intelli-Discuss#system-architectures)
- [System Requirements](https://github.com/Samarth-Jagtap/Intelli-Discuss?tab=readme-ov-file#system-architectures)
- [Running the Code](https://github.com/Samarth-Jagtap/Intelli-Discuss?tab=readme-ov-file#running-the-code)
- [Summary](https://github.com/RamiKrispin/lang2sql#summary)
- [Resources](https://github.com/RamiKrispin/lang2sql#resources)
  
# Motivation

The rapid growth of digital documents in various formats, such as PDFs and CSVs, has led to an increased need for tools that can efficiently process and extract valuable information from these sources. Traditional methods of manually extracting and analyzing data are time-consuming and often inefficient. 

**Intelli-Discuss** was created to address these challenges by providing a robust and user-friendly application that leverages advanced AI and machine learning techniques to automate the process of document interaction and data visualization. Our motivation for developing Intelli-Discuss includes:

1. **Enhanced Document Interaction**: To provide users with the ability to easily upload, process, and interact with PDFs and CSVs, transforming static documents into dynamic, queryable data sources.

2. **Time Efficiency**: To save users time by automating the extraction of meaningful information from large volumes of text and data, enabling quick and accurate responses to user queries.

3. **Improved Accessibility**: To make complex data accessible and understandable to a broader audience, including those without specialized technical skills, through natural language queries and intuitive visualizations.

4. **Integration of Advanced Technologies**: To integrate cutting-edge technologies such as semantic search using embeddings, contextual response generation, and data visualization, showcasing the power and potential of AI in practical applications.

5. **Facilitating Data-Driven Decision Making**: To empower users to make informed decisions based on accurate and timely information extracted from their documents, enhancing productivity and effectiveness in various fields, including business, research, and education.

By developing Intelli-Discuss, we aim to bridge the gap between advanced AI capabilities and everyday document interaction, providing a powerful tool that meets the evolving needs of users in the digital age.



# System Architectures

## 1. General Architecture

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
<img src="images/General Architectiure.png" width="100%" align="center"/></a>
<figcaption> Figure 1 - General Architecture describing the main function </figcaption>
</figure>
<br>
<br />

## 2. Workflow for Processing and Analyzing PDFs

Our system allows for efficient handling of multiple PDFs, extracting, chunking, and processing the text to provide meaningful responses to user queries. Here's an interactive overview of how this process works:

- **Step 1: Input/Upload PDFs**
  
  Users can upload multiple PDF documents as required.
  
- **Step 2: Text Extraction**
  
  We utilize the PyPDF2 library to read the uploaded PDFs and extract the text using PDFReader.
  
 - **Step 3: Text Chunking**
   
   Once the text extraction is complete, we run a loop to divide the extracted data into smaller, manageable chunks of text.
      
- **Step 4: Text Embedding**
  
  The smaller chunks of text are then converted into embeddings using a specific algorithm.
    
- **Step 5: Storing Embeddings**
  
  These embeddings are stored in a knowledge database, creating a repository of indexed text chunks.
    
- **Step 6: User Question Handling**
  
  - **Question Input:** Users input their questions into the system.
  - **Embedding User Question:** The questions are embedded using the same algorithm used for the text chunks.
    
- **Step 7: Building Semantic Index**
  
  A semantic index of the questions is built to provide a ranked result of the relevant text chunks.
  
- **Step 8: Language Model Processing**
  
  - **Selecting Relevant Chunks:** The system finds and ranks the chunks of text relevant to the user’s question based on their importance.
  - **Providing Context:** These selected chunks are sent as context to the language model.
     
- **Step 9: Generating Responses**
  
  The language model generates an answer based on the chunks of text selected by our vector store.
  
- **Step 10: Providing Answer**
  
  The generated answer is returned to the user, providing a contextually accurate and informative response.

### Diagram of the Workflow

This workflow ensures a seamless process for handling PDFs, extracting meaningful information, and providing accurate answers to user queries through an advanced language model.

<figure>
<img src="images/ChatPDF Diagram.png" width="100%" align="center"/></a>
<figcaption> Figure 2 - Block Diagram for ChatPDF APP </figcaption>
</figure>
<br>
<br />


## 3. Workflow for Processing and Analyzing CSVs

### Uploading and Previewing CSVs

**Example of uploading and previewing CSV files:**

  - **Access the CSV Upload Section:**
  
       - Open the ChatCSV application and navigate to the section for CSV interaction.
       - You will see an option to upload CSV files.

  - **Upload CSV Files:**
  
       - Click on the "Upload CSV" button and select the CSV file from your local storage.
       - The application will display a preview of the uploaded CSV file, showing the first few rows of data.

### Entering Queries on CSV Data

**Entering natural language queries and converting them to SQL:**

  - **Enter a Natural Language Query:**
  
       - Below the CSV preview, there is a text input field for entering queries in natural language.
       - Type your query, such as "Show me all the countries with a score greater than 7.6."

  - **Generating SQL Queries:**
  
       - The system uses Google Gemini to convert the natural language query into an SQL query.
       - The generated SQL query is displayed for user confirmation.

  - **Executing SQL Queries:**
  
       - After confirming the SQL query, click the "Execute Query" button.
       - The application runs the SQL query on the PostgreSQL database and displays the results in a tabular format.

### Generating Plots from CSV Data

**Creating visual plots based on CSV data queries:**

  - **Enter a Query for Plot Generation:**
        In the same section, you can enter a query that includes instructions for generating plots, such as "Plot a bar chart of scores by country."

  - **Generating Plots:**
  
       - The system processes the query and generates a plot based on the CSV data.
       - It uses Matplotlib to create visual representations of the data.

  - **Displaying Plots:**
  
       - The generated plot is displayed below the query input field.
       - You can interact with the plot, zoom in, or save it as needed.
      
### Diagram of the Workflow

This structured workflow ensures users can efficiently upload and analyze CSV files, providing an interactive and insightful experience through the integration of a language model.

<figure>
<img src="images/ChatCSV Diagram.png" width="100%" align="center"/></a>
<figcaption> Figure 3 - Block Diagram for ChatCSV APP </figcaption>
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


# Summary 

Intelli-Discuss is a powerful tool designed to enhance user interaction with structured and unstructured data. Its primary capabilities include:

## 1. PDF Functionality:
- **Uploading PDFs:** Users can easily upload PDF files for analysis.
- **Text Extraction:** Utilizing the PyPDF2 library, the tool extracts text from PDFs, converting them into analyzable data.
- **Dividing Text into Chunks:** Extracted text is divided into manageable chunks to facilitate efficient processing and response generation.
- **Generating Embeddings:** The extracted text is transformed into embeddings using pre-trained models, making it suitable for semantic search and context-based querying.
- **Contextual Response Generation:** Based on user queries, the system generates accurate, contextually relevant answers from the PDF content.

## 2. CSV Functionality:
- **Uploading CSVs:** Users can upload CSV files, which are previewed to ensure data integrity.
- **Inserting Data into Database:** The tool allows the creation of database tables and the insertion of CSV data into a PostgreSQL database, ensuring that data is structured and accessible.
- **Deleting Tables from Database:** Users can delete all tables from the PostgreSQL database, maintaining database hygiene and control.
- **Generating Embeddings:** CSV data is converted into embeddings, enabling semantic search and context-based querying.
- **Graphical Representation:** The tool can generate graphs from CSV data, providing visual insights into the data.

## 3. User Interaction:
- **Inputting User Queries:** Users can input queries in natural language, which are converted into embeddings for processing.
- **Converting Queries to Embeddings:** The tool transforms user queries into embeddings, facilitating semantic search and contextual understanding.

## 4. Semantic Search:
- **Performing Semantic Search:** The system executes semantic searches using embeddings, ensuring that user queries are matched with the most relevant data.
- **Ranking Search Results:** Search results are ranked based on relevance, providing users with the most pertinent information.

## 5. Contextual Response Generation:
- **Providing Context to the Language Model:** The tool supplies the necessary context to the language model, ensuring that responses are accurate and relevant.
- **Generating Answers Based on Context:** Using contextual information, the system generates precise and helpful responses to user queries.

## 6. User Response:
- **Displaying Answers to Users:** The tool formats and presents answers in a user-friendly manner, whether in text or graphical form.
- **Handling Follow-up Questions and Maintaining Context:** Intelli-Discuss maintains conversational context across multiple queries, ensuring coherent and relevant follow-up answers.
  

# Resources

- [Google AI - Google Gemini Generative Models](https://ai.google.dev/gemini-api/docs/models/generative-models)
- [OpenAI API documentation](https://platform.openai.com/docs/introduction)
- [OpenAI API registration](https://platform.openai.com/api-keys)
- [OpenAI API list of models](https://platform.openai.com/docs/models)
- [PostgreSQL-Download](https://www.postgresql.org/download/)
- [Streamlit Inc.-Documentation](https://docs.streamlit.io/)
- [FAISS.ai-Documentation](https://faiss.ai/index.html)
- [PandasAI Developers - PandasAI: Bringing the Power of AI to Pandas](https://docs.pandas-ai.com/intro)
- [LangChain Developers - Recursive Character Text Splitter in LangChain](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/)



