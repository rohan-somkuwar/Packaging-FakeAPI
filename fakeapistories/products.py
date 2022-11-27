import click

import requests

get_url = 'https://fakestoreapi.com/products/categories'
get_product_url = 'https://fakestoreapi.com/products/category/jewelery'
post_url = 'https://fakestoreapi.com/products'

@click.group()
def main():
    pass

@main.command()
# @click.launch(get_url)
def get_categories():
    response = requests.get(get_product_url)
    paste = response.text
    click.echo(paste)


@main.command()
def categories():
    response = requests.get(get_url='https://fakestoreapi.com/products/categories')
    paste = response.text
    click.echo(paste)


@main.command()
def add_product():
    response = requests.post(post_url,data =  {
                    'title': 'test product',
                    'price': 13.5,
                    'description': 'lorem ipsum set',
                    'image': 'https://i.pravatar.cc',
                    'category': 'electronic'
                })
    paste = response.text
    click.echo(paste)


if __name__ == '__main__':
    main()
