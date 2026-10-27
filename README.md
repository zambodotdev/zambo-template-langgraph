# LangGraph + zambo: every run gets a checkable receipt

run it in under a minute:
1. click "use this template", or open in codespaces
2. `pip install -r requirements.txt && python main.py`
3. it prints a receipt id and saves receipt.json, verified on the spot. check it independently with `aer1-verify receipt.json`

what you get: your LangGraph run is recorded as an AER-1 receipt: every node and step hash-chained under one merkle root, so anyone can later confirm the record was not changed after the run, without trusting any server. swap the fake chat model for your real model and the receipt covers the real run the same way.
full guide: https://zambo.dev/langgraph-handoff-receipts/

---
next step: add zambo to your ai in one url, no key, no account: https://zambo.dev/add/?ref=zambo-template-langgraph
got a receipt link from someone? check it in seconds: https://zambo.dev/verify/
every call returns a receipt. a receipt proves the saved bytes are unchanged. it does not prove the answer is right.
