# python3


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2, -1, -1):
        swaps = heapify(data, i, swaps)
    return swaps

def heapify(data, i, swaps):
    n = len(data)
    min_idx = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and data[l] < data[min_idx]:
        min_idx = l
    if r < n and data[r] < data[min_idx]:
        min_idx = r
    if i != min_idx:
        data[i], data[min_idx] = data[min_idx], data[i]
        swaps.append((i, min_idx))
        swaps = heapify(data, min_idx, swaps)
    return swaps



def main():
    # input mode (keyboard or file)
    mode = input("Enter input mode (I for keyboard input, F for file input): ")

    # input from keyboard
    if mode == "I":
        n = int(input())
        data = list(map(int, input().split()))

        # checks if length of data is the same as the said length
        assert len(data) == n

    # input from file
    elif mode == "F":
        filename = input("Enter input file name: ")
        with open(filename, 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))

            # checks if length of data is the same as the said length
            assert len(data) == n

    else:
        print("Invalid input mode. Please enter either 'I' or 'F'.")
        return

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # checks if the heap property is satisfied
    for i in range(n//2):
        if 2*i+1 < n and data[i] > data[2*i+1]:
            print("ERROR: heap property not satisfied")
            return

        if 2*i+2 < n and data[i] > data[2*i+2]:
            print("ERROR: heap property not satisfied")
            return

    # output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))

    # output all swaps
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
