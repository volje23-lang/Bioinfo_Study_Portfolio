# ==========================================
# Project: DNA GC Content Analyzer
# Goal: Analyze GC content from multiple DNA sequences
# Author: Jaewon Kim
# ==========================================

dna_list = [

    'GGCCCGGGGCGCGCGGCCGCG',  # GC-rich sequence
    'ATAAAATATTTTTATATATTA',  # AT-rich sequence
    'ATGCCGTACGTAGCTAGCTAG',  # Typical DNA sequence 1
    'CGTATGCTAGCTAGGCTAAC',   # Typical DNA sequence 2
]

# 결과 저장 파일 열기
with open("gc_content_analysis_report.txt","w") as f:
    f.write("--- Analysis Result ---\n")

    # 각 DNA sequence 분석
    for s in dna_list:

        n = len(s)

        # G / C 개수 확인
        g_count = 0

        for base in s:

            if base in "GC":
                g_count += 1

        # GC content 계산
        gc_ratio = (g_count / n) * 100

        # 결과 저장
        result_line = f"{s} | length: {n} | GC: {gc_ratio:.2f}%\n"
        f.write(result_line)

        # 진행 상황 출력
        print(f"Sequence analyzed: {s} ({gc_ratio:.2f}%)")

print("\nAll analysis results saved to 'gc_content_analysis_report.txt'")
