from nose.tools import assert_equal, assert_raises


class TestMath(object):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        assert_raises(TypeError, prime_generator.generate_primes, None)
        assert_raises(TypeError, prime_generator.generate_primes, 19.1)
        assert_equal(prime_generator.generate_primes(20), [False, False, True, 
                                                           True, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True])
        print('Sua solução foi executada com sucesso! Parabéns!')


def main():
    test = TestMath()
    test.test_generate_primes()


if __name__ == '__main__':
    main()
