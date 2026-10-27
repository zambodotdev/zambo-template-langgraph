# pip install -r requirements.txt, then: python main.py
# Runs a tiny LangGraph graph (fake chat model, no API key needed)
# and prints an AER-1 receipt for the whole run.
from langgraph.graph import StateGraph, START, END
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from aer1_langgraph import AER1LangGraphHandler

def researcher(state: dict):
    model = GenericFakeChatModel(messages=iter(["found 3 papers"]))
    return {"notes": model.invoke("research").content}

def writer(state: dict):
    model = GenericFakeChatModel(messages=iter(["draft complete"]))
    return {"draft": model.invoke("write").content}

graph = StateGraph(dict)
graph.add_node("researcher", researcher)
graph.add_node("writer", writer)
graph.add_edge(START, "researcher")
graph.add_edge("researcher", "writer")
graph.add_edge("writer", END)
app = graph.compile()

handler = AER1LangGraphHandler(goal="Write the report")
result = app.invoke({}, config={"callbacks": [handler]})
receipt = handler.finalize(final_answer=result)
problems = handler.verify(receipt)
assert problems == [], problems
handler.save("receipt.json", workflow=receipt)
print("result:", result)
print("receipt id:", receipt.get("receipt_id") or receipt.get("id") or receipt.get("workflow_id"))
print("verified by the built-in AER-1 verifier: no problems")
print("independent check: aer1-verify receipt.json")
print("want this on your own ai: https://zambo.dev/add/?ref=zambo-template-langgraph")
