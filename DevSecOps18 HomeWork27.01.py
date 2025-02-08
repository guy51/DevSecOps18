# תרגיל 1: מציאת כל המחלקים השלמים של מספר

def find_divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

number = int(input("Enter a number: "))
print("Divisors:", find_divisors(number))

# תרגיל 2: קליטת מספרים והצגת סכום וממוצע

def sum_and_avg():
    total, count = 0, 0
    while True:
        num = int(input(f"Please enter number #{count + 1} ({'avg=' + str(total/count) + '. Sum=' + str(total) if count > 0 else ''}): "))
        if num < 0:
            break
        total += num
        count += 1
    print("Thank you. Goodbye.")

sum_and_avg()

# תרגיל 3: קליטת מילים עד שהמשתמש מקליד פעמיים את אותה מילה

def word_repetition():
    words = set()
    while True:
        word = input("Please type a word: ").lower()
        if word in words:
            print(f"You entered the word '{word}' twice. Goodbye...")
            break
        words.add(word)

word_repetition()


# השוואת רשימות ומציאת איזו מכילה יותר מספרים גדולים
def compare_lists(lst1, lst2):  # שינוי שם המשתנים המקומיים
    count1 = sum(1 for i, j in zip(lst1, lst2) if i > j)
    count2 = sum(1 for i, j in zip(lst1, lst2) if j > i)

    if count1 > count2:
        print("List 1 has more larger numbers.")
    elif count2 > count1:
        print("List 2 has more larger numbers.")
    else:
        print("Both lists have the same number of larger values.")


# הגדרת הרשימות מחוץ לפונקציה
list1 = [3, 5, 30, 0]
list2 = [1000, 5, 29, -5]

# קריאה לפונקציה
compare_lists(list1, list2)
