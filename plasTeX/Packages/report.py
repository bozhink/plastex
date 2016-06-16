#!/usr/bin/env python


def ProcessOptions(options, document):
    import book
    book.ProcessOptions(options, document)
    document.context['theequation'].format = '${equation}'
