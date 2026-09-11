from scipy.stats import mannwhitneyu


def mann_whitney_u(distribution_a, distribution_b):
    """
    Perform a two-sided Mann-Whitney U test on two independent samples.

    Args:
        distribution_a: First numerical distribution.
        distribution_b: Second numerical distribution.

    Returns:
        tuple: Mann-Whitney U statistic and p-value.
    """

    if not distribution_a or not distribution_b:
        raise ValueError("Both distributions must contain data.")

    statistic, p_value = mannwhitneyu(
        distribution_a,
        distribution_b,
        alternative="two-sided"
    )

    return statistic, p_value
