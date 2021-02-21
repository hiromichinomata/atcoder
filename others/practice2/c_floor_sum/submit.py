import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder__math_code = """
import typing


def _is_prime(n: int) -> bool:
    '''
    Reference:
    M. Forisek and J. Jancina,
    Fast Primality Testing for Integers That Fit into a Machine Word
    '''

    if n <= 1:
        return False
    if n == 2 or n == 7 or n == 61:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in (2, 7, 61):
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


def _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
    a %= b
    if a == 0:
        return (b, 0)

    # Contracts:
    # [1] s - m0 * a = 0 (mod b)
    # [2] t - m1 * a = 0 (mod b)
    # [3] s * |m1| + t * |m0| <= b
    s = b
    t = a
    m0 = 0
    m1 = 1

    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b

        # [3]:
        # (s - t * u) * |m1| + t * |m0 - m1 * u|
        # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)
        # = s * |m1| + t * |m0| <= b

        s, t = t, s
        m0, m1 = m1, m0

    # by [3]: |m0| <= b/g
    # by g != b: |m0| < b/g
    if m0 < 0:
        m0 += b // s

    return (s, m0)


def _primitive_root(m: int) -> int:
    if m == 2:
        return 1
    if m == 167772161:
        return 3
    if m == 469762049:
        return 3
    if m == 754974721:
        return 11
    if m == 998244353:
        return 3

    divs = [2] + [0] * 19
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2

    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2

    if x > 1:
        divs[cnt] = x
        cnt += 1

    g = 2
    while True:
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1:
                break
        else:
            return g
        g += 1
"""

atcoder._math = types.ModuleType('atcoder._math')
exec(_atcoder__math_code, atcoder._math.__dict__)


_atcoder_math_code = """
import typing

# import atcoder._math


def inv_mod(x: int, m: int) -> int:
    assert 1 <= m

    z = atcoder._math._inv_gcd(x, m)

    assert z[0] == 1

    return z[1]


def crt(r: typing.List[int], m: typing.List[int]) -> typing.Tuple[int, int]:
    assert len(r) == len(m)

    n = len(r)

    # Contracts: 0 <= r0 < m0
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue

        # assume: m0 > m1, lcm(m0, m1) >= 2 * max(m0, m1)

        '''
        (r0, m0), (r1, m1) -> (r2, m2 = lcm(m0, m1));
        r2 % m0 = r0
        r2 % m1 = r1
        -> (r0 + x*m0) % m1 = r1
        -> x*u0*g % (u1*g) = (r1 - r0) (u0*g = m0, u1*g = m1)
        -> x = (r1 - r0) / g * inv(u0) (mod u1)
        '''

        # im = inv(u0) (mod u1) (0 <= im < u1)
        g, im = atcoder._math._inv_gcd(m0, m1)

        u1 = m1 // g
        # |r1 - r0| < (m0 + m1) <= lcm(m0, m1)
        if (r1 - r0) % g:
            return (0, 0)

        # u1 * u1 <= m1 * m1 / g / g <= m0 * m1 / g = lcm(m0, m1)
        x = (r1 - r0) // g % u1 * im % u1

        '''
        |r0| + |m0 * x|
        < m0 + m0 * (u1 - 1)
        = m0 + m0 * m1 / g - m0
        = lcm(m0, m1)
        '''

        r0 += x * m0
        m0 *= u1  # -> lcm(m0, m1)
        if r0 < 0:
            r0 += m0

    return (r0, m0)


def floor_sum(n: int, m: int, a: int, b: int) -> int:
    assert 1 <= n
    assert 1 <= m

    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)

    return ans
"""

atcoder.math = types.ModuleType('atcoder.math')
atcoder.math.__dict__['atcoder'] = atcoder
atcoder.math.__dict__['atcoder._math'] = atcoder._math
exec(_atcoder_math_code, atcoder.math.__dict__)
floor_sum = atcoder.math.floor_sum

#!/bin/python3

import sys
input = sys.stdin.readline
# from atcoder.math import floor_sum

def main():
  t = list(map(int, input().strip().split()))[0]
  for _ in range(t):
    n, m, a, b = list(map(int, input().strip().split()))
    print(floor_sum(n, m, a, b))

main()
