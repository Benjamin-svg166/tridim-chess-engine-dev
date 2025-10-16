# cli/main.py

import argparse
from engine.core_engine import CoreEngine

def run_drill(theme):
    engine = CoreEngine()
    print(f"\n🔍 Simulating '{theme}' Drill...\n")
    engine.simulate_drill(theme)

def main():
    parser = argparse.ArgumentParser(description="Tridimensional Chess CLI")
    parser.add_argument(
        "--drill",
        type=str,
        choices=["fork", "zugzwang", "pin", "skewer"],
        help="Run a tactical drill by theme"
    )

    args = parser.parse_args()

    if args.drill:
        run_drill(args.drill)
    else:
        print("🧠 No drill selected. Use --drill [theme] to run one.")

if __name__ == "__main__":
    main()
