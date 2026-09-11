from csv_reader import read_distributions
from mann_whitney import mann_whitney_u


def main():
    distribution_a, distribution_b = read_distributions("perf-data.csv")

    statistic, p_value = mann_whitney_u(
        distribution_a,
        distribution_b
    )

    print(f"Number of values in A: {len(distribution_a)}")
    print(f"Number of values in B: {len(distribution_b)}")
    print(f"Mann-Whitney U statistic: {statistic}")
    print(f"p-value: {p_value}")

    if p_value < 0.05:
        print("Result: Reject the null hypothesis.")
    else:
        print("Result: Fail to reject the null hypothesis.")


if __name__ == "__main__":
    main()
