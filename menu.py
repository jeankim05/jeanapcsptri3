import week0.shipanimation 
import week0.faceanimation
import week0.swap
import week0.keypad
import week0.tree
import week1.infodb
import week1.fibonacci

main_menu = [
    ["Swap", week0.swap.swap],
    ["Keypad", week0.keypad.keypad],
    ["Tree", week0.tree.tree]
]

animationsub_menu = [
    ["Ship Animation", week0.shipanimation.main],
    ["Face Animation", week0.faceanimation.main]
]

landlsub_menu = [
    ["InfoDB", week1.infodb.main],
    ["Fibonacci", week1.fibonacci.display]
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

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", animationsubmenu])
    menu_list.append(["Lists and Loops", landlsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()