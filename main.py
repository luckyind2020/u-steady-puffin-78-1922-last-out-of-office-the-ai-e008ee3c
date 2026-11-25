"""Out-of-office auto-reply, served hot.

Reads the single-line reply from entry.txt and prints it, the way an
inbox would send it back to whoever wrote in.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
REPLY_FILE = HERE / "entry.txt"
MAX_CHARS = 280


def load_reply(path=REPLY_FILE):
    """Return the reply with its trailing newline trimmed."""
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt holds no reply to send back")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "reply is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    print(load_reply())


if __name__ == "__main__":
    main()
