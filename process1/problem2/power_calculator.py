def calculate_power(base, exponent):
    """
    반복문을 사용하여 거듭제곱을 계산하는 함수
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        # 음수 지수 처리: 1 / (base^|exponent|)
        return 1 / calculate_power(base, -exponent)

    result = 1
    for _ in range(exponent):
        result *= base

    return result


def main():
    """
    메인 함수: 사용자 입력을 받고 제곱 계산을 수행
    """
    try:
        # 숫자 입력 받기
        number_input = input("Enter number: ")
        try:
            number = float(number_input)
        except ValueError:
            print("Invalid number input.")
            return

        # 지수 입력 받기
        exponent_input = input("Enter exponent: ")
        try:
            exponent = int(exponent_input)
        except ValueError:
            print("Invalid exponent input.")
            return

        # 거듭제곱 계산
        result = calculate_power(number, exponent)

        # 결과 출력
        print(f"Result: {int(result) if result.is_integer() else result}")

    except KeyboardInterrupt:
        print("\n프로그램이 중단되었습니다.")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
