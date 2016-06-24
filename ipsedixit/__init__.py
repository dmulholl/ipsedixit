# --------------------------------------------------------------------------
# Markov-chain pseudo-Latin text generator.
#
# To generate a list of n paragraphs:
#
#     >>> import ipsedixit
#     >>> generator = ipsedixit.Generator()
#     >>> paragraphs = generator.paragraphs(n)
#
# Author: Darren Mulholland <darren@mulholland.xyz>
# License: Public Domain
# --------------------------------------------------------------------------

import os
import argparse

from . import markov
from . import meta


class Generator(markov.MarkovGenerator):

    def __init__(self, text='tacitus'):
        super().__init__()
        if text in ('caesar', 'tacitus'):
            filepath = os.path.join(os.path.dirname(__file__), text + '.txt')
            with open(filepath, encoding='utf-8') as srcfile:
                text = srcfile.read()
        self.add_text(text)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('num',
        nargs = '?',
        default = 4,
        type = int,
        help = 'number of paragraphs to generate (default: %(default)s)',
    )
    parser.add_argument('-v', '--version',
        action='version',
        version=meta.__version__,
    )
    parser.add_argument('--min',
        default = 2,
        type = int,
        help = 'min number of sentences per paragraph (default: %(default)s)',
    )
    parser.add_argument('--max',
        default = 4,
        type = int,
        help = 'max number of sentences per paragraph (default: %(default)s)',
    )
    return parser.parse_args()


def cli():
    args = parse_args()
    generator = Generator()
    print('\n\n'.join(generator.paragraphs(args.num, args.min, args.max)))
