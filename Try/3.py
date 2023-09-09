from rich.console import Console
console = Console()
from rich.table import Table
table = Table()
table.add_column('[red]test')
table.add_column('[red]test2')
table.add_row('[red]this is a table', '[yellow]this is a table')
table.add_row('[red]hello', '[yellow]world')
console.print(table)