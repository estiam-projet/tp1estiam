#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.group()
def cli():
    """Programme de démonstration d'une interface en ligne de commande."""
    pass

@cli.command()
@click.argument('name', default='monde')
def hello(name):
    """Affiche un message de bienvenue."""
    click.echo(f"Bonjour {name} !")

@cli.command()
@click.option('--count', default=1, help='Nombre de répétitions.')
@click.argument('message')
def repeat(count, message):
    """Répète un message plusieurs fois."""
    for _ in range(count):
        click.echo(message)

if __name__ == '__main__':
    cli()