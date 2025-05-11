def affine_gap_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w):
    n = len(v)
    m = len(w)

    match_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    gap_open_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    gap_ext_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        match_matrix[i][0] = -float('inf')
        gap_open_matrix[i][0] = -gap_opening_penalty - (i - 1) * gap_extension_penalty

    for j in range(1, m + 1):
        match_matrix[0][j] = -float('inf')
        gap_open_matrix[0][j] = -gap_opening_penalty - (j - 1) * gap_extension_penalty

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = match_matrix[i - 1][j - 1] + (match_reward if v[i - 1] == w[j - 1] else -mismatch_penalty)
            gap_open_score_v = gap_open_matrix[i - 1][j] - gap_extension_penalty - gap_opening_penalty
            gap_open_score_w = gap_open_matrix[i][j - 1] - gap_extension_penalty - gap_opening_penalty
            gap_open_matrix[i][j] = max(gap_open_score_v, gap_open_score_w)
            gap_ext_score_v = gap_ext_matrix[i - 1][j] - gap_extension_penalty
            gap_ext_score_w = gap_ext_matrix[i][j - 1] - gap_extension_penalty
            gap_ext_matrix[i][j] = max(gap_ext_score_v, gap_ext_score_w)

            # Calculate the maximum score at this position
            match_matrix[i][j] = max(match_score, gap_open_matrix[i][j], gap_ext_matrix[i][j])

    i, j = n, m
    aligned_v = []
    aligned_w = []

    while i > 0 and j > 0:
        current_score = match_matrix[i][j]
        match_score = match_matrix[i - 1][j - 1] + (match_reward if v[i - 1] == w[j - 1] else -mismatch_penalty)
        gap_open_score_v = gap_open_matrix[i - 1][j] - gap_extension_penalty - gap_opening_penalty
        gap_open_score_w = gap_open_matrix[i][j - 1] - gap_extension_penalty - gap_opening_penalty

        if current_score == match_score:
            aligned_v.append(v[i - 1])
            aligned_w.append(w[j - 1])
            i -= 1
            j -= 1
        elif current_score == gap_open_score_v:
            aligned_v.append(v[i - 1])
            aligned_w.append('-')
            i -= 1
        else:
            aligned_v.append('-')
            aligned_w.append(w[j - 1])
            j -= 1

    while i > 0:
        aligned_v.append(v[i - 1])
        aligned_w.append('-')
        i -= 1

    while j > 0:
        aligned_v.append('-')
        aligned_w.append(w[j - 1])
        j -= 1

    alignment_score = match_matrix[n][m]
    aligned_v = ''.join(reversed(aligned_v))
    aligned_w = ''.join(reversed(aligned_w))

    return alignment_score, aligned_v, aligned_w

match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty = 1, 3, 2, 1
v = "GA"
w = "GTTA"

# Call the function
alignment_score, aligned_v, aligned_w = affine_gap_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w)

# Output the result
print(alignment_score)
print(aligned_v)
print(aligned_w)
