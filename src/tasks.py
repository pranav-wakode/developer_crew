# src/tasks.py

from crewai import Task
from src.agents import researcher, analyst, writer, publisher

def get_tasks():
    
    # Task 1: Research
    task_research = Task(
        description=(
            "Research the following topic extensively: '{user_request}'. "
            "Focus on recent developments, key facts, pros/cons, and expert opinions. "
            "Gather as much detailed information as possible."
        ),
        expected_output="A detailed document containing all relevant research findings and raw data.",
        agent=researcher
    )

    # Task 2: Analyze & Critique
    task_analysis = Task(
        description=(
            "Review the research findings. Identify the key themes and logical flow. "
            "Critique the content: remove irrelevant info and highlight the most important points. "
            "Create a structured outline for an article."
        ),
        expected_output="A comprehensive outline and logical structure for the final article.",
        agent=analyst,
        context=[task_research]
    )

    # Task 3: Write
    task_writing = Task(
        description=(
            "Using the analyst's outline and the original research, write a full article. "
            "Use professional Markdown formatting (H1, H2, bullet points). "
            "Ensure the tone is engaging and informative. "
            "The output must be the *final* article content ready for publishing."
        ),
        expected_output="The complete, formatted text of the article in Markdown.",
        agent=writer,
        context=[task_analysis, task_research]
    )

    # Task 4: Publish (Save File)
    task_publish = Task(
        description=(
            "Take the final article text from the writer. "
            "Save it to a file named 'report.md' using the 'Safe File Writer' tool. "
            "**You MUST call the tool with the filename 'report.md'.**"
        ),
        expected_output="Confirmation that the file was saved.",
        agent=publisher,
        context=[task_writing]
    )
    
    return [task_research, task_analysis, task_writing, task_publish]