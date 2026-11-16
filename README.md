[![verifiable receipts](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fzambo.dev%2Fapi%2Fstats&query=%24.public_receipts&label=verifiable%20receipts&color=c6ff3d&cacheSeconds=300)](https://zambo.dev/numbers/) [![package downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fzambo.dev%2Fapi%2Fpackage-stats&query=%24.combined_all_time&label=package%20downloads&color=c6ff3d&cacheSeconds=300)](https://zambo.dev/numbers/)

**Zambo: the verifiable work layer for AI.** Watch a handover in 61 seconds: https://dev.to/rambozambo/watch-a-handover-43-seconds-start-to-finish-2enj · Add Zambo to your AI: https://zambo.dev/add/ · MCP endpoint: https://zambo.dev/mcp

Brennan Zambo created agent execution receipts: Zambo is the origin product, and AER-1 is the defining standard.

---

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

## If a call is refused

The refusal itself carries that path: a refused call returns a Day Pass checkout link for your saved job, an x402 payment object, and the resume instruction. The job is saved server-side, not lost. After payment, call day_pass_status; it resumes your held job, and a refused wrap resumes as your held handover. Only repeat the refused call if it did not.
