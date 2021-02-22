"""Information mapping for pywraps."""

import os

from tqdl import download
import gensim.downloader as gsim_dl

from .cfg import CFG


class EmbeddingType:
    GENSIM = 'gensim'


class Embedding:

    def __init__(
            self, name, link, dlink, mbsize, dimension, vocabsize, tokens,
            ftype):
        self.name = name
        self.link = link
        self.dlink = dlink
        self.mbsize = mbsize
        self.dimension = dimension
        self.vocabsize = vocabsize
        self.tokens = tokens
        self.ftype = ftype
        self._downloaded_once = False
        self._gensim_fpath = None

    def __lazy_init(self):
        pass

    def _exists(self):
        return os.path.isfile(self.fpath)

    def _download(self):
        if self._exists():
            return
        print("Downloading {} to {}...".format(
            self.fname, self.fpath))
        download(self.dlink, self.fpath)
        print("Done.")
        self._downloaded_once = True

        self._generate_vocab_txt_file()
    def _vocab_to_txt(self):
        self._download()
        pass

    @property
    def fname(self):
        return self.name + '.gz'

    @property
    def fpath(self):
        return os.path.join(CFG['datadir'], self.fname)

    @property
    def vocab_fpath(self):
        return os.path.join(CFG['datadir'], self.name + '_vocab.txt')


class GensimEmbedding(Embedding):

    def __init__(self, **kwargs):
        self._gensim_fpath = None
        super().__init__(**kwargs)

    def _exists(self):
        return (self._gensim_fpath is not None)

    def _download(self):
        if self._exists():
            return
        print("Downloading {}...".format(self.name))
        self._gensim_fpath = gsim_dl.load(self.name, return_path=True)
        print("{} downloaded to {}.".format(self.name, self._gensim_fpath))
        self._downloaded_once = True

    @property
    def fpath(self):
        if not self._downloaded_once:
            self._download()
        return self._gensim_fpath


THOUSAND = 1000
MILLION = 1000 * THOUSAND
BILLION = 1000 * MILLION


word2vec_google_news_300 = Embedding(
    name='word2vec_google_news_300',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/word2vec-google-news-300',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/word2vec-google-news-300/word2vec-google-news-300.gz',  # noqa: E501
    mbsize=1600,
    dimension=300,
    vocabsize=3 * MILLION,
    tokens=100 * BILLION,
    ftype='gensim',
)


glove_twitter_200 = Embedding(
    name='glove_twitter_200',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-200',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-200/glove-twitter-200.gz',  # noqa: E501
    mbsize=759,
    dimension=200,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_twitter_100 = Embedding(
    name='glove_twitter_100',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-100',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-100/glove-twitter-100.gz',  # noqa: E501
    mbsize=387,
    dimension=100,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_twitter_50 = Embedding(
    name='glove_twitter_50',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-50',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-50/glove-twitter-50.gz',  # noqa: E501
    mbsize=200,
    dimension=50,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_twitter_25 = Embedding(
    name='glove_twitter_25',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-25',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-25/glove-twitter-25.gz',  # noqa: E501
    mbsize=105,
    dimension=25,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_wiki_gigaword_300 = Embedding(
    name='glove_wiki_gigaword_300',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-300',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-wiki-gigaword-300/glove-wiki-gigaword-300.gz',  # noqa: E501
    mbsize=376,
    dimension=300,
    vocabsize=400 * THOUSAND,
    tokens=5.6 * BILLION,
    ftype='gensim',
)


glove_wiki_gigaword_200 = Embedding(
    name='glove_wiki_gigaword_200',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-200',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-wiki-gigaword-200/glove-wiki-gigaword-200.gz',  # noqa: E501
    mbsize=252,
    dimension=200,
    vocabsize=400 * THOUSAND,
    tokens=5.6 * BILLION,
    ftype='gensim',
)


glove_wiki_gigaword_100 = Embedding(
    name='glove_wiki_gigaword_100',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-100',  # noqa: E501
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-wiki-gigaword-100/glove-wiki-gigaword-100.gz',  # noqa: E501
    mbsize=128,
    dimension=100,
    vocabsize=400 * THOUSAND,
    tokens=5.6 * BILLION,
    ftype='gensim',
)


EMBEDDINGS = [
    word2vec_google_news_300,
    glove_twitter_200,
    glove_twitter_100,
    glove_twitter_50,
    glove_twitter_25,
    glove_wiki_gigaword_300,
    glove_wiki_gigaword_200,
    glove_wiki_gigaword_100,
]
