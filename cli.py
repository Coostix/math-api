import click
from app.services import pow_op, fibonacci_op, factorial_op

@click.group()
def cli():
    """CLI pentru operații matematice"""
    pass

@cli.command()
@click.option("--base", "-b", type=int, required=True)
@click.option("--exponent", "-e", type=int, required=True)
def pow(base, exponent):
    """Ridică un număr la o putere"""
    result = pow_op(base, exponent)
    click.echo(f"Result: {result}")

@cli.command()
@click.option("--n", type=int, required=True)
def fib(n):
    """Returnează al n-lea număr Fibonacci"""
    result = fibonacci_op(n)
    click.echo(f"Result: {result}")

@cli.command()
@click.option("--n", type=int, required=True)
def fact(n):
    """Returnează factorialul unui număr"""
    result = factorial_op(n)
    click.echo(f"Result: {result}")

if __name__ == "__main__":
    cli()
