def maximum_proficiency_level(N, M, A, B):
    opponents = sorted(zip(A, B), key=lambda x: x[0])
    for proficiency, increase in opponents:
        if M >= proficiency:
            M += increase
        else:
            break
    return M


N1, M1 = 4, 2
A1 = [8, 9, 3, 2]
B1 = [5, 4, 1, 3]
print(f"Output 1: {maximum_proficiency_level(N1, M1, A1, B1)}")

N2, M2 = 5, 3
A2 = [8, 4, 5, 6, 7]
B2 = [9, 8, 7, 5, 6]
print(f"Output 2: {maximum_proficiency_level(N2, M2, A2, B2)}")

N3, M3 = 5, 9
A3 = [2, 3, 6, 7, 8]
B3 = [3, 4, 2, 2, 3]
print(f"Output 3: {maximum_proficiency_level(N3, M3, A3, B3)}")
