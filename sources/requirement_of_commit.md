# 커밋 메세지 규칙
1. 제목과 본문은 **빈 행으로 구분**
2. 제목은 **50글자 이내**
3. 제목은 **명령문**으로 작성
4. 어떻게 보단 **무엇과 왜**를 작성

# 커밋 메세지 구조
```
# Header, Body, Footer는 빈 행으로 구분한다.
타입(스코프): 주제(제목) # Header(헤더)

본문 # Body(바디)

바닥글 # Footer
```

```
# 메세지 예시
fix: Safari에서 모달을 띄웠을 때 스크롤 이슈 수정

모바일 사파리에서 Carousel 모달을 띄웠을 때,
모달 밖의 상하 스크롤이 움직이는 이슈 수정.

issue: #1137
```

<table><thead><tr><th>타입 이름</th><th>내용</th></tr></thead><tbody><tr><td>feat</td><td>새로운 기능에 대한 커밋</td></tr><tr><td>fix</td><td>버그 수정에 대한 커밋</td></tr><tr><td>build</td><td>빌드 관련 파일 수정 / 모듈 설치 또는 삭제에 대한 커밋</td></tr><tr><td>chore</td><td>그 외 자잘한 수정에 대한 커밋</td></tr><tr><td>ci</td><td>ci 관련 설정 수정에 대한 커밋</td></tr><tr><td>docs</td><td>문서 수정에 대한 커밋</td></tr><tr><td>style</td><td>코드 스타일 혹은 포맷 등에 관한 커밋</td></tr><tr><td>refactor</td><td>코드 리팩토링에 대한 커밋</td></tr><tr><td>test</td><td>테스트 코드 수정에 대한 커밋</td></tr><tr><td>perf</td><td>성능 개선에 대한 커밋</td></tr></tbody></table>