# AffineGapAligner


# Description

AffineGapAligner is a Python implementation of the global sequence alignment algorithm with affine gap penalties. This approach improves upon basic alignment by distinguishing between gap openings and gap extensions, resulting in more biologically realistic alignments.
The function uses three dynamic programming matrices and performs traceback to generate the optimal alignment between two sequences, minimizing the total penalty for mismatches and gaps.


# Features
* Supports affine gap penalty model:
* Separate penalties for opening a gap and extending it.
* Returns both the optimal alignment score and the aligned sequences.
* Uses three dynamic programming matrices:
* Match/mismatch matrix
* Gap opening matrix
* Gap extension matrix

#  Function
affine_gap_alignment(match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w)
Purpose:
Finds the global alignment of two sequences using affine gap penalties and returns the best alignment and its score.



# Parameters
* match_reward (int): Score for a character match (e.g., 1)
* mismatch_penalty (int): Penalty for mismatched characters (e.g., 3)
* gap_opening_penalty (int): Cost to open a new gap (e.g., 2)
* gap_extension_penalty (int): Cost to extend an existing gap (e.g., 1)
* v (str): First sequence (e.g., "GA")
* w (str): Second sequence (e.g., "GTTA")

# Returns
* int: Alignment score
* str: Aligned version of sequence v
* str: Aligned version of sequence w

# Example
```
match_reward = 1
mismatch_penalty = 3
gap_opening_penalty = 2
gap_extension_penalty = 1

v = "GA"
w = "GTTA"

score, aligned_v, aligned_w = affine_gap_alignment(
    match_reward, mismatch_penalty, gap_opening_penalty, gap_extension_penalty, v, w
)

print("Score:", score)
print("Aligned v:", aligned_v)
print("Aligned w:", aligned_w)
```

# Output

0
G--A
GTTA

# Applications
* Bioinformatics: Protein and DNA sequence alignment in genomics.
* Comparative Genomics: Detecting insertions, deletions, and substitutions.
* Sequence Evolution Analysis: Models evolutionary distances with more realistic gap handling.

# Requirements
* Python 3.x
* No external libraries required.

# License
* This project is licensed under the MIT License. See the LICENSE file for more details.




