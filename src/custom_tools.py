# src/custom_tools.py
import os
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools.base_tool import BaseTool

# This is your correct fix for the search tool
class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"
    description: str = "Search the web for information using DuckDuckGo. Input should be a search query string."
    
    def _run(self, query: str) -> str:
        """Execute the search."""
        search = DuckDuckGoSearchRun()
        return search.run(query)

# This is our file tool, which is working correctly
class SafeFileWriteTool(BaseTool):
    name: str = "Safe File Writer"
    description: str = "Write content to a file safely. Input should be a JSON string with 'filename' and 'content' keys."

    def _run(self, filename: str, content: str) -> str:
        """Execute the tool."""
        if not filename or not content:
            return "Error: Missing 'filename' or 'content' in input."

        # --- NEW SANDBOX ---
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))
        
        os.makedirs(output_dir, exist_ok=True)

        file_path = os.path.abspath(os.path.join(output_dir, filename))

        if not file_path.startswith(output_dir):
            return f"Error: File path '{filename}' is outside the allowed 'output' directory. Access denied."
        
        if ".." in filename.split(os.sep):
            return "Error: Relative paths with '..' are not allowed."
        # --- END NEW SANDBOX ---

        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            # Return a clearer path
            return f"Successfully wrote content to output/{filename}"
        except Exception as e:
            return f"Error writing file: {e}"