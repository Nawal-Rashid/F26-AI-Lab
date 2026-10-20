def rule_based(score, documents_complete, attendance, age):
    if documents_complete and score>=70 and attendance>=75 and age>=18:
        return "review"
    else:
        return "hold"
cases = [
        ("pass", 95, True, 100, 18, "review"),
        ("attendance failure", 82, True, 70, 20, "hold"),
        ("age failure", 84, True, 95, 17, "hold"),
        ("threshold boundry", 70, True, 75, 18, "review")
    ]
for name, score, documents_complete, attendance, age, expected in cases:
        actual=rule_based(score, documents_complete, attendance, age)
        if name == "pass":
            reason = "all conditions are satisfied."
        elif name == "attendance failure":
            reason = "attendance is below 75%."
        elif name == "age failure":
            reason = "age is below 18."
        else:
            reason = "the score is 70, so it meets the minimum requirement."
        print("case:", name)
        print("score=", score)
        print("documents complete:", documents_complete)            
        print("attendance:", attendance)
        print("age:", age)
        print("expected result:", expected)
        print("actual result:", actual)
        print("reason:",reason)