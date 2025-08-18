from typing import Tuple
try:
    import win32com.client as win32
    HAS_COM = True
except Exception:
    HAS_COM = False

def type_into_word(text: str, open_new: bool = False) -> Tuple[bool, str]:
    if HAS_COM:
        try:
            word = win32.gencache.EnsureDispatch("Word.Application")
            word.Visible = True
            if open_new or word.Documents.Count == 0:
                _ = word.Documents.Add()
            sel = word.Selection
            sel.TypeText(text)
            return True, "typed"
        except Exception:
            pass
    try:
        import pyautogui, time
        time.sleep(0.6)
        pyautogui.typewrite(text, interval=0.01)
        return True, "typed simulated"
    except Exception as e:
        return False, str(e)
