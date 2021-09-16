# -*- coding: utf-8 -*-
from collections import defaultdict
from textblob import TextBlob


def count_words(text) -> dict:
    """
    В самом примитивном варианте эта функция будет лепить к словам знаки
    препинания, от которых они не отделены
    В принципе, можно сначала удалить все знаки препинания функцией
    remove_punctuation, а затем уже вызвать эту функцию от
    нового текста
    А ещё можно установить textblob
    :param text: строка пользователя
    :return: словарь частот слов
    """
    return TextBlob(text).word_counts


def remove_words(text) -> str:
    """
    Удаляет слова "a", "the", "any"
    Опять-таки, можем удалить знаки препинания, а то вхождения вроде
    "any," останутся в тексте
    или можно установить TextBlob
    :param text: строка пользователя
    :return: новая строка
    """

    banned_words = {'a', 'the', 'any'}

    return ' '.join([word for word in TextBlob(text).words
                     if word not in banned_words])


def remove_punctuation(text) -> str:
    """
    Удаляет все знаки препинания из текста (на самом деле, непонятно,
    что считать знаками препинания. Нужно ли удалять апостроф из "I'm",
    пробелы, дефисы и т.д.
    Я считал, что удаляем заранее зафиксированный набор символов
    :param text: текст (строка) пользователя
    :return: новый текст (строка) без знаков препинания
    """
    new_text = []
    banned_symbols = {':', ';', '.', ',', '?', '!', '—',
                      '\'', '\"', '(', ')', '[', ']', '{', '}'}
    for char in text:
        if char not in banned_symbols:
            new_text.append(char)

    return ''.join(new_text)


def count_phrase(text, phrase) -> int:
    """
    можно просто вызвать text.count(phrase)
    можно text.lower().count(phrase.lower()), чтобы учесть регистр
    можно удалить все знаки препинания, а потом искать
    если мы ищем именно предложение, можно сделать сплит по точкам
    безграничные возможности
    или textblob
    :param text: строка, в которой ищем текст
    :param phrase: текст, который ищем
    :return: количество вхождений
    """
    return TextBlob(text).noun_phrases.count(phrase)


def list_phrases_with_nouns(text) -> list:
    """
    видимо, имеется в виду поиск предложений с существительными
    замечу, что это почти любое предложение
    воспользуемся силой интернета и нестандартных библиотек
    :param text: строка пользователя
    :return: список предложений, в которых есть существительные
    """
    return TextBlob(text).noun_phrases