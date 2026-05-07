# ====================================
# 프로젝트: DNA 서열 GC 함량 분석기
# 기능: 다양한 패턴의 DNA 서열을 분석하고 파일로 리포트 생성
# 작성자: 김재원
# ====================================

dna_list = ['GGCCCGGGGCGCGCGGCCGCG', # GC-rich region (높은 결합력 테스트)
           'ATAAAATATTTTTATATATTA', # AT-rich region (낮은 결합력 테스트) 
           'ATGCCGTACGTAGCTAGCTAG', # 일반적인 유전자 서열 패턴 1
           'CGTATGCTAGCTAGGCTAAC', # 일반적인 유전자 서열 패턴 2
]
with open("gc_content_analysis_report.txt", "w")as f:
    f.write("--- 분석 결과 ---\n")
    for s in dna_list:
        n = len(s)
        g_count = 0
        for base in s:
            if base in "GC":
                g_count += 1
                
        gc_ratio = (g_count / n) * 100
        
        result_line = f" {s} | length: {n} | GC: {gc_ratio:.2f}%\n"
        f.write(result_line)

        print(f"분석 완료: {s}({gc_ratio:.2f}%)")

    print("\n모든 분석 결과가 'gc_content_analysis_report"
    ".txt'에 저장되었습니다.")