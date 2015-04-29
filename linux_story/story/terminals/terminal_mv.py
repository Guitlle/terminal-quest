#!/usr/bin/env python

#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# A terminal for one of the challenges

import os
import sys

dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if __name__ == '__main__' and __package__ is None:
    if dir_path != '/usr':
        sys.path.insert(1, dir_path)

from linux_story.story.terminals.terminal_cd import TerminalCd
from linux_story.commands_real import shell_command


class TerminalMv(TerminalCd):
    commands = ["ls", "cat", "cd", "mv"]

    def do_mv(self, line):
        shell_command(self.real_path, line, "mv")

    def complete_mv(self, text, line, begidx, endidx):
        completions = self.autocomplete_files(text, line, begidx, endidx)
        return completions


if __name__ == "__main__":
    start_path = '~'
    end_path = '~/my-house'

    def check_command(arg1=None, arg2=None):
        pass

    def block_command(arg1=None, arg2=None):
        pass

    def check_output(arg1=None, arg2=None):
        pass

    terminal = TerminalMv(
        start_path,
        end_path,
        check_command,
        block_command,
        check_output
    )

    terminal.cmdloop()
