from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field , ConfigDict
import psycopg2



class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    query: str = Field(..., description="The sql query for the pagila database.")

class SqlQueryExecuter(BaseTool):
    name: str = "sql_query_executer"
    description: str = (
        "This tool executes the sql query for the pagila database."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(self, db_config):
        """Initialize the tool with a vector database instance."""
        super().__init__()
        object.__setattr__(self, "db_config", db_config)

    def _run(self, query: str) -> None:
        try:
            # Connect to PostgreSQL database
            conn = psycopg2.connect(**self.db_config)

            # Create a cursor to execute SQL commands
            cur = conn.cursor()

            # Execute the query
            cur.execute(query)

            # Fetch all results
            results = cur.fetchall()

            # Close the cursor and connection
            cur.close()
            conn.close()
            
            return results

        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL:", e)
