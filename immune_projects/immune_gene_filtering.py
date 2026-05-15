# ==========================================
# Project: Immune Gene Filtering Analysis
# Goal: Filter immune-related genes by expression level
# Author: Jaewon Kim
# ==========================================

import pandas as pd

# expression 데이터 로드
data = pd.read_csv("immune_projects/immune_expression.csv")

# 평균 expression 계산
average_expression = data["expression"].mean()

# 평균 이상 유전자 추출
high_expression_genes = data[
    data["expression"] > average_expression
]

# immune marker gene 예시
immune_marker = [
    "FOXP3",
    "IFNG",
    "CD8A",
    "CTLA4",
    "PDCD1"
]

# marker gene 추출
marker_genes = data[
    data["gene"].isin(immune_marker)
]

print(f"Average expression: {average_expression:.2f}")

print("\nHigh expression genes:")
print(high_expression_genes)

print("\nImmune marker genes:")
print(marker_genes)

# 결과 저장
high_expression_genes.to_csv(
    "immune_projects/high_expression_genes.csv",
    index=False
)

marker_genes.to_csv(
    "immune_projects/immune_marker_genes.csv",
    index=False
)