# src/tasks.py

from crewai import Task
from src.agents import researcher, analyst, writer, publisher

def get_tasks():
    
    # Task 1: Research (Unchanged)
    task_research = Task(
        description=(
            "Research the following topic extensively: '{user_request}'. "
            "Focus on recent developments, key facts, pros/cons, and expert opinions. "
            "Gather as much detailed information as possible."
        ),
        expected_output="A detailed document containing all relevant research findings and raw data.",
        agent=researcher
    )

    # Task 2: Analyze (Unchanged)
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

    # Task 3: Write (Unchanged - Keeps formatting fix)
    task_writing = Task(
        description=(
            "Using the analyst's outline and the original research, write a full article. "
            "**FORMATTING RULES:**\n"
            "1. Output ONLY a single, continuous Markdown string.\n"
            "2. Use # for titles, ## for sections, and - for bullet points.\n"
            "3. **DO NOT** output a JSON object, a Python dictionary, or any structured data format.\n"
            "4. **DO NOT** use curly braces {{ }} around your content.\n"
            "5. Just write the text directly, starting with the Title."
        ),
        expected_output="A single string of Markdown text representing the article.",
        agent=writer,
        context=[task_analysis, task_research]
    )

    # Task 4: Publish (UPDATED - STRICTER)
    task_publish = Task(
        description=(
            "You have one simple task:\n"
            "1. Take the text from the writer.\n"
            "2. Call the 'Safe File Writer' tool with filename='{filename}' and content=[the text].\n"
            "**DO NOT output the text yourself. JUST call the tool.**"
        ),
        expected_output="A confirmation message saying 'File saved successfully'.",
        agent=publisher,
        context=[task_writing]
    )
    
    return [task_research, task_analysis, task_writing, task_publish]