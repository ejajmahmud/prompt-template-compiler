"""Command-line interface for Prompt Template Compiler."""
import argparse
from .compiler import PromptCompiler

def main():
    parser = argparse.ArgumentParser(description="Prompt Template Compiler CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate prompt compilation")
    args = parser.parse_args()

    tmpl = "Hello {{user}}! {% if has_tasks %}Your tasks are: {{tasks}}{% endif %} Code: {return true;}"
    res = PromptCompiler.render(tmpl, {"user": "Alice", "has_tasks": True, "tasks": "Review PR #42"})
    print("Compiled Prompt:")
    print(" ", res)

if __name__ == "__main__":
    main()
