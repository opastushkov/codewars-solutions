def integrate(coefficient, exponent):
    return '{0}x^{1}'.format(coefficient/(exponent + 1), exponent + 1).replace('.0', '') if not coefficient/(exponent + 1) % 1 else '{0}x^{1}'.format(coefficient/(exponent + 1), exponent + 1) 