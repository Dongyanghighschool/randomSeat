import tkinter as tk
import random
from tkinter import messagebox
import threading
import pygame

# pygame 믹서 초기화
pygame.mixer.init()

# 사람 리스트
names = ['오현', '김주화', '김은주', '김진혁', '손정아', '김상희', '김기성', '박경진',
         '이현수', '박연숙', '조영수', '이효상', '노성용', '박현숙', '김아름', '정호재',
         '김민정', '박보상', '윤상태', '오재석', '김민지', '이승민', '강민구', '김기진',
         '강경훈', '염성군', '김정연', '대명은', '이선화', '이동원', '김수아', '김진상']

# 사람 리스트 섞기
random.shuffle(names)

# 자리 배치 순서
assign_order = [3, 4, 2, 5, 1, 6, 0, 7]  # 0부터 시작하는 행 인덱스

# GUI 생성
root = tk.Tk()
root.title("이쪽이 앞이에요~^^")

# 자리 표 생성
labels = [[tk.Label(root, text="", width=15, height=2, relief="ridge", borderwidth=1)
           for _ in range(4)] for _ in range(8)]

for i in range(8):
    for j in range(4):
        labels[i][j].grid(row=i, column=j)

idx = 0  # names 리스트의 현재 인덱스
step = 0  # 현재 단계

def play_sound():
    # 효과음 파일 경로를 지정해주세요 (예: 'sound.mp3' 또는 'sound.wav')
    pygame.mixer.music.load('/Users/jinhyukkim/Desktop/develop/random_seat/효과음.mp3')
    pygame.mixer.music.play()

def assign_row(row):
    global idx
    for col in range(4):
        name = names[idx]
        labels[row][col].config(text=name)
        idx += 1
    # 효과음 재생 (별도의 스레드에서 실행)
    threading.Thread(target=play_sound).start()

def next_step():
    global step
    if step < len(assign_order):
        row = assign_order[step]
        assign_row(row)
        step += 1

        # 두 개의 행을 배치한 후 2초 쉬기
        if step % 2 == 0 and step < len(assign_order):
            root.after(2000, next_step)
        else:
            root.after(500, next_step)
    else:
        # 모든 배치 완료
        messagebox.showinfo("자리 배치 완료", "모든 자리가 배치되었습니다.")

# 시작 버튼 생성
start_button = tk.Button(root, text="자리 배치 시작", command=lambda: root.after(1000, next_step))
start_button.grid(row=8, column=0, columnspan=4)

root.mainloop()
