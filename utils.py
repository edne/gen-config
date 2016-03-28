import os
import stat


def row(*args):
    "Separe arguments with space"
    return " ".join(args)


def lines(*args):
    "Separe arguments with new-line"
    return "\n".join(args)


def indent(*args):
    "Indent each argument with 4 spaces"
    return lines(*["    " + l for l in args])


def quotes(*args):
    "Surround with \""
    return "\"{}\"".format(row(*args))


def write_file(file_name, *body):
    "Write lines on a file"
    with open(file_name, "w") as f:
        f.write(lines(*body))


def write_bash(local_path, name, *code):
    "Generate an executable bash script"
    file_name = os.path.join(local_path, name)

    write_file(file_name, "#!/bin/bash", *code)

    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)


# i3 stuff:
def block(block_header, *args):
    return block_header + " {\n" + indent(*args) + "\n}"


def bindsym(sym, *command):
    return "bindsym {} {}".format(sym, " ".join(command))


def bindsym_exec(sym, *command):
    return "bindsym {} exec {}".format(sym, " ".join(command))


def bindsym_mode(sym, mode_name):
    return "bindsym {} mode \"{}\"".format(sym, mode_name)


def mode(mode_name, *args):
    return block("mode \"" + mode_name + "\"", *args)
#
