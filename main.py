# main.py

import time # <--- Add this import
import re
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
    print("\n\n🚀 Starting the Deep Research Crew...")
    print("---------------------------------")
    
    while True:
        # 1. Clean Input Prompt
        print("\n\n" + "="*50)
        print("🤖 READY FOR NEW TASK")
        print("="*50)
        user_request = input("Enter your research topic (or 'exit' to quit) > ")

        if user_request.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        
        if not user_request.strip():
            continue

        # 2. Dynamic Filename Generation (Python Logic)
        # Convert "Solid State Batteries" -> "solid_state_batteries.md"
        clean_filename = user_request.lower().replace(" ", "_")
        clean_filename = re.sub(r'[^\w\-]', '', clean_filename) # Remove special chars
        clean_filename = clean_filename[:50] + ".md" # Limit length

        print(f"📝 Target Filename: {clean_filename}")

        # 3. Pass Filename to Agents via Inputs
        inputs = {
            'user_request': user_request,
            'filename': clean_filename
        }
        
        # 4. Kick off!
        result = project_crew.kickoff(inputs=inputs)

        # 5. Final Output & Pause
        print("\n\n" + "-"*50)
        print("✅ Research completed!")
        print(f"📂 Saved to: output/{clean_filename}")
        print("-"*50)
        
        # Pause for 2 seconds to let logs finish printing before next prompt
        time.sleep(2)