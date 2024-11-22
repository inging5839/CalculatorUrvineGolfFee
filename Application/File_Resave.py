import subprocess
import os
import time
import Golf_Cost_Auto_Download as GCAD

def file_resave(month, day_volumn):
    for i in range(day_volumn):
        if i < 9:
            file_path = f'/Users/geon/Desktop/Golf_Cost_Auto_System/2024-{month}-0{i+1}.xlsx'
        else:
            file_path = f'/Users/geon/Desktop/Golf_Cost_Auto_System/2024-{month}-{i+1}.xlsx'
        subprocess.run(["osascript", "-e", f'tell application "Microsoft Excel" to open POSIX file "{file_path}"'])

        # 시간 대기 (엑셀이 열려 있는 동안 기다림, 필요에 따라 조절)
        time.sleep(1)

        # 엑셀 파일 저장
        subprocess.run(["osascript", "-e", 'tell application "Microsoft Excel" to save active workbook'])

        # 엑셀 어플리케이션 종료
        subprocess.run(["osascript", "-e", 'tell application "Microsoft Excel" to quit'])

        print(f"File '{file_path}' opened, saved, and Excel application closed successfully.")
