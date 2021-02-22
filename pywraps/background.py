"""Code for one-time operations."""

import gensim.downloader as gensim_downloader
# from gensim.models.keyedvectors import Doc2VecKeyedVectors


def embedding_to_vocab_txt(embedding):
    """Extracts the vocabulary of the given embedding and writes it to text."""
    if embedding.ftype == 'gensim':
        gensim_embedding_to_vocab_txt(embedding)
    else:
        raise ValueError('Unknown embedding type!')


def gensim_embedding_to_vocab_txt(embedding):
    gensim_name = embedding.name.replace('_', '-')
    print('Downloading gensim corpus {}...'.format(gensim_name))
    model = gensim_downloader.load(gensim_name)
    with open(embedding.vocab_fpath, 'wt+') as f:
        for word in model.vocab:
            f.write('{word}\n')
