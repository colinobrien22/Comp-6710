import csv


def read_distributions(filename):
    """
    Read distributions A and B from a CSV file.

    Args:
        filename: Path to the CSV file.

    Returns:
        tuple: Two lists containing the values from columns A and B.
    """

    distribution_a = []
    distribution_b = []

    with open(filename, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError("CSV file is missing a header.")

        if "A" not in reader.fieldnames or "B" not in reader.fieldnames:
            raise ValueError("CSV file must contain columns A and B.")

        for row in reader:
            value_a = row["A"].strip()
            value_b = row["B"].strip()

            if value_a:
                distribution_a.append(float(value_a))

            if value_b:
                distribution_b.append(float(value_b))

    return distribution_a, distribution_b
