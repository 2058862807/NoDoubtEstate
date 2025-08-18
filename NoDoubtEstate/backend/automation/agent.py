from typing import Dict, Any
from .self_improve import record_feedback

def run_agent_task(goal: str, params: Dict[str, Any]) -> Dict[str, Any]:
    g = goal.lower()
    if "deploy" in g:
        rec = {"next": "call /vercel/deploy", "params": params}
    elif "reply" in g:
        rec = {"next": "call /email/reply", "params": params}
    elif "push" in g or "commit" in g:
        rec = {"next": "call /git/push", "params": params}
    elif "word" in g or "dictate" in g:
        rec = {"next": "use /word/type", "params": params}
    else:
        rec = {"note": "no matching action", "goal": goal, "params": params}
    record_feedback("agent_plan", str(rec))
    return rec
