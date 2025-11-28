# src/agents.py

from crewai import Agent, LLM
from src.custom_tools import DuckDuckGoSearchTool, SafeFileWriteTool

# --- Setup ---
search_tool = DuckDuckGoSearchTool()
write_tool = SafeFileWriteTool()

local_llm = LLM(
    model="ollama/yxchia/qwen2.5-3b-instruct:Q4_K_M",
    base_url="http://localhost:11434"
)

# --- Agents ---

# 1. Researcher (Unchanged)
researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments and detailed information on the user's topic.",
    backstory=(
        "You are a veteran analyst with a keen eye for detail. "
        "You do not just find facts; you find the *truth* and the *context*. "
        "You ignore surface-level fluff and dig for data, dates, and specific details. "
        "Use the search tool to gather as much relevant info as possible."
    ),
    tools=[search_tool],
    llm=local_llm,
    verbose=True
)

# 2. Analyst (Unchanged)
analyst = Agent(
    role="Critical Content Strategist",
    goal="Analyze the raw research, identify gaps, and construct a logical outline.",
    backstory=(
        "You are the brain of the operation. You look at raw data and see the story. "
        "You critique the research: is it enough? Is it relevant? "
        "You organize the chaotic notes from the researcher into a clean, logical structure "
        "that the writer can easily follow."
    ),
    llm=local_llm,
    verbose=True
)

# 3. Writer (Unchanged)
writer = Agent(
    role="Lead Content Creator",
    goal="Draft a compelling, well-formatted markdown article based on the analyst's outline.",
    backstory=(
        "You are a skilled storyteller and technical writer. "
        "You take structured outlines and turn them into engaging prose. "
        "You use Markdown formatting (headers, lists, bold text) effectively to make the content readable. "
        "You do NOT invent facts; you stick to the provided research."
    ),
    llm=local_llm,
    verbose=True
)

# 4. Publisher (UPDATED - STRICTER)
publisher = Agent(
    role="File Publishing Utility",
    goal="Save the content to the file using the tool. Do NOT print the content.",
    backstory=(
        "You are a file system utility. You have NO creative ability. "
        "You receive text and a filename. "
        "**Your ONLY purpose is to call the 'Safe File Writer' tool.** "
        "**You are FORBIDDEN from printing the article text in your final answer.** "
        "If you output the text instead of calling the tool, you have failed."
    ),
    tools=[write_tool],
    llm=local_llm,
    verbose=True,
    allow_delegation=False
)