from googletrans import Translator

translator = Translator()

LANGUAGES = {
    'afrikaans': 'af',
    'albanian': 'sq',
    'arabic': 'ar',
    'belarusian': 'be',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'chinese_simplified': 'zh-CN',
    'chinese_traditional': 'zh-TW',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'galician': 'gl',
    'german': 'de',
    'greek': 'el',
    'hebrew': 'iw',
    'hindi': 'hi',
    'hungarian': 'hu',
    'icelandic': 'is',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'korean': 'ko',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'macedonian': 'mk',
    'malay': 'ms',
    'maltese': 'ml',
    'norwegian': 'no',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'romanian': 'ro',
    'russian': 'ru',
    'serbian': 'sr',
    'slovak': 'sk',
    'slovenian': 'sl',
    'spanish': 'es',
    'swahili': 'sw',
    'swedish': 'sv',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'yiddish': 'yi',
}

print("Supported Language:")
for lang in LANGUAGES:
    print(lang)

langsrc = input("Enter language src: ")
langdest = input("Enter Language you want to translate to (NOTE:use exact spelling!!): ")

word = input("Enter to string to be translated: ")

x = translator.translate(word, LANGUAGES[langdest], langsrc)
print(x.text)
