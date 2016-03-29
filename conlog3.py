#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-


import termcolor


class ConLog3(object):
    """Console Logging class"""

    _PREFIX = {
        "info": "[*]",
        "succ": "[+]",
        "fail": "[-]",
        "warn": "[!]",
        "debug": "[debug]",
        "error": "[error]"
    }

    _ATTRS = []

    def __init__(self, bold=False):
        """Constructor"""
        if bold:
            self._ATTRS.append("bold")

    def info(self, message):
        """Prints an 'information' message on the standard output"""
        print("{0} {1}".format(termcolor.colored(self._PREFIX['info'], "blue", attrs=self._ATTRS), message))

    def succ(self, message):
        """Prints a 'success' message on the standard output"""
        print("{0} {1}".format(termcolor.colored(self._PREFIX['succ'], "green", attrs=self._ATTRS), message))

    def fail(self, message):
        """Prints a 'fail'  message on the standard output"""
        print("{0} {1}".format(termcolor.colored(self._PREFIX['fail'], "red", attrs=self._ATTRS), message))

    def warn(self, message):
        """Prints a 'warning' message on the standard output"""
        print("{0} {1}".format(termcolor.colored(self._PREFIX['warn'], "yellow", attrs=self._ATTRS), message))

    def debug(self, message):
        """Prints a 'debugging' message on the standard output"""
        print("{0} {1}".format(termcolor.colored(self._PREFIX['debug'], "magenta", attrs=self._ATTRS), message))

    def error(self, message):
        """Prints an 'error' message on the standard output"""
        print("{0}".format(termcolor.colored(self._PREFIX['error'] + " " + message, "red", attrs=self._ATTRS)))

    def header(self, message, level=0):
        """Prints a 'heading' message on the standard output"""
        if level == 0:
            delim = '-' * len(message)
            output = termcolor.colored(delim + '\n' + message.upper() + '\n' + delim, "white", attrs=self._ATTRS)
            print("{0}".format(output))
        else:
            delim = '-' * len(message)
            output = termcolor.colored(message + '\n' + delim, "white", attrs=self._ATTRS)
            print("{0}".format(output))


if __name__ == '__main__':

    clog = ConLog3(bold=True)
    clog.info("ok")
    clog.succ("ok")
    clog.warn("ok")
    clog.fail("ok")
    clog.debug("ok")
    clog.error("ok")

    clog.header("hello", level=1)
    clog.header("hello")
