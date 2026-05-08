import unittest

from visiting_nursing_agent import VisitingNursingAIAgent, simulate_visit


class VisitingNursingAIAgentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.agent = VisitingNursingAIAgent()

    def test_emergency_case_returns_emergency_status(self) -> None:
        report = simulate_visit(
            self.agent,
            {
                "patient_name": "山田",
                "temperature_c": 39.0,
                "spo2": 90,
                "systolic_bp": 150,
                "diastolic_bp": 90,
                "pain_level": 4,
                "has_medication_issue": False,
            },
        )

        self.assertEqual(report["status"], "emergency")
        self.assertTrue(any("緊急連絡" in action for action in report["actions"]))

    def test_stable_case_returns_stable_status(self) -> None:
        report = simulate_visit(
            self.agent,
            {
                "patient_name": "佐藤",
                "temperature_c": 36.7,
                "spo2": 97,
                "systolic_bp": 124,
                "diastolic_bp": 78,
                "pain_level": 2,
                "has_medication_issue": False,
            },
        )

        self.assertEqual(report["status"], "stable")

    def test_follow_up_case_with_medication_issue(self) -> None:
        report = simulate_visit(
            self.agent,
            {
                "patient_name": "田中",
                "temperature_c": 37.8,
                "spo2": 95,
                "systolic_bp": 132,
                "diastolic_bp": 84,
                "pain_level": 7,
                "has_medication_issue": True,
            },
        )

        self.assertEqual(report["status"], "needs_follow_up")
        self.assertTrue(any("服薬状況" in action for action in report["actions"]))


if __name__ == "__main__":
    unittest.main()
