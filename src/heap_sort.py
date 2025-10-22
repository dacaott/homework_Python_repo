def heap_sort(arr):
    n = len(arr)

    # Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # обмен
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def main():
    s = input("Введите числа через пробел:\n")
    try:
        nums = [int(x) for x in s.strip().split()]
        sorted_nums = heap_sort(nums)
        print("Отсортированный массив:", sorted_nums)
    except:  # noqa: E722
        print("Пожалуйста, вводите только целые числа через пробел")


if __name__ == "__main__":
    main()
