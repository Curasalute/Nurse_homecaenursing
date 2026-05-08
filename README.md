# Nurse_homecaenursing

訪問看護シミュレーション用のシンプルなAIエージェント実装です。

## 使い方

```python
from visiting_nursing_agent import VisitingNursingAIAgent, simulate_visit

agent = VisitingNursingAIAgent()
report = simulate_visit(
    agent,
    {
        "patient_name": "山田",
        "temperature_c": 38.9,
        "spo2": 91,
        "systolic_bp": 170,
        "diastolic_bp": 100,
        "pain_level": 6,
        "has_medication_issue": True,
    },
)

print(report)
```

## テスト

```bash
python -m unittest discover -s tests
```
