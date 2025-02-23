#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from src.crewai_test.crew import SrcCrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

class crew_flow():

    def __init__(self , db_config) -> str:
        self.db_config = db_config
    
    
    def get_results(self , query)->str:
        """
        Run the crew.
        """
        
        inputs = {
            "plain_query": query
        }

        try:
            sql_crew = SrcCrewai(self.db_config)
            result = sql_crew.crew().kickoff(inputs=inputs)
        except Exception as e:
            raise Exception(f"An error occurred while running the crew: {e}")
        
        return result.raw
