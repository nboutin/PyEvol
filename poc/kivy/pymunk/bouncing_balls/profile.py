'''
Created on 16 juil. 2019

@author: nboutin
'''

import pstats
from pstats import SortKey

if __name__ == '__main__':
    """
    python3 -m cProfile -o bouncing_ball.cprof main.py 
    """
    p = pstats.Stats('bouncing_ball.cprof')
    
#     p.strip_dirs().sort_stats(-1).print_stats()

#     p.sort_stats(SortKey.NAME)
#     p.print_stats()

    # what algorithms are taking time
    p.sort_stats(SortKey.CUMULATIVE).print_stats(10)

    # what functions were looping a lo
    p.sort_stats(SortKey.TIME).print_stats(10)
