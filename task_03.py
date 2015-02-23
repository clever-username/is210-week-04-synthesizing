#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Interest rate calculator."""

import decimal

NAME = raw_input('What is your name? ')
PRNCPL = int(raw_input('What is the principal of the loan? '))
DUR = int(raw_input('For how long is this being borrowed? '))
PRE_Q = raw_input('Are you pre-qualified? ').lower()[:1]

if (0 < PRNCPL < 199999) and (DUR <= 15) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('3.63')
elif (0 < PRNCPL <= 199999) and (DUR <= 15) and (PRE_Q == 'n'):
    INT_RT = decimal.Decimal('4.65')
elif (0 < PRNCPL <= 199999) and (16 <= DUR <= 20) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('4.04')
elif (0 < PRNCPL <= 199999) and (16 <= DUR <= 20) and (PRE_Q == 'n'):
    INT_RT = decimal.Decimal('4.98')
elif (0 < PRNCPL <= 199999) and (21 <= DUR <= 30) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('5.77')
elif (0 < PRNCPL <= 199999) and (21 <= DUR <= 30) and (PRE_Q == 'n'):
    INT_RT = decimal.Decimal('6.39')
elif (200000 <= PRNCPL <= 999999) and (DUR <= 15) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('3.02')
elif (200000 <= PRNCPL <= 999999) and (DUR <= 15) and (PRE_Q == 'n'):
    INT_RT = decimal.Decimal('3.98')
elif (200000 <= PRNCPL <= 999999) and (16 <= DUR <= 20) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('3.27')
elif (200000 <= PRNCPL <= 999999) and (16 <= DUR <= 20) and (PRE_Q == 'n'):
    INT_RT = decimal.Decimal('4.08')
elif (200000 <= PRNCPL <= 999999) and (21 <= DUR <= 30) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('4.66')
elif (PRNCPL >= 1000000) and (DUR <= 15) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('2.05')
elif (PRNCPL >= 1000000) and (16 <= DUR <= 20) and (PRE_Q == 'y'):
    INT_RT = decimal.Decimal('2.05')
print INT_RT
# print 'Loan Report for: {N}
"""BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ').title()

if BASE == 'Seattle Gray':
    ACCENT_1 = 'Ceramic Glaze'
    ACCENT_2 = 'Cumulus Nimbus'
elif BASE == 'Manatee':
    ACCENT_1 = 'Platinum Mist'
    ACCENT_2 = 'Spartan Sage'

ACCENT = raw_input('Which accent color, "{A1}" or "{A2}"?: '.format(
     A1=ACCENT_1, A2=ACCENT_2)).title()"""
