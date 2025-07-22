def main():
    print("[*] MinMax Calculator!")
    print("[*] Enter the numbers you want to calculate the min and max of")
    numbers = input("[*] Enter the numbers: ")
    numbers = numbers.split()

    try:
        numbers = [float(num) for num in numbers]

        # 파이썬 내장함수 min(), max() 사용 금지
        min_num = numbers[0]
        max_num = numbers[0]

        for num in numbers:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

        print(f"Min: {min_num}, Max: {max_num}")
    except ValueError:
        print("Invalid input.")
        return


if __name__ == "__main__":
    main()
