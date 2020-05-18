# -*- coding: utf-8 -*-
from enum import Enum, auto


class SYMBOLS(Enum):
    VOWEL = auto()
    VOWEL_SIGN = auto()
    CODA = auto()
    CONSONANT = auto()
    SPECIAL = auto()
    NUMBER = auto()


class IastEntity:
    def __init__(self, iast_element, type):
        self.iast_element = iast_element
        self.type = type


SCHWA_CHARACTER = "a"

devanagari_map = {
    "अ": IastEntity('a', SYMBOLS.VOWEL),
    "आ": IastEntity('ā', SYMBOLS.VOWEL),
    "इ": IastEntity('i', SYMBOLS.VOWEL),
    "ई": IastEntity('ī', SYMBOLS.VOWEL),
    "उ": IastEntity('u', SYMBOLS.VOWEL),
    "ऊ": IastEntity('ū', SYMBOLS.VOWEL),
    "ऋ": IastEntity('ṛ', SYMBOLS.VOWEL),
    "ॠ": IastEntity('ṝ', SYMBOLS.VOWEL),
    "ऌ": IastEntity('ḷ', SYMBOLS.VOWEL),
    "ॡ": IastEntity('ḹ', SYMBOLS.VOWEL),
    "ए": IastEntity('e', SYMBOLS.VOWEL),
    "ऐ": IastEntity('ai', SYMBOLS.VOWEL),
    "ओ": IastEntity('o', SYMBOLS.VOWEL),
    "औ": IastEntity('au', SYMBOLS.VOWEL),

    "ा": IastEntity('ā', SYMBOLS.VOWEL_SIGN),
    "ि": IastEntity('ī', SYMBOLS.VOWEL_SIGN),
    "ी": IastEntity('ī', SYMBOLS.VOWEL_SIGN),
    "ु": IastEntity('u', SYMBOLS.VOWEL_SIGN),
    "ू": IastEntity('ū', SYMBOLS.VOWEL_SIGN),
    "ृ": IastEntity('ṛ', SYMBOLS.VOWEL_SIGN),
    "ॄ": IastEntity('ṝ', SYMBOLS.VOWEL_SIGN),
    "ॢ": IastEntity('ḷ', SYMBOLS.VOWEL_SIGN),
    "ॣ": IastEntity('ḹ', SYMBOLS.VOWEL_SIGN),
    "े": IastEntity('e', SYMBOLS.VOWEL_SIGN),
    "ै": IastEntity('ai', SYMBOLS.VOWEL_SIGN),
    "ो": IastEntity('o', SYMBOLS.VOWEL_SIGN),
    "ौ": IastEntity('au', SYMBOLS.VOWEL_SIGN),
    "्": IastEntity('', SYMBOLS.VOWEL_SIGN),

    "ं": IastEntity('ṁ', SYMBOLS.CODA),
    "ः": IastEntity('ḥ', SYMBOLS.CODA),
    "ँ": IastEntity('m̐', SYMBOLS.CODA),
    "ऽ": IastEntity("'", SYMBOLS.CODA),

    "क": IastEntity('k', SYMBOLS.CONSONANT),
    "ख": IastEntity('kh', SYMBOLS.CONSONANT),
    "ग": IastEntity('g', SYMBOLS.CONSONANT),
    "घ": IastEntity('gh', SYMBOLS.CONSONANT),
    "ङ": IastEntity('ṅ', SYMBOLS.CONSONANT),

    "च": IastEntity('c', SYMBOLS.CONSONANT),
    "छ": IastEntity('ch', SYMBOLS.CONSONANT),
    "ज": IastEntity('j', SYMBOLS.CONSONANT),
    "झ": IastEntity('jh', SYMBOLS.CONSONANT),
    "ञ": IastEntity('ñ', SYMBOLS.CONSONANT),

    "ट": IastEntity('ṭ', SYMBOLS.CONSONANT),
    "ठ": IastEntity('ṭh', SYMBOLS.CONSONANT),
    "ड": IastEntity('ḍ', SYMBOLS.CONSONANT),
    "ढ": IastEntity('ḍh', SYMBOLS.CONSONANT),
    "ण": IastEntity('ṇ', SYMBOLS.CONSONANT),

    "त": IastEntity('t', SYMBOLS.CONSONANT),
    "थ": IastEntity('th', SYMBOLS.CONSONANT),
    "द": IastEntity('d', SYMBOLS.CONSONANT),
    "ध": IastEntity('dh', SYMBOLS.CONSONANT),
    "न": IastEntity('n', SYMBOLS.CONSONANT),

    "प": IastEntity('p', SYMBOLS.CONSONANT),
    "फ": IastEntity('ph', SYMBOLS.CONSONANT),
    "ब": IastEntity('b', SYMBOLS.CONSONANT),
    "भ": IastEntity('bh', SYMBOLS.CONSONANT),
    "म": IastEntity('m', SYMBOLS.CONSONANT),

    "य": IastEntity('y', SYMBOLS.CONSONANT),
    "र": IastEntity('r', SYMBOLS.CONSONANT),
    "ल": IastEntity('l', SYMBOLS.CONSONANT),
    "व": IastEntity('v', SYMBOLS.CONSONANT),

    "श": IastEntity('ś', SYMBOLS.CONSONANT),
    "ष": IastEntity('ṣ', SYMBOLS.CONSONANT),
    "स": IastEntity('s', SYMBOLS.CONSONANT),

    "ह": IastEntity('h', SYMBOLS.CONSONANT),

    "ॐ": IastEntity('oṁ', SYMBOLS.SPECIAL),

    "०": IastEntity('0', SYMBOLS.NUMBER),
    "१": IastEntity('1', SYMBOLS.NUMBER),
    "२": IastEntity('2', SYMBOLS.NUMBER),
    "३": IastEntity('3', SYMBOLS.NUMBER),
    "४": IastEntity('4', SYMBOLS.NUMBER),
    "५": IastEntity('5', SYMBOLS.NUMBER),
    "६": IastEntity('6', SYMBOLS.NUMBER),
    "७": IastEntity('7', SYMBOLS.NUMBER),
    "८": IastEntity('8', SYMBOLS.NUMBER),
    "९": IastEntity('9', SYMBOLS.NUMBER)
}


def devanagari_to_iast(data):
    result = ""
    for idx, ch in enumerate(data):
        if ch in devanagari_map:
            iastEntity = devanagari_map[ch]
            if iastEntity.type == SYMBOLS.CONSONANT:
                result += iastEntity.iast_element
                result += SCHWA_CHARACTER
            elif iastEntity.type == SYMBOLS.VOWEL_SIGN:
                result = result[:-1]
                result += iastEntity.iast_element
            else:
                result += iastEntity.iast_element
        else:
            result += ch

    return result
