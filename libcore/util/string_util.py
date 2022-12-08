#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class StringUtil:
    @staticmethod
    def is_empty(s: str) -> bool:

        if s is None:
            return False

        if len(s) <= 0:
            return False

        s_trimmed = s.strip()

        if len(s_trimmed) <= 0:
            return False

        return True


if __name__ == '__main__':
    pass
