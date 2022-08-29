A, B, C, D, E, F, X = map(int, input().split())
Tak1 = X // (A + C) * (B * A)
temp = X % (A + C)
if temp < A:
    Tak2 = temp * B
else:
    Tak2 = A * B

Aok1 = X // (D + F) * (D * E)
temp = X % (D + F)
if temp < D:
    Aok2 = temp * E
else:
    Aok2 = D * E

if Tak1 + Tak2 > Aok1 + Aok2:
    print("Takahashi")
if Tak1 + Tak2 < Aok1 + Aok2:
    print("Aoki")
if Tak1 + Tak2 == Aok1 + Aok2:
    print("Draw")
