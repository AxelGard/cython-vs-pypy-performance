from . import config
from . import cy

__version__ = "0.1.0"

def main():
    print(cy.primes(100))


if __name__ == '__main__':
    if config.CONFIG['debug']:
        main()
