def main():
    str = []
    print("##### name list #####")
    while True:
        print("=== 메뉴 선택 ===")
        print("1. 이름 추가")
        print("2. 이름 전체 목록")
        print("3. 이름 존재 여부")
        print("4. 이름 삭제")
        print("5. 종료.")


        choice = input("메뉴를 선택하세요 : ")
        if choice == "1":
            add_name = input("추가할 이름을 입력하세요 : ")
            str.append(add_name)
        elif choice == "2":
            print(f'name_list = {str}')
        elif choice == "3":
            check_name = input("확인할 이름을 입력 : ")
            if check_name in str:
                print(f"{check_name}은 존재합니다.")
            else:
                print(f"{check_name}은(는) 존재하지 않습니다.")
        elif choice == "4":
            delete_name = input("삭제할 이름을 입력 : ")
            if delete_name in str:
                str.remove(delete_name)
            else:
                print(f'{delete_name}을 찾을 수 없습니다.')
        elif choice == "5":
            print("Thank you - 사용해주셔서 감사합니다")
            break
    

main()