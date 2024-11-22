import os
import pandas as pd
from openpyxl import Workbook, load_workbook


# 폴더에 있는 엑셀 파일 목록 가져오기

def gather_data():
    folder_path = '/Users/geon/Desktop/Golf_Cost_Auto_System'
    excel_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    print(excel_files)
    for excel_file in excel_files:
        wb = load_workbook(excel_file)
        wb.save(excel_file)
        os.system("osascript -e 'quit app \"Microsoft Excel\"'")

    excel_files.sort()
    print(excel_files)

    # 모든 엑셀 파일을 읽어서 DataFrame으로 저장
    dfs = []
    result_df = pd.DataFrame()
    for file in excel_files:
        # file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file, header=None)
        add_data = df.iloc[2:]
        print(add_data)
        result_df = pd.concat([result_df, add_data], ignore_index=True)

    # 모든 데이터프레임을 하나로 합치기
    # merged_df = pd.concat(dfs, ignore_index=True)

    # 특정 열을 기준으로 정렬
    #sorted_df = merged_df.sort_values(by=2, ascending=True)
    #sorted_df = merged_df.sort_values(by=1, ascending=True)
    #sorted_df = merged_df.sort_values(by=0, ascending=True)

    # 정렬된 데이터프레임을 새로운 엑셀 파일로 저장
    output_path = '/Users/geon/Desktop/Golf_Cost_Auto_System/gathered.xlsx'
    result_df.to_excel(output_path, index=False)

    print(f'모든 엑셀 파일을 합쳐서 정렬된 결과를 {output_path}에 저장했습니다.')
