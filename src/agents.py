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

# 1. The Researcher
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

# 2. The Analyst (Critique & Logic)
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

# 3. The Writer
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

# 4. The Publisher (The "Dumb" Utility from our previous success)
publisher = Agent(
    role="File Publishing Utility",
    goal="Save the exact text provided by the writer to a file.",
    backstory=(
        "You are a silent utility. You do not think, you do not summarize. "
        "You take the text given to you and you call the 'Safe File Writer' tool to save it. "
        "**Your only job is to use the tool.**"
    ),
    tools=[write_tool],
    llm=local_llm,
    verbose=True,
    allow_delegation=False
)