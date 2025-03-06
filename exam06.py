# 터미널 실행 방법 : 터미널 -> python 파일이름.py 

def print_menu():
    print("##### 메뉴 #####")
    print("1. 명함 추가")
    print("2. 명함 목록")
    print("3. 이름으로 검색")
    print("4. 번호로 변경")
    print("5. 이름으로 변경")
    print("6. 번호로 삭제")
    print("7. 이름으로 삭제")
    print("99. 종료")

def main():
    cards = [{'no':1, 'name':"홍길동",'tel':'1234'}, {'no':2, 'name':"전우치",'tel':'2222'}]
    new_no = 3
    while True:
        print_menu()
        choice = input("메뉴 선택 : ")
        # 1 2 4 7
        if choice == '1':   # 명함 추가
            name = input("- 이름 입력 : ")
            tel = input("- 연락처 입력 : ")
            card = {'no':new_no, 'name':name, 'tel':tel}
            cards.append(card)
            new_no+=1
        elif choice == '2':    # 명함 목록 출력
            print(cards)

        elif choice == '3':   # 이름으로 검색
            name = input("- 검색할 이름을 입력하세요 : ")
            for card in cards:
                if card['name']==name:
                    print(card)
                    break
        elif choice == '4':        # 번호 변경
            no = int(input(" - 번호 입력 : "))
            # 찾아낸 명함을 저장할 변수. 초기값은 None -> 검색에 실패하면 None이 유지
            find_card = None
            # cards의 명함을 한장씩 꺼내 명함의 no가 사용자가 입력한 no와 일치하는자 비교
            # 일치하면 find_card 에 저장한 다음 검색을 중지
            for card in cards:
                if card['no']==no:
                    find_card = card
                    break
            if find_card==None:
                print("@@ 명함을 찾지 못했습니다.@@")
            else:
                tel = input(" - 변경할 연락처 : ")
                find_card['tel'] = tel
        elif choice == '5':     # 이름으로 변경
            name = input(" - 변경할 이름 입력 : ")
            find_card = None
            for card in cards:
                if card['name']==name:
                    find_card = card
                    break
            if find_card==None:
                print("@@ 명함을 찾지 못했습니다 @@")
            else:
                tel = input(" - 변경할 전화번호 입력 :")
                name = input(" - 변경할 이름 입력 : ")
                find_card['tel'] = tel
                find_card['name'] = name
        elif choice == '6':         # 번호로 검색 후 삭제
            no = input(" - 번호 검색 :")
            find_card = None
            for card in cards:
                if card['no'] == no:
                    find_card = card
                    break
            if find_card == None:
                print("@@ 명함을 찾지 못했습니다 @@")
            else:
                cards.remove(card)         
        elif choice == '7':         # 이름으로 검색 후 삭제
            name = input(" - 찾을 이름 입력 : ")
            find_card = None
            for card in cards:
                if card['name']==name:
                    find_card = card
                    break
            if find_card==None:
                print("@@ 명함을 찾지 못했습니다 @@")
            else:
                cards.remove(card)

        elif choice =='99':
            print("+++ GOOD BYE +++")
            break

main()