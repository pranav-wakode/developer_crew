from crewai import Task
from .agents import planner, researcher, writer

# The initial user request
user_request = "Research 'best Python web frameworks' and save the answer to a file named research.md."

# --- 5. Define Tasks (3 Tasks) ---
task_plan = Task(
    description=f"Create a plan to fulfill this request: '{user_request}'. "
                "Your final output must be a simple plan detailing the search query and the filename.",
    expected_output="A plan including the string for the search query and the string for the filename.",
    agent=planner,
    human_input=True
)

task_research = Task(
    description="Execute the web search using the query from the planner's report.",
    expected_output="A detailed summary of the research findings.",
    agent=researcher,
    context=[task_plan]
)

task_write = Task(
    description="Take the research findings and the filename from the plan. "
                "Format the findings as a markdown file and save it using the file writing tool.",
    expected_output="The final file path of the saved markdown file.",
    agent=writer,
    context=[task_research, task_plan]
)