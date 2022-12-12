#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class StringUtil:
    @staticmethod
    def is_empty(s: str) -> bool:

        if s is None:
            return True

        if len(s) <= 0:
            return True

        s_trimmed = s.strip()

        if len(s_trimmed) <= 0:
            return True

        return False


if __name__ == '__main__':
    pass
