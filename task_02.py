#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python alarm clock."""

DAY = raw_input('What day is it?: ').lower()[:3]
TIME = int(raw_input('What time is it?: '))

SNOOZE = True if (DAY == 'sat' or DAY == 'sun') or TIME < 600 else False

if SNOOZE is False:
    print 'Beep! '*5
