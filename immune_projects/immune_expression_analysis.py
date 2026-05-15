# ==========================================
# Project: Immune Gene Expression Analysis
# Goal: Analyze and visualize immune gene expression data
# Author: Jaewon Kim
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# immune gene expression 데이터 로드
data = pd.read_csv("immune_projects/immune_expression.csv")

# 평균 expression 계산
average_expression = data["expression"].mean()

# 가장 높은 expression gene 확인
max_row = data.loc[data["expression"].idxmax()]

print(f"Average expression: {average_expression:.2f}")

print(
    f"Highest expression gene: "
    f"{max_row['gene']} ({max_row['expression']})"
)

# expression 기준 정렬
sorted_data = data.sort_values("expression", ascending=False)

print(sorted_data)

# gene expression 시각화
plt.bar(
    sorted_data["gene"],
    sorted_data["expression"],
    color="skyblue"
    )

# 평균 expression 기준선 추가
plt.axhline(
    y=average_expression,
    color="red",
    linestyle="--"
    )

plt.xlabel("Gene")
plt.ylabel("Expression Level")

plt.title("Immune Gene Expression Analysis")

plt.xticks(rotation=45)

plt.tight_layout()

# 그래프 저장
plt.savefig("result_graph.png")

plt.show()