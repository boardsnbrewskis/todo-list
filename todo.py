#!/usr/bin/env python3
"""A dead-simple command-line to-do list."""

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    add_task("Learn git branching")
    add_task("Push to GitHub")
    list_tasks()
