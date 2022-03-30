{% include navigation.html %}

[Link to replit for code](https://replit.com/@JeanKim4/jeanapcsptri3)

[Link to github repository](https://github.com/jeankim05/jeanapcsptri3/tree/main)

    
    

``` python
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

## Documentation of Code Week 1
* info.db is the file with all the loops. There are three types of loops in this particular page: recursion, for loops, and while loops
* This is what displays the actual data which are appended to the list
* Code for calling these loop functions are shown down below:


![image](https://user-images.githubusercontent.com/60992581/159366930-73e5250c-5d50-4f9f-ae2a-6a85585a9e53.png)

* The fibonacci sequence is present from the first term to the nth term. The nth term is what the user presents.
* It is a recursion algorithm. The first two terms are added to make the third term and so on.
* The code for this is shown below:

![image](https://user-images.githubusercontent.com/60992581/159367348-31597a0e-9571-4281-862e-57d450a30680.png)

## Documentation of Code Week 2
![image](https://user-images.githubusercontent.com/60992581/160324691-8a921a93-5523-4ec1-b08a-b92a84610516.png)
* Line 4 implements call so that it can be used in the menu
* Line 16 shows an error because the user may add a negative number which will not work with factorial


<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@JeanKim4/jeanapcsptri3?embed=true" > 
*
*
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@IsaacLe2/Tri3Repo?embed=true" > 
