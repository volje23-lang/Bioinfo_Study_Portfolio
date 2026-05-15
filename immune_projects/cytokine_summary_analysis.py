# ==========================================
# Project: Cytokine Summary Analysis
# Goal: Summarize cytokine expression patterns
# Author: Jaewon Kim
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# cytokine expression 데이터 로드
data = pd.read_csv(
    "immune_projects/cytokine_expression.csv"
)

# 평균 expression 계산
average_expression = data["expression"].mean()

# 평균 이상 cytokine 추출
high_cytokines = data[
    data["expression"] > average_expression
]

# expression 기준 정렬
sorted_data = data.sort_values(
    by="expression",
    ascending=False
)

print("[Cytokine Summary Analysis]")
print(f"Average expression: {average_expression:.2f}")

print("\nHighly expressed cytokines:")
print(high_cytokines)

print("\nSorted cytokine expression:")
print(sorted_data)

# 결과 저장
sorted_data.to_csv(
    "immune_projects/cytokine_summary_results.csv",
    index=False
)

high_cytokines.to_csv(
    "immune_projects/high_cytokines.csv",
    index=False
)

# cytokine expression 시각화
plt.figure(figsize=(9, 5))

plt.bar(
    sorted_data["gene"],
    sorted_data["expression"]
)

plt.axhline(
    average_expression,
    linestyle="--",
    label="Average expression"
)

plt.xlabel("Cytokine genes")
plt.ylabel("Expression level")

plt.title("Cytokine Expression Summary")

plt.legend()
plt.tight_layout()

plt.savefig(
    "outputs/cytokine_expression_barplot.png"
)

plt.show()

# 간단한 expression 변화 확인
print("\nResults saved as CSV files and barplot image.")