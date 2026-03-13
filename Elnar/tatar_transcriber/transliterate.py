# ========================
# Arabic Tatar → Latin
# ========================

ARABIC_SINGLE = {
    'ا':'a', 'آ':'a', 'ب':'b', 'پ':'p', 'ت':'t', 'ج':'c', 'چ':'ç',
    'ح':'h', 'خ':'x', 'د':'d', 'ر':'r', 'ز':'z', 'ژ':'j',
    'س':'s', 'ش':'ş', 'ع':'‘', 'ف':'f', 'ق':'q', 'ك':'k',
    'ل':'l', 'م':'m', 'ن':'n', 'و':'w', 'ه':'h', 'ی':'i', 'ى':'y',
    'ئ':'’', 'ء':'’', 'ؤ':'w', 'ة':'h', 'ې':'e', 'ڭ':'ŋ',
    'ط':'t', 'غ':'g'
}

# Common multi-letter combos with positional awareness
ARABIC_COMBO = {
    # غي → gi
    'غي':'gi',
    # تيك → tik
    'تيك':'tik',
    # تش → ç
    'تش':'ç',
    # جه → c
    'جه':'c',
    # шл → şl
    'شل':'şl',
    # кш → kş
    'كش':'kş',
    # ла → la
    'لا':'la',
    # уи → wi
    'وي':'wi'
}

def transliterate(text):
    """
    Transliterate Arabic-script Tatar text to Latin
    with positional awareness for ي and other key letters.
    """
    # First, replace common combos
    for combo, repl in ARABIC_COMBO.items():
        text = text.replace(combo, repl)

    # Then transliterate single letters with basic positional rules
    result = ""
    words = text.split()
    for word in words:
        new_word = ""
        for i, c in enumerate(word):
            if c == 'ي':
                # Rules depending on position
                if i == 0:
                    new_word += 'i'   # beginning of word
                elif i == len(word) - 1:
                    new_word += 'i'   # end of word
                else:
                    new_word += 'i'   # middle, could be refined later
            elif c == 'ى':
                new_word += 'y'      # usually ы
            else:
                new_word += ARABIC_SINGLE.get(c, c)
        result += new_word + " "
    return result.strip()

# ========================
# Latin → Cyrillic
# ========================
LATIN_TO_CYRILLIC = {
    'a':'а','b':'б','c':'дж','ç':'ч','d':'д','e':'е','f':'ф',
    'g':'г','h':'һ','i':'и','j':'ж','k':'к','l':'л','m':'м',
    'n':'н','o':'о','p':'п','q':'к','r':'р','s':'с','ş':'ш',
    't':'т','u':'у','w':'в','x':'х','y':'ы','z':'з','ŋ':'ң'
}

def latin_to_cyrillic(text):
    return ''.join(LATIN_TO_CYRILLIC.get(c, c) for c in text)
