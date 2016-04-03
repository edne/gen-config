#!/usr/bin/env python
# -*- coding: utf-8 -*-
import i3

from generate_bash import generate_bash
from generate_i3 import generate_i3
from generate_i3bar import generate_i3bar


if __name__ == "__main__":
    generate_bash()
    generate_i3bar()
    generate_i3()
    i3.command("reload")
