"""pages/page1.py — คำนวณเกรดรายวิชา."""

TITLE = "คำนวณเกรด"


def _read_number(value, default):
    """แปลงค่าจาก query เป็น float ที่ปลอดภัย."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    if number != number:
        return default
    return number


def build(query=None):
    query = query or {}

    assignment = _read_number(query.get("assignment", ""), 0)
    quiz = _read_number(query.get("quiz", ""), 0)
    midterm = _read_number(query.get("midterm", ""), 0)
    final = _read_number(query.get("final", ""), 0)
    project = _read_number(query.get("project", ""), 0)

    # clamp to 0..100 so score input stays valid
    values = {
        "assignment": max(0, min(100, assignment)),
        "quiz": max(0, min(100, quiz)),
        "midterm": max(0, min(100, midterm)),
        "final": max(0, min(100, final)),
        "project": max(0, min(100, project)),
    }

    weighted_total = (
        values["assignment"] * 0.15
        + values["quiz"] * 0.10
        + values["midterm"] * 0.25
        + values["project"] * 0.20
        + values["final"] * 0.30
    )

    if weighted_total >= 80:
        grade = "A"
        message = "เยี่ยมมาก! คุณทำผลงานได้ดีเยี่ยม"
    elif weighted_total >= 75:
        grade = "B+"
        message = "ดีมาก ควรพัฒนาต่อเนื่อง"
    elif weighted_total >= 70:
        grade = "B"
        message = "ดี ควรรักษาระดับและปรับปรุงเล็กน้อย"
    elif weighted_total >= 60:
        grade = "C"
        message = "ผ่านแล้ว แต่ยังต้องพัฒนาอีกเล็กน้อย"
    elif weighted_total >= 50:
        grade = "D"
        message = "เกณฑ์ผ่านต่ำ ต้องพยายามมากขึ้น"
    else:
        grade = "F"
        message = "ยังไม่ผ่าน ต้องทบทวนและปรับปรุง"

    has_input = any(value > 0 for value in values.values())

    return {
        "assignment": values["assignment"],
        "quiz": values["quiz"],
        "midterm": values["midterm"],
        "final": values["final"],
        "project": values["project"],
        "weighted_total": round(weighted_total, 2),
        "grade": grade,
        "message": message,
        "has_input": has_input,
    }
