from crewai import Crew, Process
from src.crew.agents import planner, researcher, writer
from src.crew.tasks import task_plan, task_research, task_write

# --- 6. Create and Run the Crew ---
project_crew = Crew(
    agents=[planner, researcher, writer],
    tasks=[task_plan, task_research, task_write],
    process=Process.sequential,
    verbose=True
)

# Kick off the crew!
if __name__ == "__main__":
    print("🚀 Starting the Developer Crew...")
    result = project_crew.kickoff()

    print("\n✅ Crew run completed!")
    print("Final Result:")
    print(result)