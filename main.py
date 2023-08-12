#!/usr/bin/python
import argparse
import os
from argparse import Namespace
from pathlib import Path

from helpers.user_repository import UserRepository

user_shell = os.environ['SHELL']


def switch_directory(user_repository: UserRepository, alias: str):
    # If we received the path

    # Check if the path exists in our list of paths
    try:
        path = user_repository.find_one(alias)
        os.chdir(path)
        os.system(user_shell)

    except KeyError:
        print(f"{alias} is not registered.\n")
        print("Select one of the following options:")

        for key, value in user_repository.find_all().items():
            print(f"{key} -> {value}")


def register_path(user_repository: UserRepository, name: str, path: str):
    # Check if the path exists
    if not Path(path).exists():
        print(f"{path} does not exist.")

        return

    absolute_path = os.path.abspath(path)

    user_repository.save(name, absolute_path)
    print(f"{name} registered as {absolute_path}")


def list_paths(user_repository: UserRepository):
    for key, value in user_repository.find_all().items():
        print(f"{key} -> {value}")


def delete_path(user_repository: UserRepository, name: str):
    try:
        user_repository.delete(name)
        print(f"{name} deleted.")
    except KeyError:
        print(f"{name} is not registered.")

        return


def register_current_path(user_repository: UserRepository):
    current_path = os.getcwd()
    user_repository.save('last_path', current_path)
    print(f"{current_path} registered as last_path")


def switch_to_last_path(user_repository: UserRepository):
    last_path = user_repository.find_one('last_path')

    os.chdir(last_path)
    os.system(user_shell)


def process_args(
        path_to_switch: str,
        path_to_register: str,
        alias: str,
        list_register: bool,
        path_to_delete: str,
        wants_go_to_last: bool
):
    user_repository = UserRepository(Path(__file__).parent / "config/directories.json")

    if path_to_switch:
        switch_directory(user_repository, path_to_switch)

    # If the user wants to register a path
    if path_to_register and alias:

        if type(path_to_register) == bool:
            path_to_register = os.getcwd()

        register_path(user_repository, alias, path_to_register)

    # If the user wants to register the current path as last_path
    if path_to_register and not alias:
        register_current_path(user_repository)

    if list_register:
        list_paths(user_repository)

    if path_to_delete:
        delete_path(user_repository, path_to_delete)

    if wants_go_to_last:
        switch_to_last_path(user_repository)


def cli() -> Namespace:
    parser = argparse.ArgumentParser(
        prog='change-dir',
        description='Change directory to the specified path.',
    )

    parser.add_argument(
        '-s', '--switch',
        type=str,
        metavar='ALIAS',
        help='Path to switch to.',
    )

    parser.add_argument(
        '-a', '--alias',
        type=str,
        metavar='NAME',
        help='Alias of the path to register.'
    )

    parser.add_argument(
        '-d', '--delete',
        type=str,
        metavar='ALIAS',
        help='Name of the path to delete.'
    )

    parser.add_argument(
        '-l', '--list',
        default=False,
        action='store_true',
        help='List all registered paths.'
    )

    parser.add_argument(
        '-r', '--register',
        nargs='?',
        type=str,
        const=True,
        default=False,
        metavar='PATH',
        help='Register a path. '
             'If no path is given, the current path will be registered. '
             'If no alias is given, the alias will be last_path.'
    )

    parser.add_argument(
        '-g', '--goto-last',
        default=False,
        action='store_true',
        help='Move to the alias registered as last_path'
    )

    parsed_args = parser.parse_args()

    # Validations You cannot give an alias without giving a path to register, but you can use register in order to
    # save the current path
    if parsed_args.alias and not parsed_args.register:
        parser.error("You cannot give an alias without giving a path to register")

    return parsed_args


if __name__ == '__main__':
    # os.chdir("/home/limbers/Documents")
    # os.system("pwd")
    # os.system("/usr/bin/zsh")

    args = cli()

    process_args(args.switch, args.register, args.alias, args.list, args.delete, args.goto_last)
