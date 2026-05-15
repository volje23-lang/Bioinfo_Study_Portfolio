# ==========================================
# Project: FASTA Parser Practice
# Goal: Parse and analyze DNA sequence data from FASTA file
# Author: Jaewon Kim
# ==========================================

filename = "sample.fasta"

# FASTA 파일 읽기
with open(filename, "r") as file:
    lines = file.readlines()

# FASTA 형식 한 줄씩 처리
for line in lines:

    line = line.strip()

    # 빈 줄 제외
    if line == "":
        continue

    # FASTA header 확인
    if line.startswith(">"):

        print(f"Header: {line}")

    # DNA sequence 분석
    else:

        length = len(line)

        g_count = line.count("G")
        c_count = line.count("C")

        # GC content 계산
        gc_content = (
            (g_count + c_count) / length
        ) * 100

        # GC content 기준 간단 분류
        if gc_content >= 60:
            status = "GC-rich"

        elif gc_content >= 40:
            status = "Normal"

        else:
            status = "AT-rich"

        # 결과 출력
        print(f"Sequence: {line}")
        print(f"Length: {length}")
        print(f"GC Content: {gc_content:.2f}%")
        print(f"Status: {status}")

        print("-" * 30)