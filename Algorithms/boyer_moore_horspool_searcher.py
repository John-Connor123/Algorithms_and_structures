from random import randint


def boyer_moore_horspool_searcher(subseq, seq) -> int:
    """Boyer–Moore–Horspool algorithm or Horspool's algorithm.
        Average-complexity: E(T(m, n)) = O(m/Z), where Z = len(set(subseq + seq)). Best case: O(n/m), worse case: O(m*n).
        Memory-complexity: O(Z_m), where Z_m = len(set(subseq))."""
    offset_dict = create_offset_dict(subseq)
    i = m = len(subseq) - 1
    while i < len(seq):
        if seq[i-m:i+1] == subseq:
            return i - m
        i += offset_dict.get(seq[i], len(subseq))
    return -1


def create_offset_dict(lst) -> dict:
    offset_dict = {}
    for i in range(len(lst)-1):
        offset_dict[lst[i]] = len(lst) - (i + 1)
    return offset_dict


if __name__ == '__main__':
    print("Description of function boyer_moore_horspool_searcher:\n", boyer_moore_horspool_searcher.__doc__)
    iterations_count = 10000
    sequence_length = 100

    for i in range(1, iterations_count+1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")

        sequence = [randint(-2*sequence_length, 2*sequence_length) for _ in range(sequence_length)]
        start_index = randint(0, sequence_length - 1)
        subsequence_length = randint(start_index, sequence_length - 1) - start_index

        is_slice_from_sequence = randint(0, 1)
        if is_slice_from_sequence:
            subsequence = sequence[start_index:start_index+subsequence_length]
        else:
            subsequence = [randint(-sequence_length, sequence_length) for _ in range(subsequence_length)]
        sequence = ' '.join(map(str, sequence))
        subsequence = ' '.join(map(str, subsequence))

        assert sequence.find(subsequence) == boyer_moore_horspool_searcher(subsequence, sequence)
    print("\nTests passed!")
