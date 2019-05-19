from django.core.exceptions import ValidationError
import re


CNPJ_WEIGHTS = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def cnpj_calculate_first_digit(cnpj):
    """This method calculates the first check digit given the 12 first digits of a CNPJ"""

    check_digit = sum([i * int(j) for i, j in zip(CNPJ_WEIGHTS[1:], cnpj[:12])]) % 11
    return 0 if check_digit < 2 else 11 - check_digit


def cnpj_calculate_second_digit(cnpj):
    """This method calculates the second check digit given the 13 first digits (containing the 1st check digit)
    of a CNPJ"""

    check_digit = sum([i * int(j) for i, j in zip(CNPJ_WEIGHTS, cnpj[:13])]) % 11
    return 0 if check_digit < 2 else 11 - check_digit


def cnpj_validate_check_digits(cnpj):
    """Return True if the given CNPJ is Valid and have the correct check digits"""
    first_check_digit = int(cnpj[12])
    second_check_digit = int(cnpj[13])

    if (cnpj_calculate_first_digit(cnpj) != first_check_digit) or (cnpj_calculate_second_digit(cnpj) != second_check_digit):
        return False

    return True

def cnpj_validator(cnpj):
    """Validator for the CNPJ field. It is validating the variables size, the mask and the check digits"""
    if len(cnpj) != 18:
        raise ValidationError('The CNPJ {0} must have 18 characters'.format(cnpj))

    if not re.match(r'[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}', cnpj):
        raise ValidationError('The CNPJ {0} must have 14 numerics in a total of 18 characters, '
                              'following the format: 99.999.999/9999-99'.format(cnpj))

    cnpj_number = str(re.sub(r'[^0-9]', '', cnpj))

    if not cnpj_validate_check_digits(cnpj_number):
        raise ValidationError('Incorrect CNPJ. The {0} check digits are not correct.'.format(cnpj))

