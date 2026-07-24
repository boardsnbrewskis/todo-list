#!/usr/bin/env python3
"""A simple command-line to-do list with persistence."""

import argparse
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {task}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    else:
        print(f"No task at position {index}")


def main():
    parser = argparse.ArgumentParser(description="A simple to-do list.")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("task", help="The task description")

    subparsers.add_parser("list", help="List all tasks")

    remove_parser = subparsers.add_parser("remove", help="Remove a task by number")
    remove_parser.add_argument("index", type=int, help="Task number to remove")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "remove":
        remove_task(args.index)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
