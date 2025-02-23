import os
import psycopg2
import pandas as pd


os.environ["GOOGLE_API_KEY"] = input("Enter your Google API Key: ")


db_config = {
    "host": input("Enter database host (default: localhost): ") or "localhost",
    "database": input("Enter database name: "),
    "user": input("Enter database username: "),
    "password": input("Enter database password: ")
}

from src.crewai_test.main import crew_flow


flow = crew_flow(db_config)

while True:
    query = input("Enter a natural language query (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        print("Exiting the program.")
        break
    
    print(f"Processing query: {query}...")
    resp = flow.get_results(query)
    
    print("Generated SQL Query and Results:")
    print(resp)
    
    with open("report.md", "a", encoding="utf-8") as file:
        file.write(f"Query: {query}\n\nResponse:\n{resp}\n\n\n")
