# main.py

from crewai import Crew, Process
from src.agents import researcher, analyst, writer, publisher
from src.tasks import get_tasks

# --- Create the Crew ---
project_crew = Crew(
    agents=[researcher, analyst, writer, publisher],
    tasks=get_tasks(),
    process=Process.sequential,
    verbose=True
)

# --- Run the Crew in a Loop ---
if __name__ == "__main__":
    print("🚀 Starting the Deep Research Crew...")
    print("---------------------------------")
    print("Enter your research topic (or 'exit' to quit).")

    while True:
        user_request = input("\nTopic > ")

        if user_request.lower() == 'exit':
            print("👋 Goodbye!")
            break
        
        if not user_request:
            continue

        inputs = {'user_request': user_request}
        
        # Kick off!
        result = project_crew.kickoff(inputs=inputs)

        print("\n✅ Research completed!")
        print("Check the 'output/report.md' file.")
        print("---------------------------------")