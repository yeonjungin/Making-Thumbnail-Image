# Making Thumbnail image
### 블로그 작성 시 썸네일을 매번 만들어내는 게 귀찮아서 만들어낸 썸네일 자동 프로그램
#### 이 프로그램은 python 기반으로 작성되어 있다.
폰트는 NotoSansKR(Bold)이다.
배경색상은 랜덤으로 변경된다.
글자수는 33자 미만까지만 가능하게 설정되어 있다.

폰트는 자유롭게 변경이 가능하다.
run.py 파일에서 아래 해당하는 코드를 찾아서, 변경해주면 된다.
font = ImageFont.truetype('폰트파일 전체경로 적기', size=50)

![image](https://user-images.githubusercontent.com/47666431/111150411-68edb500-85d1-11eb-9053-3ccc0e4f1213.png)
