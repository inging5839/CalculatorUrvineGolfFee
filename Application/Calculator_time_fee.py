import pandas as pd

def calculator_time_fee():
    # 엑셀 파일 불러오기 (특정 시트만 지정)
    excel_file_path = '/Users/geon/Desktop/Golf_Cost_Auto_System/gathered.xlsx' # 엑셀 파일 이름 작성
    sheet_name = 'Sheet1'  # 원하는 시트의 이름 또는 인덱스 (0부터 시작)
    sat_start_day = 5 # ------------ 해당 월의 첫 토요일 날짜를 작성해주세요 -------------- # 24년 9월 달력 예외발생!!!!! 수정 필요 (24.10.01 작성)
    sun_start_day = sat_start_day + 1 
    holiday = [1, 3, 9] # 해당 월의 공휴일을 리스트 형식으로 작성해주세요. -> 주말과 겹치지 않는 공휴일만 추가 -> 없으면 공백
    origin_df = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=None)
    try:
        # 엑셀 파일 읽기
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

        # print(df.at[4, '시간'])
        # '시간' 열의 데이터 값의 앞 두 글자가 15보다 작은 경우에 해당하는 행의 'O' 열에 7000 값을 부여

        # 14시 까지 입장 시 시간 당 7,000원
        df.loc[df[2].astype(str).str[:2].astype(int) < 15, 9] = 7000
        df.loc[df[2].astype(str).str[:2].astype(int) >= 15, 9] = 10000


        # 평일 - 14시 까지 입장 -> 이후 연속된 시간은 15시 이후에도 7,000원
        for i in range(0, len(df[4])):
            if i == len(df[4]) - 1:
                break
            if (df[4][i]) == (df[4][i+1]) and (int(df[2][i][:2])+1 == int(df[2][i+1][:2])) and (int(df[9][i]) == 7000):
                df.loc[i+1, 9] = 7000
        # 주말 이용 전체 10,000원 설정
        for i in range(0, 5):
            df.loc[df[0].astype(str).str[8:].astype(int) == sat_start_day, 9] = 10000
            df.loc[df[0].astype(str).str[8:].astype(int) == sun_start_day, 9] = 10000
            sat_start_day = sat_start_day + 7
            sun_start_day = sun_start_day + 7
        # 공휴일 이용 전체 10,000원 설정
        for i in holiday:
            df.loc[df[0].astype(str).str[8:].astype(int) == i, 9] = 10000

        # 데이터 기존 파일에 덮어쓰기
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)


    except Exception as e:
        print(f"오류 발생: {e}")

    return df
