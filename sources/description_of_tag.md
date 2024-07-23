# Tag 명령어

```bash
git tag -l # tag 리스트 출력
git tag -a {tag_name} -m "tag description" # HEAD에 tag 만들기
git tag -a {tag_name} {commit_number} -m "tag description" # 특정 커밋에 tag 만들기

git push --tags # 푸시하지 않으면 local에만 반영됩니다.
```

# Tag 설명

## 1.0.0의 '.'의 의미
1.0.0은 '.'을 기준으로 3 부분으로 나눌 수 있다.

> major.minor.patch
> 주(主).부(部).수(修)

major: 기존 버전과 호환되지 않게 API가 바뀌면 “주(主) 버전”을 올림
minor: 기존 버전과 호환되면서 새로운 기능을 추가할 때는 “부(部) 버전”을 올림
patch: 기존 버전과 호환되면서 버그를 수정한 것이라면 “수(修) 버전”을 올림
참고: 주.부.수 형식에 정식배포 전 버전이나 빌드 메타데이터를 위한 라벨을 덧붙이는 방법도 있다.

> 편의상 여기서 minor와 patch는 합쳐서 사용합시다.