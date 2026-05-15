# ==========================================
# Project: Simple Differential Expression Analysis
# Goal: Compare immune marker gene expression
# Author: Jaewon Kim
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# expression 데이터 로드
try:
    data = pd.read_csv("immune_projects/immune_condition_expression.csv")
except FileNotFoundError:
    print("File path error: please check immune_condition_expression.csv")

# treated / control 비율 계산
data["fold_change"] = (
    (data["treated_TPM"] + 1e-5) /
    (data["control_TPM"] + 1e-5)
)

# expression 변화 비교를 위해 log2FC 적용
data["log2FC"] = np.log2(data["fold_change"])

# log2FC 기준으로 간단히 Up / Down 분류
data["status"] = "Steady"
data.loc[data["log2FC"] >= 1, "status"] = "Up"
data.loc[data["log2FC"] <= -1, "status"] = "Down"

upregulated_genes = data[data["status"] == "Up"]
downregulated_genes = data[data["status"] == "Down"]

print("[Simple Differential Expression Analysis]")
print(data[["gene", "control_TPM", "treated_TPM", "fold_change", "log2FC", "status"]])

print("\nUp-regulated genes:")
print(upregulated_genes[["gene", "log2FC", "status"]])

print("\nDown-regulated genes:")
print(downregulated_genes[["gene", "log2FC", "status"]])

# 조건별 immune marker expression 시각화
x = np.arange(len(data["gene"]))

plt.figure(figsize=(10, 6))
plt.bar(x - 0.2, data["control_TPM"], width=0.4, label="Control")
plt.bar(x + 0.2, data["treated_TPM"], width=0.4, label="Treated")

plt.xticks(x, data["gene"], rotation=45)
plt.ylabel("Expression Level (TPM)")
plt.title("Immune Gene Expression Changes: Control vs Treated")
plt.legend()
plt.tight_layout()

# 결과 저장
data.to_csv("immune_projects/differential_expression_results.csv", index=False)
upregulated_genes.to_csv("immune_projects/upregulated_genes.csv", index=False)
downregulated_genes.to_csv("immune_projects/downregulated_genes.csv", index=False)

plt.savefig("outputs/differential_expression_barplot.png")
plt.show()

print("\nResults saved as CSV files and barplot image.")