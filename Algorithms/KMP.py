from random import randint


def KMP(subseq, seq) -> int:
    """Knuth–Morris–Pratt algorithm. Complexity: O(n+m), Memory-complexity: O(m), m - subsequence length)"""
    prefix_array = create_prefix_array(subseq)
    similar_symbols_count = 0
    for i in range(1, len(seq)+1):
        while similar_symbols_count >= 0:
            if subseq[similar_symbols_count] == seq[i-1]:
                break
            similar_symbols_count = prefix_array[similar_symbols_count]
        similar_symbols_count += 1
        if similar_symbols_count == len(subseq):
            return i - similar_symbols_count
    return -1


def create_prefix_array(lst) -> list:
    prefix_array = [0] * (len(lst) + 1)
    prefix_array[0] = -1
    for i in range(1, len(lst)+1):
        alpha = prefix_array[i - 1]
        while alpha >= 0:
            if lst[alpha] == lst[i-1]:
                break
            alpha = prefix_array[alpha]
        prefix_array[i] = alpha + 1

    return prefix_array


if __name__ == '__main__':
    iterations_count = 1000
    sequence_length = 100
    subsequence_length = 5

    for i in range(1, iterations_count+1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")
        sequence = [randint(-2*sequence_length, 2*sequence_length) for _ in range(sequence_length)]
        if randint(0, 1):
            start_index = randint(0, sequence_length-1)
            subsequence = sequence[start_index:min(start_index+subsequence_length, sequence_length)]
        else:
            subsequence = [randint(-sequence_length, sequence_length) for _ in range(subsequence_length)]
        sequence = ' '.join(map(str, sequence))
        subsequence = ' '.join(map(str, subsequence))

        assert sequence.find(subsequence) == KMP(subsequence, sequence)
    print("\nTests passed!")
