# --------------------------------------------------------------------------
# Markov chain random text generator.
# --------------------------------------------------------------------------

import random
import itertools
import re


# We don't want to mistake these abbreviations for sentence endings.
abbreviations = (
    'a.d.', 'b.c.', 'c.', 'cf.', 'cn.', 'col.', 'dr.', 'e.g.',
    'ff.', 'fl.', 'id.', 'i.e.', 'kal.', 'mr.', 'mrs.',
    'n.b.', 'p.s.', 'q.v.', 's.c.',
)


# Problematic characters and comments to strip from input text.
strip_regex = re.compile(r'\(|\)|\[|\]|"|_|-|\+|^#.*\n', re.MULTILINE)


class MarkovGenerator:

    def __init__(self):
        self.table = {}
        self.startkeys = []

    def add_text(self, text):
        """ Add input text to the lookup table of word triples. """
        w1, w2 = '', ''
        for word in strip_regex.sub('', text).split():
            if self._is_sentence_end(w2):
                self.startkeys.append((w1, w2))
            self.table.setdefault((w1, w2), []).append(word)
            w1, w2 = w2, word
        self.table.setdefault((w1, w2), []).append('')

    def _is_sentence_end(self, word):
        """ Simple heuristic for detecting the end of a sentence. """
        if word == '' or word[-1] in '!?':
            return True
        if word[-1] != '.' or len(word) == 2:
            return False
        if word.lower() in abbreviations:
            return False
        else:
            return True

    def sentences(self, n, seed=None):
        """ Returns a list of `n` sentences.

        If a `seed` (a two-word string) is specified and can be matched, the
        first sentence will start with those words. If `seed` cannot be matched,
        an empty list will be returned.
        """
        sentence, sentences = [], []
        if seed:
            w1, w2 = seed.split()
            if (w1, w2) in self.table:
                sentence = [seed]
            else:
                return []
        else:
            w1, w2 = random.choice(self.startkeys)
        while len(sentences) < n:
            word = random.choice(self.table[(w1, w2)])
            if word == '':
                w1, w2 = random.choice(self.startkeys)
                word = random.choice(self.table[(w1, w2)])
            sentence.append(word)
            if self._is_sentence_end(word):
                sentences.append(' '.join(sentence))
                sentence = []
            w1, w2 = w2, word
        return sentences

    def paragraphs(self, n, min=2, max=4, seed=None):
        """ Returns a list of `n` paragraphs.

        Each paragraph will have between `min` and `max` sentences.

        If a `seed` (a two word string) is specified and can be matched, the
        first sentence of the first paragraph will start with those words. If
        `seed` cannot be matched, an empty list will be returned.
        """
        lengths = [random.randint(min, max) for i in range(n)]
        sentences = self.sentences(sum(lengths), seed)
        if not sentences:
            return []
        end = list(itertools.accumulate(lengths))
        start = [0] + end[:]
        return [' '.join(sentences[start[i]:end[i]]) for i in range(n)]
