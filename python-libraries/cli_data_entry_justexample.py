from rich import print
from rich.console import Console
from rich.table import Table

console = Console()
console.print("List of volleyball stars on the Japanese national team", style = "bold red")
table = Table(title = "Japan Volleyball Stars")
table.add_column("Age", style = "cyan", no_wrap = True)
table.add_column("Name", style = "magenta")
table.add_column("Position", justify="right", style = "yellow")
table.add_column("Starter (Y/N)", justify = "right", style = "green")
table.add_row("30", "Yuki Ishikawa", "Outside Hitter", "Y")
table.add_row("24", "Ran Takahashi", "Outside Hitter", "Y")
table.add_row("26", "Yuji Nishida", "Opposite", "Y")
table.add_row("32", "Masahiro Sekita", "Setter", "Y")
table.add_row("31", "Tomohiro Yamamaoto", "Libero", "Y")
table.add_row("27", "Kento Miyaura", "Opposite", "N")
console.print(table)
console.print("\n[bold purple]Please enter other favorite players:[/bold purple]")

y = False
Name = input("Enter the name of the player: ")
console.print("This is the name you entered: ", Name)
sure = input("Is this the name you meant to enter? (Y/N)")
def check(sure):
  a = False
  y = False
  if sure == "Y":
    a = True
    y = True
  elif sure == "N":
    a = False
  while a is False: 
    Name = input("Enter new input: ")
    sure = input("Is this the name you meant to enter? (Y/N)")
    if sure == "Y":
      a == True
      y == True
    return y
check(sure)
Age = input("Enter the age of the player: ")
sure1 = input("Is this the name you meant to enter? (Y/N)")
check(sure1)
Position = input("Enter the position of the player: ")
sure2 = input("Is this the name you meant to enter? (Y/N)")
check(sure2)
Starter = input("Enter if the player is a starter: ")
sure3 = input("Is this the name you meant to enter? (Y/N)")
check(sure3)
if y == True: 
  table.add_row(Age, Name, Position, Starter)
  
console.print(table)
