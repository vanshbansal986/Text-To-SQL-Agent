# Text-to-SQL Agent for Pagila Database

## Table of Contents
- [Text-to-SQL Agent for Pagila Database](#text-to-sql-agent-for-pagila-database)
  - [Table of Contents](#table-of-contents)
  - [Problem Statement](#problem-statement)
  - [How It Works](#how-it-works)
    - [Custom Tools and Frameworks](#custom-tools-and-frameworks)
  - [Project Workflow](#project-workflow)
  - [Main Analysis and Results](#main-analysis-and-results)
  - [Project Structure](#project-structure)
  - [Setup](#setup)
  - [Usage](#usage)


## Problem Statement
This project aims to develop a natural language interface that translates user input (plain text queries) into SQL queries for the Pagila database. The Pagila database consists of 21 interrelated tables, and the goal is to generate accurate SQL queries while handling ambiguous or incorrect user inputs gracefully.


## How It Works
This project is built using a **multi-agentic framework** to handle the conversion of natural language to SQL and execution of queries efficiently. It consists of **two main agents**:

1. **SQL Query Generation Agent**
   - This agent is responsible for converting plain text user input into SQL queries.
   - It ensures the generated queries align with the Pagila database schema, using proper table and column names.
   - The agent is designed to handle ambiguous queries by prompting the user for clarifications when necessary.

2. **SQL Execution Agent**
   - This agent takes the generated SQL query and executes it on the Pagila database.
   - It retrieves the results and formats them into a structured table for easy interpretation.
   - If the query fails due to syntax errors or schema mismatches, it provides feedback to improve query accuracy.

### Custom Tools and Frameworks
- **CrewAI**: The project leverages the CrewAI framework for orchestrating multiple agents and handling complex task execution.
- **Custom Tools**: Special tools are implemented to optimize query generation and execution, ensuring high accuracy and performance.
- **Model Used**: The underlying LLM model used for natural language processing and SQL generation is **Gemini 2.0 Flash**, which provides efficient and accurate query translation.

This multi-agent approach ensures that the system is both scalable and robust, effectively handling diverse and complex natural language queries.



## Project Workflow
1. **User Input:** The user provides a natural language question.
2. **Query Generation:** The system processes the input and generates a corresponding SQL query.
3. **Execution:** The generated SQL query is executed on the Pagila database.
4. **Output Display:** The results of the query execution are displayed in a structured table format.
5. **Error Handling:** If the input is ambiguous or incorrect, the system provides feedback to help the user refine their query.

## Main Analysis and Results
For detailed analysis and evaluation results, refer to the [report.md](./report.md) file. The system has been tested against 40 predefined queries, and accuracy is assessed based on:
- **100%** for fully correct queries.
- **50%** for logically correct queries with minor errors.
- **0%** for incorrect queries or queries that produce incorrect results.

## Project Structure
```
├── README.md           # Project documentation
├── app.py              # Application entry point
├── final_report.md     # Final project report
├── main.py             # Main execution script
├── pagila/             # Pagila database files
├── queries.csv         # Test queries
├── report.md           # Detailed analysis and evaluation
├── requirements.txt    # Required dependencies
└── src/
    ├── crewai_test/
    │   ├── README.md
    │   ├── __init__.py
    │   ├── crew.py
    │   ├── main.py
    │   ├── pyproject.toml
    │   ├── config/
    │   │   ├── agents.yaml
    │   │   └── tasks.yaml
    │   ├── tools/
    │   │   ├── __init__.py
    │   │   └── query_executer.py
    ├── pipeline/       # Data pipeline scripts
    ├── system_prompts/ # Prompt engineering files
    │   ├── prompt1.txt
    │   └── prompt2.txt
    └── utils/          # Utility scripts
```

## Setup
To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Create the pagila database using Docker**
   ```sh
   docker-compose up
   ```
   Once running, execute the following command to access the database:
   ```sh
   docker exec -it pagila psql -U postgres
   ```

## Usage

1. **Run the Application**
   ```sh
   python test.py
   ```

2. **Enter Required Credentials**
   - You will be prompted to enter your **Google API Key**.
   - Provide the **database connection details** (host, database name, username, password).

3. **Provide Natural Language Queries**
   - Enter a query when prompted.
   - Example Input: "List the top 5 films with the highest revenue."
   - To exit, type 'exit'.
