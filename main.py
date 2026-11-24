"""One-line roast of an everyday gadget, for the make.fun bounty."""
import os

OUTPUT_PATH = "/output/entry.txt"

ROAST = (
    "My phone dies at 4 p.m. every day: the only coworker that clocks out "
    "early, ignores every message, and still expects a promotion."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
