import week0.shipanimation 
import week0.faceanimation
import week0.swap
import week0.keypad
import week0.tree
import week1.infodb
import week1.fibonacci
import week2.factorial
import week2.mathfunction
import week2.palindrome

main_menu = [
    ["Swap", week0.swap.main],
    ["Keypad", week0.keypad.main],
    ["Tree", week0.tree.main]
]

animationsub_menu = [
    ["Ship Animation", week0.shipanimation.main],
    ["Face Animation", week0.faceanimation.main]
]

landlsub_menu = [
    ["InfoDB", week1.infodb.menu],
    ["Fibonacci", week1.fibonacci.menu]
]

mathsub_menu = [
    ["Factorial", week2.factorial.menu],
    ["Great Common Denominator Math Function", week2.mathfunction.greatestcommondenominator],
    ["Palindrome", week2.palindrome.menu]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)


def animationsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, animationsub_menu)

def landlsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, landlsub_menu)

def mathsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, mathsub_menu)

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", animationsubmenu])
    menu_list.append(["Lists and Loops", landlsubmenu])
    menu_list.append(["Math", mathsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()