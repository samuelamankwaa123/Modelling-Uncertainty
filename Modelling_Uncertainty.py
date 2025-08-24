# Fixed version: import numpy and use total_people (not sample_size) when
# computing SDs for expected counts out of 100.

import numpy as np

# --- Inputs
total_people = 100
sample_size = 20
L_count, M_count, S_count = 7, 10, 3
assert L_count + M_count + S_count == sample_size

# --- Sample proportions
L_prob = L_count / sample_size
M_prob = M_count / sample_size
S_prob = S_count / sample_size

# --- Expected counts out of total_people
expected_L = (L_prob * total_people)
expected_M = (M_prob * total_people)
expected_S = (S_prob * total_people)

# --- Binomial SD for counts out of total_people
def binomial_sd(n, p):
    return np.sqrt(n * p * (1 - p))

sd_L = binomial_sd(total_people, L_prob)
sd_M = binomial_sd(total_people, M_prob)
sd_S = binomial_sd(total_people, S_prob)

# --- 68% (≈1 SD) ranges for counts
range_L = (expected_L - sd_L, expected_L + sd_L)
range_M = (expected_M - sd_M, expected_M + sd_M)
range_S = (expected_S - sd_S, expected_S + sd_S)

print(f"E[L]={expected_L:.1f}, E[M]={expected_M:.1f}, E[S]={expected_S:.1f}")
print(f"Range L: {range_L[0]:.2f}–{range_L[1]:.2f}")
print(f"Range M: {range_M[0]:.2f}–{range_M[1]:.2f}")
print(f"Range S: {range_S[0]:.2f}–{range_S[1]:.2f}")

