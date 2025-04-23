# cli.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import calculator  # importe ta logique métier

@click.group()
def cli():
    """Interface en ligne de commande - Calculatrice"""
    pass

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def add(a, b):
    """Addition de deux nombres."""
    result = calculator.addition(a, b)
    click.echo(f"Résultat: {result}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def sub(a, b):
    """Soustraction de deux nombres."""
    result = calculator.soustraction(a, b)
    click.echo(f"Résultat: {result}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def mul(a, b):
    """Multiplication de deux nombres."""
    result = calculator.multiplication(a, b)
    click.echo(f"Résultat: {result}")

@cli.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
def div(a, b):
    """Division de deux nombres."""
    try:
        result = calculator.division(a, b)
        click.echo(f"Résultat: {result}")
    except ValueError as e:
        click.echo(f"Erreur: {e}")

if __name__ == '__main__':
    cli()
