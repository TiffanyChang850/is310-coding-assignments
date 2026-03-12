from rich import print
from rich.console import Console
from rich.table import Table

console = Console()
console.print("Here is some initial data:", style="bold cyan")

table = Table(title="Star Wars Movies")
table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right")
table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console.print(table)
console.print("\n[bold cyan]Now I want you to enter your preferred movies:[/bold cyan]")

movie_title = input("Enter the title of the movie: ")
release_date = input("Enter the release date of the movie: ")
box_office = input("Enter the box office earnings of the movie: ")
