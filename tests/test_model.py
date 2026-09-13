import tempfile
import unittest
from pathlib import Path

from therapeutic_economies import Parameters, SCENARIOS, inversion, policy, simulate


class ModelTests(unittest.TestCase):
    def test_states_remain_bounded(self):
        for scenario in SCENARIOS:
            for endogenous in (True, False):
                for row in simulate(scenario, 7, endogenous):
                    self.assertGreaterEqual(row["protection_share"], 0.0)
                    self.assertLessEqual(row["protection_share"], 1.0)
                    self.assertGreaterEqual(row["capability"], 0.0)
                    self.assertLessEqual(row["capability"], 1.0)

    def test_deterministic_seed(self):
        self.assertEqual(simulate("conditional_support", 42), simulate("conditional_support", 42))

    def test_fixed_baseline_capability_is_constant(self):
        params = Parameters()
        rows = simulate("unconditional_protection", 5, endogenous=False, params=params)
        self.assertTrue(all(row["capability"] == params.initial_capability for row in rows))

    def test_scenarios_are_distinct(self):
        schedules = {scenario: policy(scenario, 0, 120) for scenario in SCENARIOS}
        self.assertEqual(len(set(schedules.values())), len(SCENARIOS))

    def test_sequenced_transition_changes_phase(self):
        early = policy("sequenced_transition", 0, 120)
        middle = policy("sequenced_transition", 50, 120)
        late = policy("sequenced_transition", 100, 120)
        self.assertNotEqual(early, middle)
        self.assertNotEqual(middle, late)
        self.assertGreater(early[0], late[0])
        self.assertLess(early[1], late[1])

    def test_unknown_scenario_fails_closed(self):
        with self.assertRaises(ValueError):
            policy("invented", 0, 120)

    def test_inversion_uses_declared_full_horizon(self):
        self.assertTrue(inversion(simulate("unconditional_protection", 7, endogenous=True)))
        self.assertFalse(inversion(simulate("conditional_support", 7, endogenous=True)))


if __name__ == "__main__":
    unittest.main()
