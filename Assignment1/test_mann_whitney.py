import unittest

from mann_whitney import mann_whitney_u
from csv_reader import read_distributions


class TestMannWhitneyU(unittest.TestCase):

    def test_known_distributions(self):
        distribution_a = [1, 1, 2, 3, 1, 1, 4]
        distribution_b = [6, 4, 7, 1, 3, 7, 3, 7]

        statistic, p_value = mann_whitney_u(
            distribution_a,
            distribution_b
        )

        self.assertAlmostEqual(statistic, 8.5)
        self.assertAlmostEqual(
            p_value,
            0.023941434608217273
        )

    def test_identical_distributions(self):
        distribution_a = [1, 2, 3, 4, 5]
        distribution_b = [1, 2, 3, 4, 5]

        statistic, p_value = mann_whitney_u(
            distribution_a,
            distribution_b
        )

        self.assertGreaterEqual(p_value, 0.05)

    def test_empty_distribution(self):
        distribution_a = []
        distribution_b = [1, 2, 3]

        with self.assertRaises(ValueError):
            mann_whitney_u(
                distribution_a,
                distribution_b
            )

    def test_perf_data_csv(self):
        distribution_a, distribution_b = read_distributions(
            "perf-data.csv"
        )

        statistic, p_value = mann_whitney_u(
            distribution_a,
            distribution_b
        )

        self.assertEqual(len(distribution_a), 109)
        self.assertEqual(len(distribution_b), 109)

        self.assertAlmostEqual(statistic, 6149.0)
        self.assertAlmostEqual(
            p_value,
            0.6550995176508366
        )


if __name__ == "__main__":
    unittest.main()
