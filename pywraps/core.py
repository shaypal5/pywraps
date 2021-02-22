"""Core functionality for the pywraps package."""

from .util import string_iter_to_vocab_counter
from .info import EMBEDDINGS


def _vocab_pair_intersect_test(ref_vocab, sec_vocab):
    """Returns the coverage ratio of words in a reference vocabulary.

    Parameters
    ----------
    ref_vocab : iterable of strings
        The reference vocabulary. The ratio of words in this vocabulary that
        are also in the secondary vocabulary is returned.
    sec_vocab : iterable of strings
        The secondary vocabulary, against which word coverage is checked.

    Returns
    -------
    float
        A number between 0 and 1, representing the ratio of words in the
        reference vocabulary found in the secondary vocabulary.
    """
    inter = set(ref_vocab).intersection(set(sec_vocab))
    return len(inter) / len(ref_vocab)


def vocab_intersect_test(text):
    pass


def select_embedding(texts):
    for embedding in EMBEDDINGS:
        pass
