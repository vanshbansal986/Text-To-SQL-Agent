import streamlit as st
import os
import markdown2
import pandas as pd
import re
from src.crewai_test.main import crew_flow

# Must be the first Streamlit command
st.set_page_config(page_title="Text to SQL Demo", page_icon="🤖")

# Custom CSS remains the same until the question-text class
st.markdown("""
<style>
    /* Section Headers */
    .section-header {
        font-size: 1.5em;
        font-weight: bold;
        margin: 1.5em 0 1em 0;
        padding-bottom: 0.5em;
        border-bottom: 2px solid #f0f0f0;
    }
    
    /* Tables */
    .dataframe {
        width: 100%;
        border-collapse: collapse;
        margin: 1em 0;
        font-size: 16px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .dataframe th {
        background-color: #4a4a4a;
        color: white;
        padding: 12px 15px;
        text-align: left;
        font-weight: bold;
    }
    .dataframe td {
        padding: 12px 15px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    .dataframe tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    .dataframe tr:hover {
        background-color: #f0f0f0;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background-color: #2b2b2b !important;
        padding: 1em;
        border-radius: 8px;
        margin: 1em 0;
    }
    code {
        font-family: 'Courier New', monospace !important;
        font-size: 16px !important;
    }
    
    /* Question and result text */
    .content-text {
        font-size: 1.2em;
        margin: 1em 0;
        padding: 1em;
        background-color: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid #4a4a4a;
        line-height: 1.6;
        color: #2c3e50;
    }
    
    /* Result description text */
    .result-description {
        margin: 1em 0;
        font-size: 1.1em;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# Database config and sidebar setup remain the same
if 'response' not in st.session_state:
    st.session_state.response = None

db_config = {
    "host": "localhost",
    "database": "pagila",
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}

with st.sidebar:
    st.title("Configuration")
    google_api_key = st.text_input("Google API Key", type="password")
    if google_api_key:
        os.environ["GOOGLE_API_KEY"] = google_api_key

st.title("Pagila Database Query Agent 🗄️")
st.write("Convert natural language to SQL queries")

user_query = st.text_area(
    "Enter your question:",
    placeholder="e.g. Show me all customers from Canada",
    height=100
)


def extract_table_and_text(result_text):
    """Separate table content from regular text in the result."""
    # Find markdown table pattern
    table_pattern = r'(\|.*\|(\r?\n|$))+'
    table_match = re.search(table_pattern, result_text)
    
    if table_match:
        table_content = table_match.group(0).strip()
        # Get text before and after table
        text_parts = re.split(table_pattern, result_text)
        text_content = ' '.join(part.strip() for part in text_parts if part and not part.isspace() and not part.startswith('|'))
        return table_content, text_content
    else:
        return None, result_text.strip()

def clean_markdown_table(table_text):
    """Clean and standardize markdown table format."""
    if not table_text:
        return None
        
    lines = [line.strip() for line in table_text.split('\n')]
    lines = [line for line in lines if line and not line.isspace()]
    
    if len(lines) >= 2:
        header_cells = len(lines[0].split('|'))
        separator_line = '|' + '|'.join(['-' * 15 for _ in range(header_cells-2)]) + '|'
        lines[1] = separator_line
    return '\n'.join(lines)

def parse_table_to_dataframe(table_text):
    """Convert markdown table text into a pandas DataFrame."""
    try:
        if not table_text:
            return None
            
        clean_text = clean_markdown_table(table_text)
        lines = [line.strip() for line in clean_text.split('\n') if line.strip()]
        
        headers = [cell.strip() for cell in lines[0].split('|') if cell.strip()]
        data = []
        for line in lines[2:]:
            row = [cell.strip() for cell in line.split('|') if cell.strip()]
            if row:
                data.append(row)
                
        return pd.DataFrame(data, columns=headers)
    except Exception:
        return None

def parse_response(response):
    """Parse and clean the LLM response."""
    sections = re.split(r'###\s*', response)
    sections = [s.strip() for s in sections if s.strip()]
    
    parsed = {
        'question': '',
        'result': '',
        'query': ''
    }
    
    for section in sections:
        if section.lower().startswith('question'):
            parsed['question'] = section.replace('Question', '').strip()
        elif section.lower().startswith('result'):
            parsed['result'] = section.replace('Result', '').strip()
        elif section.lower().startswith('query'):
            parsed['query'] = section.replace('Query used', '').strip()
            
    return parsed

def extract_sql_query(text):
    """Extract SQL query from text and clean it."""
    query = re.sub(r'```sql\s*|\s*```', '', text)
    query = '\n'.join(line for line in query.split('\n') if line.strip())
    return query

if st.button("Convert to SQL"):
    if user_query.strip() and google_api_key:
        with st.spinner("Generating response..."):
            try:
                response = crew_flow(db_config).get_results(user_query)
                parsed_response = parse_response(response)
                
                # Display Question
                st.markdown('<div class="section-header">Question</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="content-text">{parsed_response["question"]}</div>', 
                          unsafe_allow_html=True)
                
                # Display Results
                st.markdown('<div class="section-header">Results</div>', unsafe_allow_html=True)
                
                # Extract table and text content from results
                table_content, text_content = extract_table_and_text(parsed_response["result"])
                
                # Display text content if present
                if text_content:
                    st.markdown(f'<div class="result-description">{text_content}</div>', 
                              unsafe_allow_html=True)
                
                # Display table if present
                if table_content:
                    df = parse_table_to_dataframe(table_content)
                    if df is not None:
                        st.dataframe(df, use_container_width=True)
                
                # Display Query
                st.markdown('<div class="section-header">Query Used</div>', unsafe_allow_html=True)
                clean_query = extract_sql_query(parsed_response["query"])
                st.code(clean_query, language='sql')
                
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
    elif not google_api_key:
        st.error("Please enter a Google API key in the sidebar")
    else:
        st.warning("Please enter a question first")