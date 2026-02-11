from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import math

LANGUAGES = [
    ("fi", "🇫🇮 Finnish"),
    ("da", "🇩🇰 Danish"),
    ("nl", "🇳🇱 Dutch"),
    ("el", "🇬🇷 Greek"),
    ("sv", "🇸🇪 Swedish"),
    ("no", "🇳🇴 Norwegian"),
    ("de", "🇩🇪 German"),
    ("fr", "🇫🇷 French"),
    ("es", "🇪🇸 Spanish"),
    ("it", "🇮🇹 Italian"),
    ("pt", "🇵🇹 Portuguese"),
    ("tr", "🇹🇷 Turkish"),
    ("ru", "🇷🇺 Russian"),
    ("en", "🇬🇧 English"),
    ("ar", "🇸🇦 Arabic"),
    ("zh", "🇨🇳 Chinese"),
    ("ja", "🇯🇵 Japanese"),
    ("ko", "🇰🇷 Korean"),
    ("hi", "🇮🇳 Hindi"),
    ("id", "🇮🇩 Indonesian"),
    ("th", "🇹🇭 Thai"),
    ("vi", "🇻🇳 Vietnamese"),
    ("uk", "🇺🇦 Ukrainian"),
    ("pl", "🇵🇱 Polish"),
    ("cs", "🇨🇿 Czech"),
    ("sk", "🇸🇰 Slovak"),
    ("hu", "🇭🇺 Hungarian"),
    ("ro", "🇷🇴 Romanian"),
    ("bg", "🇧🇬 Bulgarian"),
    ("he", "🇮🇱 Hebrew"),
    ("sr", "🇷🇸 Serbian"),
    ("hr", "🇭🇷 Croatian"),
    ("sl", "🇸🇮 Slovenian"),
    ("lt", "🇱🇹 Lithuanian"),
    ("lv", "🇱🇻 Latvian"),
    ("et", "🇪🇪 Estonian"),
    ("is", "🇮🇸 Icelandic"),
    ("mt", "🇲🇹 Maltese"),
    ("ms", "🇲🇾 Malay"),
    ("ka", "🇬🇪 Georgian"),
]

PER_PAGE = 4


def language_keyboard(page: int = 0):
    total_pages = math.ceil(len(LANGUAGES) / PER_PAGE)
    page = max(0, min(page, total_pages - 1))

    start = page * PER_PAGE
    end = start + PER_PAGE

    keyboard = []

    # language buttons (1 per row)
    for code, name in LANGUAGES[start:end]:
        keyboard.append([
            InlineKeyboardButton(
                text=name,
                callback_data=f"tts:{code}"
            )
        ])

    # navigation row: ⬅️  7/16  ➡️
    nav = []

    nav.append(
        InlineKeyboardButton(
            "⬅️", callback_data=f"page:{page - 1}" if page > 0 else "noop"
        )
    )

    nav.append(
        InlineKeyboardButton(
            f"{page + 1}/{total_pages}", callback_data="noop"
        )
    )

    nav.append(
        InlineKeyboardButton(
            "➡️", callback_data=f"page:{page + 1}" if page < total_pages - 1 else "noop"
        )
    )

    keyboard.append(nav)

    return InlineKeyboardMarkup(keyboard)
