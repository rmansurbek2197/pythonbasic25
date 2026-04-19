def find_second_largest_and_smallest(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_largest, second_smallest

def main():
    lst = [12, 45, 7, 23, 56, 89, 34, 6, 98, 21, 43, 11, 76, 54, 33, 90, 27, 65, 72, 49, 38, 15, 93, 67, 81]
    second_largest, second_smallest = find_second_largest_and_smallest(lst)
    print("Ikkinchi eng katta son:", second_largest)
    print("Ikkinchi eng kichik son:", second_smallest)
    print("Ro'yxat:", lst)

    lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]
    second_largest, second_smallest = find_second_largest_and_smallest(lst)
    print("Ikkinchi eng katta son:", second_largest)
    print("Ikkinchi eng kichik son:", second_smallest)
    print("Ro'yxat:", lst)

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    second_largest, second_smallest = find_second_largest_and_smallest(lst)
    print("Ikkinchi eng katta son:", second_largest)
    print("Ikkinchi eng kichik son:", second_smallest)
    print("Ro'yxat:", lst)

if __name__ == "__main__":
    main()