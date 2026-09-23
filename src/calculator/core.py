import os
import sys
# Добавляем путь, чтобы скрипт видел соседний модуль core
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import core

def clear_screen():
    """Очищает экран терминала для удобства работы."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_float_input(prompt: str) -> float:
    """Безопасно запрашивает число у пользователя."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Ошибка: Введите корректное число.")

def main():
    while True:
        clear_screen()
        print("=" * 40)
        print("        🧮 ИНТЕРАКТИВНЫЙ КАЛЬКУЛЯТОР        ")
        print("=" * 40)
        print(" 1. Сложение (+)        6. Корень (√)")
        print(" 2. Вычитание (-)       7. Факториал (!)")
        print(" 3. Умножение (*)       8. Синус (sin)")
        print(" 4. Деление (/)         9. Косинус (cos)")
        print(" 5. Степень (^)        10. Логарифм (ln)")
        print("-" * 40)
        print(" 0. Выход из программы")
        print("=" * 40)
        
        choice = input("Выберите операцию (0-10): ").strip()
        
        if choice == '0':
            print("\n👋 До свидания!")
            break
            
        if choice not in [str(i) for i in range(1, 11)]:
            input("\n❌ Неверный пункт меню. Нажмите Enter, чтобы повторить...")
            continue
            
        print("\n" + "-" * 40)
        
        try:
            # Операции с двумя числами
            if choice in ['1', '2', '3', '4', '5']:
                a = get_float_input("Введите первое число (a): ")
                b = get_float_input("Введите второе число (b): ")
                
                if choice == '1':
                    res = core.add(a, b)
                    print(f"\n✅ Результат: {a} + {b} = {res}")
                elif choice == '2':
                    res = core.subtract(a, b)
                    print(f"\n✅ Результат: {a} - {b} = {res}")
                elif choice == '3':
                    res = core.multiply(a, b)
                    print(f"\n✅ Результат: {a} * {b} = {res}")
                elif choice == '4':
                    res = core.divide(a, b)
                    print(f"\n✅ Результат: {a} / {b} = {res}")
                elif choice == '5':
                    res = core.power(a, b)
                    print(f"\n✅ Результат: {a} ^ {b} = {res}")
            
            # Операции с одним числом
            else:
                a = get_float_input("Введите число: ")
                
                if choice == '6':
                    res = core.sqrt(a)
                    print(f"\n✅ Результат: √{a} = {res}")
                elif choice == '7':
                    if not a.is_integer():
                        raise ValueError("Факториал можно вычислить только для целого числа")
                    res = core.factorial(int(a))
                    print(f"\n✅ Результат: {int(a)}! = {res}")
                elif choice == '8':
                    res = core.sin(a)
                    print(f"\n✅ Результат: sin({a}) = {res}")
                elif choice == '9':
                    res = core.cos(a)
                    print(f"\n✅ Результат: cos({a}) = {res}")
                elif choice == '10':
                    res = core.ln(a)
                    print(f"\n✅ Результат: ln({a}) = {res}")
                    
        except ValueError as e:
            print(f"\n❌ Ошибка вычисления: {e}")
        except Exception as e:
            print(f"\n❌ Что-то пошло не так: {e}")
            
        input("\nНажмите Enter, чтобы вернуться в меню...")

if __name__ == "__main__":
    main()
