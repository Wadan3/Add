
"""
friendly_dev_motivation.py
A clean, respectful, and lighthearted developer motivation CLI.

Usage:
  python friendly_dev_motivation.py --name Wadan
  python friendly_dev_motivation.py --name Wadan --mode extra
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


MOTIVATIONS = [
    "Today your code will run like a Swiss watch.",
    "You debug faster than the bugs appear.",
    "Every error is just a step toward a better version.",
    "You and algorithms have a healthy relationship.",
    "Today is the day everything finally runs.",
]

LIGHT_JOKES = [
    "Just remember to run tests before pushing.",
    "If it works, it’s a feature. If not, it’s a learning opportunity.",
    "Sometimes restart is a valid engineering strategy.",
    "Console logs are still unsung heroes.",
    "Clean code = peaceful sleep.",
]

EXTRA_FUN = [
    "Coffee loaded. Focus activated.",
    "Your IDE believes in you.",
    "Git approves your commits.",
    "Even warnings are polite today.",
]


def parse_args(argv: Sequence[str]) -> Config:
    parser = argparse.ArgumentParser(
        description="Clean & friendly developer motivation CLI"
    )
    parser.add_argument("--name", required=True, help="Your name")
    parser.add_argument("--mode", choices=["normal", "extra"], default="normal")
    args = parser.parse_args(argv)
    return Config(name=args.name, mode=args.mode)


def main(argv: Sequence[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    cfg = parse_args(argv)

    motivation = random.choice(MOTIVATIONS)
    joke = random.choice(LIGHT_JOKES)

    print(f"\n✨ {cfg.name}, {motivation}")
    print(f"😄 {joke}")

    if cfg.mode == "extra":
        print(f"🎉 {random.choice(EXTRA_FUN)}")

    print("\nKeep building. Keep improving. 🚀\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
