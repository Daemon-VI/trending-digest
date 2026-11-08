import argparse

from .search import fetch_issues


def main() -> None:
    p = argparse.ArgumentParser(description="Good first issues digest")
    p.add_argument("languages", nargs="+", help="e.g. python typescript")
    p.add_argument("--limit", type=int, default=5)
    args = p.parse_args()
    for lang in args.languages:
        print(f"\n## {lang}")
        for i in fetch_issues(lang, args.limit):
            print(f"- {i['title']}\n  {i['html_url']}")


if __name__ == "__main__":
    main()
