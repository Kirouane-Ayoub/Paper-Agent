import os
from pathlib import Path

import mesop as me
import mesop.labs as mel
import settings as settings
from llama_index.core.agent import AgentRunner, FunctionCallingAgentWorker
from models import llm
from tools import extract_and_clean_text, get_doc_tools

paper_to_tools_dict = {}
papers = [
    os.path.join(settings.DATA_FOLDER, f)
    for f in os.listdir(settings.DATA_FOLDER)
    if os.path.isfile(os.path.join(settings.DATA_FOLDER, f))
]

for paper in papers:
    vector_tool, summary_tool = get_doc_tools(paper, Path(paper).stem)
    paper_to_tools_dict[paper] = [vector_tool, summary_tool]

initial_tools = [t for paper in papers for t in paper_to_tools_dict[paper]]

agent_worker = FunctionCallingAgentWorker.from_tools(
    initial_tools, llm=llm, verbose=False
)
agent = AgentRunner(agent_worker)


def transform(query: str, history: list[mel.ChatMessage]):
    response = agent.query(query)
    text = extract_and_clean_text(response.response)
    return text


@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/chat",
    title="Paper-Agent",
)
def page():
    mel.chat(transform, title="Paper-Agent", bot_user="Paper-Agent bot")
