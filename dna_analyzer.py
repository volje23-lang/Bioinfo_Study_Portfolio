sequences = ['ATTGCGA', 'CCGTAG', 'GGATTC', 'TTACGA']
print("--- 분석 결과 ---")
for seq in sequences:
    length = len(seq)
    gc_count = seq. count( 'G' ) + seq. count( 'C' )
    gc_content = (gc_count / length) * 100
    print(f"서열: {seq} | 길이: {length} | GC 함량: {gc_content:.1f}%")