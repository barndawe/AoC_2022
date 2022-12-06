def main():
    marker_length = 14

    with open("input.txt") as input:
        data_stream = input.readline()

    for marker_end_idx in range(marker_length - 1, len(data_stream)):
        potential_marker = data_stream[marker_end_idx - marker_length: marker_end_idx]
        if len(set(potential_marker)) == marker_length:
            print(marker_end_idx)
            break

if __name__ == "__main__":
    main()