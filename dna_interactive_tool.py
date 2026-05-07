# ==================================
# 프로젝트: DNA 서열 대화형 분석기
# 기능: 사용자로부터 DNA를 입력받아 실시간으로 GC함량 분석
# 업데이트: 소문자 입력 허용 및 빈 값 입력 방어 로직 추가
# 작성자: 김재원
#===================================

while True:
    print("-" * 40)
    # 0. 입력 받기 (q 입력 시 종료, .strip().upper()로 공백 제거 및 대문자 변환)
    user_input = input("Enter DNA sequence (q to quit): ").strip().upper()
    
    if user_input == "Q":
        print("Exiting program... Goodbye!")
        break

    # 1. 빈 값 입력 방어 (에러 방지)
    if not user_input:
        print("[Error] No input detected. Please try again.")
        continue
    
    
    # 2. 유효성 검사 (A, T, G, C 외의 문자가 있는지 확인)
    is_valid = True
    for base in user_input:
        if base not in "ATGC":
            print(f"[Error] Invalid character: '{base}' (Only A, T, G, C are allowed)")
            is_valid = False
            break
    if not is_valid:
        continue

    # 3. 데이터 분석
    length = len(user_input)
    g_count = user_input.count("G")
    c_count = user_input.count("C")

    gc_ratio = ((g_count + c_count) / length) * 100

    # 4. 결과 출력
    print(f"\n[Sequence Analysis]")
    print(f"Input Seq : {user_input}")
    print(f"Length    : {length}")
    print(f"GC Content: {gc_ratio:.2f}%")
    
    if gc_ratio >= 60:
        status = "[GC-rich] High binding affinity"
    elif gc_ratio >= 40:
        status = "[Normal] Stable region"
    else:
        status = "[AT-rich] Low binding affinity"

    print(f">> Status : {status}")
        
   # 5. 파일 저장 
    with open("interactive_dna_log.txt", "a") as f:
        f.write(f"\n[Interactive Session Analysis]\n")
        f.write(f"Input Seq : {user_input}\n")
        f.write(f"Length    : {length}\n")
        f.write(f"GC Content: {gc_ratio:.2f}%\n")
        f.write(f"Result: {status}\n")
        f.write("-" * 35 + "\n")

    print("\n>> Analysis results have been logged to 'interactive_dna_log.txt'")
        
