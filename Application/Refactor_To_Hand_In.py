import pandas as pd

def refactor(target_month):
    excel_file = '/Users/geon/Desktop/Golf_Cost_Auto_System/gathered.xlsx'
    gathered_df = pd.read_excel(excel_file)

    data = pd.DataFrame(columns=['', '동', '호', '동호수', '이름', '날짜', '업장종류', '룸 번호', '시간',
                                 '', '결제상태', '기준금액', '결제단위', '판매금액'])


    data[''] = [''] * len(gathered_df)
    data['동'] = gathered_df[4].astype(str).str[:3].astype(int).tolist()
    data['호'] = gathered_df[4].astype(str).str[6:].astype(int).tolist()
    add_dong_ho = gathered_df[4].astype(str).str[:3] + '-' + gathered_df[4].astype(str).str[6:]
    data['동호수'] = add_dong_ho.tolist()
    data['이름'] = gathered_df[3].tolist()
    data['날짜'] = gathered_df[0].tolist()
    data['룸 번호'] = gathered_df[1].tolist()

    data['업장종류'] = [''] * len(gathered_df)

    data.loc[data['룸 번호'].astype(str) == '스크린골프(2단지)', '업장종류'] = '2단지스크린골프'
    data.loc[data['룸 번호'].astype(str) != '스크린골프(2단지)', '업장종류'] = '1단지스크린골프'
    data['시간'] = gathered_df[2].tolist()
    data['결제상태'] = ['결제완료'] * len(gathered_df)
    data[''] = [''] * len(gathered_df)
    data['기준금액'] = gathered_df[9].tolist()
    data['결제단위'] = [1] * len(gathered_df)
    data['판매금액'] = gathered_df[9].tolist()





    # df_new = pd.DataFrame(data)

    # 새로운 엑셀 파일에 데이터프레임 저장
    new_excel_path = f'/Users/geon/Desktop/Golf_Cost_Auto_System/{target_month}월_스크린골프_관리비_base.xlsx'
    data.to_excel(new_excel_path, index=False)

    print(f'{target_month}월 관리비 파일이 생성되었습니다: {new_excel_path}')
    
    
    # 필요없는 파일 지우기