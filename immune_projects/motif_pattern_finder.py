# ==========================================
# Project: DNA Motif Pattern Finder
# Goal: Find repeated DNA motifs in sequences
# Author: Jaewon Kim
# ==========================================

import pandas as pd

# DNA sequence 데이터 로드
data = pd.read_csv(
    "immune_projects/dna_motif_sequences.csv"
)

# motif 탐색 연습
target_motif = "ATG"

print("[DNA Motif Pattern Finder]")
print(f"Target motif: {target_motif}\n")

motif_counts = []

# 각 sequence에서 motif 개수 확인
for index, row in data.iterrows():

    sequence_id = row["sequence_id"]
    dna_sequence = row["dna_sequence"]

    motif_count = dna_sequence.count(target_motif)

    motif_counts.append(motif_count)

    print(f"{sequence_id}")
    print(f"Sequence: {dna_sequence}")
    print(f"{target_motif} count: {motif_count}")

    # 간단한 motif 분류
    if motif_count >= 3:
        print("Possible motif-rich sequence")

    elif motif_count >= 1:
        print("Motif detected")

    else:
        print("No motif detected")

    print("-" * 40)

# 결과 저장
data["ATG_count"] = motif_counts

data.to_csv(
    "immune_projects/motif_search_results.csv",
    index=False
)

print("Motif search results saved.")