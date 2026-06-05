"""
friendly_dev_motivation.py
A respectful, professional, and lighthearted developer motivation CLI.

Usage:
  python friendly_dev_motivation.py --name YourName
  python friendly_dev_motivation.py --name YourName --mode extra
"""

from __future__ import annotations
import argparse
import random
import sys
from dataclasses import dataclass
from typing import Sequence

@dataclass(frozen=True)
class Config:
    name: str
    mode: str = "normal"  # normal | extra

# ----------------------------
# Motivational and lighthearted messages
# ----------------------------
MOTIVATIONS = [
    "Your code today will run smoothly and elegantly.",
    "Every challenge you face is a step toward mastery.",
    "Each bug you solve is a testament to your skill.",
    "Your algorithms and logic are in perfect harmony today.",
    "Today is a day of clarity and productive coding."
]

LIGHT_JOKES = [
    "Remember: a well-commented function is a friendly teammate.",
    "If your code works, celebrate quietly; if not, learn gracefully.",
    "Even minor refactors are victories for future developers.",
    "Every console log is a breadcrumb for understanding.",
    "Clean code fosters peace of mind and clarity."
]

EXTRA_FUN = [
    "Your IDE applauds your careful typing.",
    "Git approves of your commits silently.",
    "Coffee is brewed; focus mode engaged.",
    "Warnings are now polite suggestions rather than alarms."
]

# ----------------------------
# Input helpers
# ----------------------------
def read_choice(prompt: str, valid: set[str]) -> str:
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print("Invalid input. Please try again.")

def parse_args(argv: Sequence[str]) -> Config:
    parser = argparse.ArgumentParser(
        description="Professional & friendly developer motivation CLI"
    )
    parser.add_argument("--name", required=True, help="Your name")
    parser.add_argument("--mode", choices=["normal", "extra"], default="normal")
    args = parser.parse_args(argv)
    return Config(name=args.name, mode=args.mode)

# ----------------------------
# CLI Execution
# ----------------------------
def main(argv: Sequence[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    cfg = parse_args(argv)

    motivation = random.choice(MOTIVATIONS)
    joke = random.choice(LIGHT_JOKES)

    print("\n" + "="*50)
    print(f"   Greetings, {cfg.name}!")
    print("="*50)
    print(f"✨ {motivation}")
    print(f"💡 {joke}")

    if cfg.mode == "extra":
        print(f"\n🎉 Bonus message: {random.choice(EXTRA_FUN)}")

    print("\nKeep coding with respect, diligence, and joy.\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
