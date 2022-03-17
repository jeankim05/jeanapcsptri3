{% include navigation.html %}

<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@JeanKim4/jeanapcsptri3?lite=true%22%3E#menu.py"></iframe>
</div>

[Link to replit for code](https://replit.com/@JeanKim4/jeanapcsptri3)
//
[Link to github repository](https://github.com/jeankim05/jeanapcsptri3/tree/main)
```
import shipanimation
import faceanimation
import swap
import keypad
import tree

main_menu = [
    ["Swap", "swap.py"],
    ["Keypad", "keypad.py"],
    ["Tree", "tree.py"]
]

animationsub_menu = [
    ["Ship Animation", "shipanimation.py"],
    ["Face Animation", "faceanimation.py"]
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


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", animationsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()
    ```
