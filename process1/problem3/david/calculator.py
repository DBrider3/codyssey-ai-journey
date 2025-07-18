def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b


def parse_expression(expression: str) -> tuple:
    """수식을 파싱하여 숫자와 연산자를 분리하는 함수"""
    try:
        # 공백 제거 후 분리
        parts = expression.strip().split()

        # 입력 형식 검증: "숫자 연산자 숫자" 형태여야 함
        if len(parts) != 3:
            raise ValueError(
                "❌ 잘못된 입력 형식입니다. '숫자 연산자 숫자' 형태로 입력해주세요."
            )

        # 숫자 변환
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        # 연산자 검증
        if operator not in ["+", "-", "*", "/"]:
            raise ValueError(
                "❌ 지원하지 않는 연산자입니다. +, -, *, / 중 하나를 사용해주세요."
            )

        return num1, operator, num2

    except ValueError as e:
        if "잘못된 입력 형식" in str(e) or "지원하지 않는 연산자" in str(e):
            raise e
        else:
            raise ValueError("❌ 숫자를 올바르게 입력해주세요.")


def evaluate_expression(expression: str) -> float:
    """수식을 평가하여 결과를 반환하는 함수"""
    try:
        num1, operator, num2 = parse_expression(expression)

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            if num2 == 0:
                raise ValueError("❌ 0으로 나눌 수 없습니다.")
            result = divide(num1, num2)
            if result is None:
                raise ValueError("❌ 나눗셈 오류가 발생했습니다.")

        # 결과가 정수인 경우 정수로 반환, 소수인 경우 float로 반환
        if result == int(result):
            return int(result)
        else:
            return result

    except ValueError as e:
        raise e


def expression_calculator():
    """문자열 수식 입력 방식 계산기"""
    print("=" * 50)
    print("📝 문자열 수식 계산기")
    print("=" * 50)
    print("사용법: 숫자 연산자 숫자 (예: 2 + 3)")
    print("지원 연산자: +, -, *, /")
    print("=" * 50)

    while True:
        try:
            expression = input("\nEnter expression: ").strip()

            if expression.lower() == "exit":
                print("👋 수식 계산기를 종료합니다.")
                break

            if not expression:
                print("❌ 수식을 입력해주세요.")
                continue

            result = evaluate_expression(expression)
            print(f"Result: {result}")

        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\n👋 수식 계산기를 종료합니다.")
            break


def get_user_input():
    """사용자로부터 실수형 숫자 2개를 입력받는 함수"""
    print("=" * 50)
    print("간단한 계산기 프로그램")
    print("=" * 50)

    while True:
        try:
            num1 = int(float(input("첫 번째 숫자를 입력하세요: ")))
            num2 = int(float(input("두 번째 숫자를 입력하세요: ")))
            return num1, num2
        except ValueError:
            print("❌ 올바른 숫자를 입력해주세요!")
            continue


def show_menu():
    """계산 메뉴를 보여주는 함수"""
    print("\n📋 어떤 계산을 하시겠습니까?")
    print("➕ 덧셈: +")
    print("➖ 뺄셈: -")
    print("✖️ 곱셈: *")
    print("➗ 나눗셈: /")
    print("🔄 모든 계산 보기: all")
    print("🚪 종료: exit")


def calculate_all(a: float, b: float):
    """모든 계산 결과를 보여주는 함수"""
    print(f"\n{a}와 {b}의 모든 계산 결과:")
    print("-" * 30)
    print(f"➕ 덧셈: {a} + {b} = {add(a, b)}")
    print(f"➖ 뺄셈: {a} - {b} = {subtract(a, b)}")
    print(f"✖️ 곱셈: {a} × {b} = {multiply(a, b)}")
    try:
        print(f"➗ 나눗셈: {a} ÷ {b} = {divide(a, b):.2f}")
    except ValueError as e:
        print(f"➗ 나눗셈: {e}")


def perform_calculation(a: int, b: int, operator: str):
    """연산자를 받아서 계산을 수행하는 함수"""
    if operator == "+":
        result = add(a, b)
        print(f"Result: {result}")
    elif operator == "-":
        result = subtract(a, b)
        print(f"Result: {result}")
    elif operator == "*":
        result = multiply(a, b)
        print(f"Result: {result}")
    elif operator == "/":
        result = divide(a, b)
        if result is not None:
            print(f"Result: {result}")
    else:
        print("Invalid operator.")


def main():
    """메인 프로그램"""
    while True:
        print("\n🎯 계산기 모드를 선택하세요:")
        print("1️⃣ 일반 계산기")
        print("2️⃣ 수식 입력 계산기 (Bouns)")
        print("🚪 종료")

        mode_choice = input("\n모드를 선택하세요 (1/2/exit): ").strip().lower()

        if mode_choice == "1":
            # 기존 일반 계산기 모드
            while True:
                num1, num2 = get_user_input()

                while True:
                    show_menu()
                    choice = input("\n연산자를 입력하세요: ").strip().lower()

                    if choice in ["+", "-", "*", "/"]:
                        perform_calculation(num1, num2, choice)
                    elif choice == "all":
                        calculate_all(num1, num2)
                    elif choice == "exit":
                        print("\n👋 계산기를 종료합니다. 감사합니다!")
                        return
                    else:
                        print("Invalid operator.")

                    # 계속할지 묻기
                    continue_choice = input(
                        "\n같은 숫자로 다른 계산을 하시겠습니까? (y/n): "
                    ).lower()
                    if continue_choice != "y":
                        break

                # 새로운 계산을 할지 묻기
                new_calc = input("\n새로운 계산을 하시겠습니까? (y/n): ").lower()
                if new_calc != "y":
                    break

        elif mode_choice == "2":
            # 수식 입력 계산기 모드
            expression_calculator()

        elif mode_choice == "exit":
            print("\n👋 계산기를 종료합니다. 감사합니다!")
            break
        else:
            print("❌ 올바른 모드를 선택해주세요.")


if __name__ == "__main__":
    main()
