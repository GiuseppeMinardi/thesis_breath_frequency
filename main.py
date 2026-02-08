"""Docstring for thesis_breath_frequency main file."""

import argparse
from pathlib import Path

from thesis_breath_frequency import logger
from thesis_breath_frequency.cleaning import load_and_process_excel
from thesis_breath_frequency.project_configs import ProjectPaths

project_paths = ProjectPaths()

raw_data_path = project_paths.data_folder.raw.joinpath("Respiratorio CPET BR.xlsx")


def data_cleaning(source_excel_path: Path, destination_csv_path: Path):
    """Load, process and save cleaned data from Excel to CSV format.

    Args:
        source_excel_path: Path to the raw Excel file.
        destination_csv_path: Path where the cleaned CSV file will be saved.
    """
    cleaned_excel = load_and_process_excel(source_excel_path=source_excel_path)
    logger.info(f"Data cleaned successfully. Saving to {destination_csv_path}")
    logger.info("Dataset Header: {cleaned_excel.columns.tolist()}")
    cleaned_excel.to_csv(destination_csv_path, index=False)


def main():
    """Main Function."""  # noqa: D401
    parser = argparse.ArgumentParser(description="Breath Frequency MedThesis CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Clean Command ---
    clean_parser = subparsers.add_parser("clean", help="Clean raw data")
    clean_parser.add_argument(
        "-i",
        "--input",
        required=False,
        default=raw_data_path,
        type=Path,
        help="Path to raw data",
    )
    clean_parser.add_argument(
        "-o",
        "--output",
        required=False,
        default=project_paths.data_folder.interim.joinpath("cleaned_data.csv"),
        type=Path,
        help="Path for cleaned data",
    )

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()

    if args.command == "clean":
        data_cleaning(source_excel_path=args.input, destination_csv_path=args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
