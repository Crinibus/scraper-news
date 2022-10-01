from argparse import ArgumentParser


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

    parser.add_argument(
        "--show",
        help="print out news",
        dest="show",
        action="store_true"
    )

    parser.add_argument(
        "--hours",
        help="amount of hours",
        dest="hours",
        type=int,
    )

    return parser.parse_args()
