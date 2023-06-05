def longest_common_subsequence(s1, s2):
    # Initialize an array to store the lengths of the LCS for each prefix of s1 and s2
    m, n = len(s1), len(s2)
    lcs_lengths = [[0] * (n + 1) for _ in range(m + 1)]

    # Compute the lengths of the LCS for each prefix of s1 and s2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])

    # Construct the LCS from the lengths array
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif lcs_lengths[i - 1][j] > lcs_lengths[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()

    # Return the LCS and its length
    return lcs, lcs_lengths[m][n]
