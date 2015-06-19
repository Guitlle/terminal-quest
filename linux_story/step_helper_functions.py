#!/usr/bin/env python

# step_helper_functions.py
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Functions specific for use in Step class

import os


def unblock_commands(line, list_of_commands):
    '''Blocks the command that start with cd and mv unless the command is in
    list_of_commands
    '''

    line = line.strip()
    if ("mv" in line or "cd" in line) and \
            line not in list_of_commands and \
            not line.strip() == 'mv --help':

        print 'Nice try! But you do not need that command for this challenge'
        return True


def unblock_commands_with_cd_hint(line, list_of_commands):
    '''Unblocks the commands and informs the user
    '''
    line = line.strip()
    if ("cd" in line and line not in list_of_commands):
        print "You're close, but you entered an unexpected destination path. Try going somewhere else."
        return True

    elif ("mv" in line) and \
            not line.strip() == 'mv --help':

        print 'Nice try! But you do not need that command for this challenge'
        return True


def unblock_commands_with_mkdir_hint(line, list_of_commands):
    line = line.strip()
    if ("mkdir" in line and line not in list_of_commands):
        print (
            "Nearly there!  But you're trying to build something "
            "different from what was expected.  Try building something else."
        )

        return True

    elif ("mv" in line or "cd" in line) and \
            not line.strip() == 'mv --help':

        print 'Nice try! But you do not need that command for this challenge'
        return True


def unblock_cd_commands(line):
    if line.startswith("mkdir") or \
            (line.startswith("mv") and not line.strip() == 'mv --help'):
        print 'Nice try! But you do not need that command for this challenge'
        return True


def find_common_parent(path1, path2):
    # Assume they are in the same form,
    # as absolute fake paths, e.g.
    # ~/town/.hidden-shelter and
    # ~/farm/barn/.shelter

    dirs1 = path1.split("/")
    dirs2 = path2.split("/")

    if len(dirs1) >= len(dirs2):
        a = dirs1
        b = dirs2
    else:
        a = dirs2
        b = dirs1

    # len(dirs_b) <= len(dirs_a)
    # This doesn't always work, if there are directories with the same
    # name in multiple places, this will concatenate them.
    common_dirs = [x for x in b if a[b.index(x)] == x]
    common_path = '/'.join(common_dirs)
    return common_path


# TODO: this will break if we have two paths with directories with
# the same name but in different places.
def route_between_paths(start_path, end_path):
    # Assume they are in the same form,
    # as absolute fake paths, e.g.
    # ~/town/.hidden-shelter and
    # ~/farm/barn/.shelter

    common_path = find_common_parent(start_path, end_path)

    start_split = start_path.split(common_path)
    if len(start_split) != 2:
        raise Exception("common_path is not correct")

    end_split = end_path.split(common_path)
    if len(end_split) != 2:
        raise Exception("common_path is not correct")

    start_diff = start_split[1]
    end_diff = end_split[1]

    start_dirs = filter(None, start_diff.split("/"))
    end_dirs = filter(None, end_diff.split("/"))

    a_dest_path = start_path
    dest_paths = []

    for d in start_dirs[::-1]:
        a_dest_path = a_dest_path.replace(d, "")

        if a_dest_path.endswith("//"):
            a_dest_path = a_dest_path[:-2]
        if a_dest_path.endswith("/"):
            a_dest_path = a_dest_path[:-1]

        a_dest_path = os.path.expanduser(a_dest_path)
        dest_paths.append(a_dest_path)

    for d in end_dirs:
        a_dest_path = os.path.join(a_dest_path, d)
        a_dest_path = os.path.expanduser(a_dest_path)
        dest_paths.append(a_dest_path)

    return dest_paths
