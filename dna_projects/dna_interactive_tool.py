# ==========================================
# Project: Interactive DNA Sequence Analyzer
# Goal: Analyze GC content from user input
# Author: Jaewon Kim
# ==========================================

while True:

    print("-" * 40)

    # 사용자 입력 받기
    user_input = input("Enter DNA sequence (q to quit): ").strip().upper()

    # 프로그램 종료
    if user_input == "Q":

        print("Exiting program...")
        break

    # 빈 입력 처리
    if not user_input:

        print("[Error] Empty input")
        continue

    # DNA sequence 유효성 확인
    is_valid = True

    for base in user_input:

        if base not in "ATGC":

            print(f"[Error] Invalid character: '{base}'")

            is_valid = False
            break

    if not is_valid:
        continue

    # sequence 기본 분석
    length = len(user_input)

    g_count = user_input.count("G")
    c_count = user_input.count("C")

    gc_ratio = (
        (g_count + c_count) / length
    ) * 100

    print("\n[Sequence Analysis]")

    print(f"Input Seq : {user_input}")
    print(f"Length    : {length}")
    print(f"GC Content: {gc_ratio:.2f}%")

    # GC content 기준 분류
    if gc_ratio >= 60:
        status = "GC-rich"

    elif gc_ratio >= 40:
        status = "Normal"

    else:
        status = "AT-rich"

    print(f"Status : {status}")

    # 결과 로그 저장
    with open("interactive_dna_log.txt", "a") as f:

        f.write("\n[Interactive Session Analysis]\n")

        f.write(f"Input Seq : {user_input}\n")
        f.write(f"Length    : {length}\n")
        f.write(f"GC Content: {gc_ratio:.2f}%\n")
        f.write(f"Status    : {status}\n")

        f.write("-" * 35 + "\n")

    print("\nAnalysis results saved to 'interactive_dna_log.txt'")
    