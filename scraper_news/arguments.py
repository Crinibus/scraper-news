from argparse import ArgumentParser
import re


def argparse_setup() -> ArgumentParser.parse_args:
    """Setup and return argparse."""
    parser = ArgumentParser(description="")

    parser.add_argument(
        "-s",
        "--scrape",
        help="scrape news",
        action="store_true",
        dest="scrape",
    )

    parser.add_argument(
        "--threads",
        help="use threads when scraping news",
        action="store_true",
        dest="threads",
    )

    parser.add_argument(
        "-b",
        "--breaking",
        help="scrape breaking news",
        action="store_true",
        dest="breaking",
    )

    parser.add_argument(
        "--source",
        help="the source the news is scraped from (can be multiple)",
        type=str,
        nargs="*",
        dest="sources",
        default=["tv2"],
    )

    parser.add_argument("--show", help="print out news", dest="show", action="store_true")

    parser.add_argument(
        "--hours",
        help="amount of hours back from now or a time interval back e.g. 4 to 10 hours back (--hours 4-10)",
        dest="hours",
        type=str,
    )

    parser.add_argument(
        "--count",
        help="count the number of news in news.json",
        dest="count",
        action="store_true",
    )

    return validate_arguments(parser)


def validate_arguments(parser: ArgumentParser):
    args = parser.parse_args()

    if args.hours:
        valid_hours_re = re.compile(r"^([\d]+\-[\d]+)$|^[\d]+$")
        if not valid_hours_re.match(args.hours):
            parser.error("Not valid --hours argument")

    return args
