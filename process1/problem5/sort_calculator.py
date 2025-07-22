def main():
    print("[*] Sort Calculator")
    numbers = input("[*] Enter numbers: ")

    try:
        numbers = [float(num) for num in numbers.split()]

        # Python 내장 함수 sorted(), sort() 사용 금지, 대신 버블 정렬 알고리즘 사용
        for i in range(len(numbers)):
            for j in range(len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        for i in range(len(numbers)):
            if i == 0:
                print(f"Sorted: {numbers[i]}", end=" ")
            else:
                print(f"{numbers[i]}", end=" ")
        print()
    except ValueError:
        print("Invalid input.")
        return


if __name__ == "__main__":
    main()
