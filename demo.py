Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"""
SignBridge — Sign Language Interpreter (Core Module, no Flask)

This module defines:
- Static data: ASL_SIGNS, NAV_LINKS, STEPS, FEATURES, PHRASES, LANGUAGES, FOOTER_COLS
- Helper functions to "query" that data, similar to your Flask JSON APIs.

You can import this module from any Python program or UI framework.

Example:

    from signbridge_core import (
        get_sign, get_all_signs, get_all_phrases,
        NAV_LINKS, STEPS, FEATURES, LANGUAGES, FOOTER_COLS
    )

    print(get_sign("A"))
    print(get_all_signs())
"""

# ── ASL Fingerspelling ─────────────────────────────────────────────────────
ASL_SIGNS = {
    "A": {"emoji": "✊", "desc": "Closed fist, thumb resting on side"},
    "B": {"emoji": "🤚", "desc": "Flat open hand, all fingers pointing up"},
    "C": {"emoji": "🤌", "desc": "Curved hand forming a C shape"},
    "D": {"emoji": "👆", "desc": "Index up, others curve down to thumb"},
    "E": {"emoji": "🤘", "desc": "All fingers bent, thumb tucked under"},
    "F": {"emoji": "👌", "desc": "Index & thumb touch, other fingers up"},
    "G": {"emoji": "👈", "desc": "Index and thumb point sideways"},
    "H": {"emoji": "🫵", "desc": "Index and middle point sideways"},
    "I": {"emoji": "🤙", "desc": "Pinky extended, others curled"},
    "J": {"emoji": "🤙", "desc": "Pinky extended, trace a J in the air"},
    "K": {"emoji": "✌️", "desc": "Index up, middle angled, thumb between"},
    "L": {"emoji": "🤟", "desc": "L-shape: index up, thumb out sideways"},
    "M": {"emoji": "✊", "desc": "Thumb tucked under first three fingers"},
    "N": {"emoji": "✊", "desc": "Thumb tucked under index and middle"},
    "O": {"emoji": "👌", "desc": "All fingers curve to meet the thumb"},
    "P": {"emoji": "🤞", "desc": "K handshape rotated to point downward"},
    "Q": {"emoji": "👇", "desc": "G handshape rotated to point downward"},
    "R": {"emoji": "🤞", "desc": "Index and middle fingers crossed"},
    "S": {"emoji": "✊", "desc": "Fist with thumb over curled fingers"},
    "T": {"emoji": "✊", "desc": "Thumb inserted between index and middle"},
    "U": {"emoji": "✌️", "desc": "Index and middle together, pointing up"},
    "V": {"emoji": "✌️", "desc": "Index and middle spread in a V shape"},
    "W": {"emoji": "🖖", "desc": "Ring, middle, and index spread upward"},
    "X": {"emoji": "☝️", "desc": "Index finger bent into a hook"},
    "Y": {"emoji": "🤙", "desc": "Thumb and pinky extended outward"},
    "Z": {"emoji": "☝️", "desc": "Index finger traces a Z in the air"},
}

# ── Navigation ─────────────────────────────────────────────────────────────
NAV_LINKS = [
    {"href": "#how",       "label": "How It Works"},
    {"href": "#features",  "label": "Features"},
    {"href": "#demo",      "label": "Try It"},
    {"href": "#languages", "label": "Languages"},
]

# ── Steps ──────────────────────────────────────────────────────────────────
STEPS = [
    {
        "num": 1, "emoji": "📷", "title": "Open Camera",
        "desc": (
            "Open SignBridge in any browser and allow camera access. "
            "Works on phones, tablets, and laptops — no app needed."
        ),
    },
    {
        "num": 2, "emoji": "🤙", "title": "Make a Sign",
        "desc": (
            "Place your hands in frame and sign naturally. Our AI tracks "
            "21 hand landmarks per hand at 30 frames per second."
        ),
    },
    {
        "num": 3, "emoji": "⚡", "title": "Instant Translation",
        "desc": (
            "Watch the translation appear in real-time. Context-aware AI "
            "strings signs into complete, natural sentences."
        ),
    },
    {
        "num": 4, "emoji": "🔊", "title": "Speak or Share",
        "desc": (
            "Have it spoken aloud, copy it to another app, or export a full "
            "conversation transcript. Your words, your way."
        ),
    },
]

# ── Features ───────────────────────────────────────────────────────────────
FEATURES = [
    {
        "icon": "⚡", "bg": "#e0f2fe", "color": "#0284c7",
        "title": "Real-Time Detection",
        "desc": (
            "Sub-100ms latency using on-device AI. Signs are recognized "
            "before you finish making them — truly fluid conversation."
        ),
    },
    {
        "icon": "🧠", "bg": "#dcfce7", "color": "#16a34a",
        "title": "Context-Aware AI",
        "desc": (
            "Beyond gesture-by-gesture detection — our model understands "
            "full sentences, grammar, and common sign idioms."
        ),
    },
    {
        "icon": "🔒", "bg": "#faf5ff", "color": "#7c3aed",
        "title": "100% Private",
        "desc": (
            "All processing happens on your device. Your camera feed never "
            "touches our servers. What you sign, stays yours."
        ),
    },
    {
        "icon": "🌍", "bg": "#fff1f2", "color": "#e11d48",
        "title": "10 Sign Languages",
        "desc": (
            "ASL, BSL, ISL, Auslan, LSF, DGS and more. Switch between "
            "languages with a single tap from the selector."
        ),
    },
    {
        "icon": "🔊", "bg": "#fffbeb", "color": "#d97706",
        "title": "Voice Output",
        "desc": (
            "Translated text spoken aloud instantly using natural TTS in "
            "40+ voices and accents. Great face-to-face."
        ),
    },
    {
        "icon": "📚", "bg": "#f0fdf4", "color": "#15803d",
        "title": "Learn Mode",
        "desc": (
            "Practice with guided exercises, get instant feedback on form, "
            "and explore the full ASL/BSL dictionary."
        ),
    },
]

# ── Phrases ────────────────────────────────────────────────────────────────
PHRASES = [
    {"label": "Hello!",        "text": "Hello! Nice to meet you 👋"},
    {"label": "Thank you",     "text": "Thank you very much 🙏"},
    {"label": "Help me",       "text": "Please help me 🆘"},
    {"label": "I love you",    "text": "I love you ❤️"},
    {"label": "Good morning",  "text": "Good morning! ☀️"},
    {"label": "How are you?",  "text": "How are you? 😊"},
    {"label": "My name is",    "text": "My name is... ✍️"},
    {"label": "See you later", "text": "See you later! 👋"},
]

# ── Languages ──────────────────────────────────────────────────────────────
LANGUAGES = [
    {"flag": "🇺🇸", "code": "ASL",    "full": "American Sign Language",     "status": "coming"},
    {"flag": "🇬🇧", "code": "BSL",    "full": "British Sign Language",       "status": "live"},
    {"flag": "🇮🇳", "code": "ISL",    "full": "Indian Sign Language",        "status": "live"},
    {"flag": "🇦🇺", "code": "Auslan", "full": "Australian Sign Language",    "status": "coming"},
    {"flag": "🇫🇷", "code": "LSF",    "full": "Langue des Signes Française", "status": "coming"},
    {"flag": "🇩🇪", "code": "DGS",    "full": "Deutsche Gebärdensprache",    "status": "coming"},
    {"flag": "🇧🇷", "code": "Libras", "full": "Língua Brasileira de Sinais", "status": "coming"},
    {"flag": "🇯🇵", "code": "JSL",    "full": "Japanese Sign Language",      "status": "coming"},
]

# ── Footer ─────────────────────────────────────────────────────────────────
FOOTER_COLS = [
    {
        "title": "Product",
        "links": [
            {"href": "#how",       "label": "How It Works"},
            {"href": "#features",  "label": "Features"},
            {"href": "#demo",      "label": "Live Demo"},
            {"href": "#languages", "label": "Languages"},
            {"href": "#",          "label": "Download App"},
        ],
    },
    {
        "title": "Learn",
        "links": [
            {"href": "#", "label": "ASL Dictionary"},
            {"href": "#", "label": "BSL Dictionary"},
            {"href": "#", "label": "Lessons"},
            {"href": "#", "label": "Blog"},
            {"href": "#", "label": "Research"},
        ],
    },
    {
        "title": "Support",
        "links": [
...             {"href": "#", "label": "Help Center"},
...             {"href": "#", "label": "Contact Us"},
...             {"href": "#", "label": "Privacy Policy"},
...             {"href": "#", "label": "Accessibility"},
...             {"href": "#", "label": "Open Source"},
...         ],
...     },
... ]
... 
... # ── Helper functions (replace Flask JSON APIs) ─────────────────────────────
... 
... 
... def get_sign(letter):
...     """
...     Return ASL data for a single letter.
... 
...     Args:
...         letter (str): Alphabet letter.
... 
...     Returns:
...         dict: {"letter": "A", "emoji": "...", "desc": "..."} or
...               {"error": "..."} if not found.
...     """
...     key = str(letter).upper()
...     sign = ASL_SIGNS.get(key)
...     if sign:
...         return {"letter": key, **sign}
...     return {"error": f"No data for '{key}'"}
... 
... 
... def get_all_signs():
...     """
...     Return a copy of the full ASL fingerspelling dictionary.
... 
...     Returns:
...         dict: mapping of letter -> {emoji, desc}
...     """
...     return dict(ASL_SIGNS)
... 
... 
... def get_all_phrases():
...     """
...     Return a list of demo phrases.
... 
...     Returns:
...         list[dict]: [{"label": ..., "text": ...}, ...]
...     """
    return list(PHRASES)


# Optional quick CLI demo to show how it works without Flask or UI
if __name__ == "__main__":
    print("🤟 SignBridge core module demo (no Flask)")
    print("Type a letter A–Z to see its sign, or 'quit' to exit.\n")

    while True:
        user = input("Letter> ").strip()
        if not user:
            continue
        if user.lower() in ("q", "quit", "exit"):
            break
