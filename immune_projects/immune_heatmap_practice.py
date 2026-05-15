
# ==========================================
# Project: Immune Heatmap Practice
# Goal: Visualize immune marker expression across samples
# Author: Jaewon Kim
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# 히트맵 연습용 데이터셋 로드
data = pd.read_csv("immune_projects/immune_heatmap_data.csv")

# 유전자명을 인덱스로 설정
heatmap_data = data.set_index("gene")

print("[Immune Heatmap Data Check]")
print(heatmap_data)

# heatmap 시각화
plt.figure(figsize=(8, 6))

# colormap 변경 연습
im = plt.imshow(
    heatmap_data,
    aspect="auto",
    cmap="YlGnBu"
)

# 색상 기준 바 추가
plt.colorbar(im, label="Expression level")

# 샘플명 / 유전자명 표시
plt.xticks(
    range(len(heatmap_data.columns)),
    heatmap_data.columns
)

plt.yticks(
    range(len(heatmap_data.index)),
    heatmap_data.index
)

# 히트맵 위에 expression 값 표시
for i in range(len(heatmap_data.index)):
    for j in range(len(heatmap_data.columns)):
        plt.text(
            j,
            i,
            f"{heatmap_data.iloc[i, j]:.1f}",
            ha="center",
            va="center",
            color="black"
        )

plt.title("Immune Marker Expression Heatmap")
plt.xlabel("Samples")
plt.ylabel("Genes")

plt.tight_layout()

plt.savefig("outputs/immune_heatmap_v2.png")

plt.show()

# 가공된 데이터 저장
heatmap_data.to_csv(
    "immune_projects/processed_heatmap.csv"
)

print("\nHeatmap image and processed table saved.")