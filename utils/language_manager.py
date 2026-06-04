from utils.settings import settings


class LanguageManager:

    def __init__(self):

        self.default_language = getattr(
            settings,
            "DEFAULT_LANGUAGE",
            "id"
        )

    def get_system_prompt(self):

        if self.default_language == "en":

            return """
Use professional business English.

Rules:

- Clear.
- Concise.
- Executive style.
- Perfect grammar.
"""

        return """
Gunakan Bahasa Indonesia profesional.

Aturan:

- Tata bahasa benar.
- Gaya bahasa profesional.
- Ringkas dan jelas.
- Hindari istilah bahasa Inggris jika ada padanan Indonesia.

Terjemahan:

brand = merek
feedback = umpan balik
workflow = alur kerja
brief = kebutuhan proyek
"""