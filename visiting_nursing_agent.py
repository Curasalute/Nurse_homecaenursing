from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class VisitScenario:
    patient_name: str
    temperature_c: float
    spo2: int
    systolic_bp: int
    diastolic_bp: int
    pain_level: int
    has_medication_issue: bool


class VisitingNursingAIAgent:
    """Simple rule-based AI agent for visiting nursing simulation."""

    def decide(self, scenario: VisitScenario) -> Dict[str, object]:
        actions: List[str] = ["バイタル測定を記録する", "患者の主訴をヒアリングする"]
        urgency_score = 0

        if scenario.temperature_c >= 38.5:
            urgency_score += 2
            actions.append("発熱対応として水分摂取と安静を促す")

        if scenario.spo2 <= 92:
            urgency_score += 3
            actions.append("酸素化低下のため主治医へ緊急連絡する")

        if scenario.systolic_bp >= 180 or scenario.diastolic_bp >= 110:
            urgency_score += 3
            actions.append("高血圧緊急域のため救急受診を調整する")

        if scenario.pain_level >= 7:
            urgency_score += 1
            actions.append("疼痛緩和ケアを優先する")

        if scenario.has_medication_issue:
            urgency_score += 1
            actions.append("服薬状況を確認し、必要時は薬剤調整を相談する")

        if urgency_score >= 5:
            status = "emergency"
            summary = f"{scenario.patient_name}さんは緊急対応が必要です。"
        elif urgency_score >= 2:
            status = "needs_follow_up"
            summary = f"{scenario.patient_name}さんは当日中の追加フォローが必要です。"
        else:
            status = "stable"
            summary = f"{scenario.patient_name}さんは経過観察で問題ありません。"

        return {
            "patient_name": scenario.patient_name,
            "status": status,
            "actions": actions,
            "summary": summary,
        }


def simulate_visit(agent: VisitingNursingAIAgent, scenario_data: Dict[str, object]) -> Dict[str, object]:
    scenario = VisitScenario(**scenario_data)
    return agent.decide(scenario)
