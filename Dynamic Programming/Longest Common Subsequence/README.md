# Longest Common Subsequence with Dynamic Programming

This is a Python implementation of the longest common subsequence problem using dynamic programming. Given two sequences `s1` and `s2`, the goal is to find the longest subsequence that is common to both sequences.

## Dynamic Programming Approach

The key idea behind the dynamic programming approach to this problem is to break it down into smaller subproblems and store the results of those subproblems in an array. Specifically, we can define an array `lcs_lengths` such that `lcs_lengths[i][j]` represents the length of the LCS for the prefixes of `s1` and `s2` up to lengths `i` and `j`, respectively. We can then fill in this array iteratively, starting with `lcs_lengths[0][0] = 0` and working our way up to `lcs_lengths[m][n]`, where `m` and `n` are the lengths of `s1` and `s2`, respectively.

To compute `lcs_lengths[i][j]`, we need to consider the last character of each sequence. If the last characters match (`s1[i-1] == s2[j-1]`), then the length of the LCS is one greater than the length of the LCS for the prefixes without the last character (`lcs_lengths[i-1][j-1]`). Otherwise, the length of the LCS is the maximum of the lengths of the LCS for the prefixes without the last character from `s1` (`lcs_lengths[i-1][j]`) and `s2` (`lcs_lengths[i][j-1]`).

Once we have computed the lengths of the LCS for each prefix of `s1` and `s2`, we can construct the LCS itself by working backwards from the end of the sequences. If the last characters match, then they must be part of the LCS, so we add them to the subsequence and move on to the next characters (`i -= 1` and `j -= 1`). Otherwise, we look at the previous entries in the `lcs_lengths` array to determine which direction to move in (`i -= 1` or `j -= 1`). We continue this process until we reach the beginning of one of the sequences.

By computing the length of the LCS and constructing the LCS itself using dynamic programming, we can solve the longest common subsequence problem in O(mn) time, where `m` and `n` are the lengths of `s1` and `s2`, respectively. This is much faster than the brute force approach of considering all possible subsequences of both sequences, which would take O(2^(m+n)) time.

## Usage

To use the `longest_common_subsequence` function, simply provide two strings `s1` and `s2`. The function returns a tuple containing the longest common subsequence (as a list of characters) and its length.

```python
s1 = "AGGTAB"
s2 = "GXTXAYB"

lcs, length = longest_common_subsequence(s1, s2)
print("Longest common subsequence:", "".join(lcs))
print("Length:", length)
```

This will output the following result:

```
Longest common subsequence: GTAB
Length: 4
```

which means that the longest common subsequence of the strings "AGGTAB" and "GXTXAYB" is "GTAB", with a length of 4.