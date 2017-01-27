#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import time


def MoneyFormat(number):
    """ transform a number to money format (CLP)
    """
    return '$' + str(format(math.floor(number * 100) / 100, ',.0f'))


class Timer(object):
    """ timer to detect execution time

    @sample:
        with Timer() as timer:
            print "executing some code"

        time += timer.msecs
        total_time += timer.secs
    """

    def __init__(self, verbose=False):
        """ default constructor

        @param verbose if true, enable logs
        """
        self.verbose = verbose
        self.start_time = 0
        self.end_time = 0

    def start(self):
        """ the timer start to count
        """
        self.start_time = time.time()

    def end(self):
        """ the timer end to count
        """
        self.end_time = time.time()
        self.secs = self.end_time - self.start_time
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.end()
