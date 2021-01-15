from PIL import Image, ImageDraw, ImageFont
# PIL 패키지는 이미지 처리에 유용한 패키지이다.
import textwrap  # textwrap : word-wrapping과 같은 텍스트 처리를 한다.
import random

from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QGridLayout, QLabel, QTextEdit, \
    QPushButton, QMessageBox
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 그리드 레이아웃
        grid = QGridLayout()
        self.setLayout(grid)

        self.TextEdit1 = QTextEdit()

        grid.addWidget(self.TextEdit1, 0, 1)
        grid.addWidget(QLabel('띄어쓰기 포함 33자까지만 가능합니다.'), 1, 1)
        grid.addWidget(QLabel('33자가 넘어가면 가운데 정렬이 안 되니 주의해주세요.'), 2, 1)
        grid.addWidget(QLabel(''), 3, 1)

        # 버튼 생성
        btn = QPushButton('&Download', self)
        grid.addWidget(btn, 4, 1)
        btn.setCheckable(True)
        btn.toggle()
        btn.clicked.connect(self.btn_clicked)

        self.setWindowTitle("Creating Thumbnail image")  # 타이틀바에 나타나는 창의 제목을 설정함.
        self.setGeometry(300, 300, 300, 200)
        self.center()
        self.show()  # 위젯을 스크린에 보여준다.

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_clicked(self):
        try:
            print(self.TextEdit1.toPlainText())
            # TextEdit1에 쓰여있는 글자를 가져온다.
            run(self.TextEdit1.toPlainText())
            QMessageBox.about(self, "Success", "Success download")

        except:
            print("error!")


# 배경색 랜덤으로 추출하는 함수
def random_bg_color():
    rgbl = []

    for num in range(3):  # 숫자 3개 뽑기
        num = random.randint(0, 255)  # 0부터 255까지 추출
        rgbl.append(num)
        # random.shuffle(rgbl) #suffle함수 : 리스트 항목 섞기

    return tuple(rgbl)


# RUN 메서드
def run(file_name):
    para = textwrap.wrap(file_name, width=11)  # 각 줄당 최대 글자수 11개까지 (띄어쓰기 포함)
    max_w, max_h = 480, 480  # 이미지 사이즈 480x480
    bg_color = 'rgb' + str(random_bg_color())  # 랜덤숫자를 rgb 형식으로 바꾸기

    image = Image.new('RGB', (max_w, max_h), bg_color)
    # Image.new(mode,size,color) > 주어진 형식의 새로운 이미지를 생성한다.
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('C:/Users/0206d/Downloads/Noto_Sans_KR/NotoSansKR-Bold.otf', size=50)
    font_color = 'rgb(0,0,0)'  # 글자 색상은 검정(black)

    current_h, pad = 0, 10  # currnet_h는 현재 높이 위치, pad는 줄간격

    if len(file_name) <= 11:
        current_h = 180

    elif len(file_name) <= 22:
        current_h = 150

    else:
        current_h = 110

    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((max_w - w) / 2, current_h), line, font=font, fill=font_color)
        current_h += h + pad

    image.save('{}.png'.format(file_name[:5]))  # 제목의 5자까지 잘라서 파일명으로 입력 후 저장
    print('download done')
    return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
