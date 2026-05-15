# ==========================================
# Project: GEO-style Immune Expression Analysis
# Goal: Compare immune gene expression  between healthy and inflammatory conditions
# Author: Jaewon Kim
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# GEO-style 데이터셋 핸들링 연습
data = pd.read_csv("immune_projects/geo_style_expression.csv")

# pseudo-count 적용 (0으로 나눠지는 에러 방지용)
data["fc"] = (
    (data["inflammatory_TPM"] + 1e-5) /
    (data["healthy_TPM"] + 1e-5)
)

# expression 변화 비교를 위해 log2FC 적용
data["log2FC"] = np.log2(data["fc"])

# log2FC >= 1은 대략 2배 증가로 보고 간단히 분류
data["status"] = "Steady"
data.loc[data["log2FC"] >= 1, "status"] = "Up"
data.loc[data["log2FC"] <= -1, "status"] = "Down"

up_genes = data[data["status"] == "Up"]

print(f"[GEO-style Analysis] Total genes: {len(data)}")
print(f"Up-regulated genes: {len(up_genes)}")

# immune-related gene expression 변화 시각화
plt.figure(figsize=(10, 5))
plt.bar(data["gene"], data["log2FC"])

plt.axhline(1, color="red", linestyle="--", alpha=0.5)
plt.axhline(-1, color="blue", linestyle="--", alpha=0.5)

plt.xlabel("Immune-related genes")
plt.ylabel("log2 Fold Change")
plt.title("Immune Expression Change (Inflammatory vs Healthy)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/geo_style_barplot.png")
plt.show()

# 분석 결과 저장
data.to_csv("immune_projects/geo_results.csv", index=False)
up_genes.to_csv("immune_projects/geo_upregulated_genes.csv", index=False)
