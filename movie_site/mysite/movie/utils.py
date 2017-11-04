#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_int_or_zero(n):
    try:
        return int(n)
    except (ValueError, TypeError):
        return 0
