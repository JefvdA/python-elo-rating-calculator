"""
For now this main module contains all logic, split up should happen after main calculation is implemented.
Don't bother with command arguments now, we can just hard-code values in this file, or even better, write tests :)

Elo calculation:
Rn = Ro + K * (S - E)

Rn = new elo
Ro = old elo
K = factor for how big elo change should be -> start with 32
S = actual outcome (WIN = 1, DRAW = 0.5, LOSS = 0)
E = expected outcome (see calculation below)

E = 1 / ( 1 + 10^( (Rb - Ra) / c ) )

Rb = the other player's elo
Ra = your elo
c = factor for differentiation between the elo's -> start with 400
"""


def main() -> None:
    print("Hello world!")


if __name__ == '__main__':
    main()
