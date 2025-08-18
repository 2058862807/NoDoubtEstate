import json, os
MEMO_FILE = os.path.join(os.path.dirname(__file__), "..", "ai", "memory.json")

def record_feedback(event: str, detail: str):
    try:
        os.makedirs(os.path.dirname(MEMO_FILE), exist_ok=True)
        data = []
        if os.path.exists(MEMO_FILE):
            data = json.load(open(MEMO_FILE, "r", encoding="utf-8"))
        data.append({"event": event, "detail": detail})
        json.dump(data, open(MEMO_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    except Exception:
        pass
