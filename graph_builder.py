from transformers import pipeline
from langgraph.graph import StateGraph, END
from typing import TypedDict
from memory_store import LongTermMemory


class AgentState(TypedDict):
    question: str
    context: str
    answer: str


# ✅ Use GPT2 (Fully Compatible)
pipe = pipeline(
    task="text-generation",
    model="gpt2",
    max_new_tokens=120,
    temperature=0.3,
    do_sample=True
)

memory = LongTermMemory()


def retrieve(state: AgentState):
    context = memory.search(state["question"])
    return {"context": context}


def generate(state: AgentState):
    prompt = f"""
You are a helpful IT support assistant.
Use the context to answer clearly.

Context:
{state['context']}

Question:
{state['question']}

Answer:
"""

    result = pipe(prompt)
    full_output = result[0]["generated_text"]

    # Remove prompt from output
    answer = full_output.replace(prompt, "").strip()

    return {"answer": answer}


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate)

    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()