# :pushpin: Phase 1 

1. 현재 커밋에 'v0.1'라는 태그를 달아주세요.
2. dev 브랜치를 만들고 checkout 해주세요.
3. add, sub, mul, div의 주석을 하나씩 제거하며 커밋을 해주세요. (커밋 4번 하여도 좋음.)
4. `work_dir`에 special_functions.py를 만들고 아래 내용을 붙여넣고 커밋 해주세요. (코드만. 코드블럭 전체 X)

```python
def pow(a, b):
    pass

def abs(a):
    pass

def mod(a, b):
    pass
```

👉: `Tag`, `branch 생성`, `commit`

---


# :pushpin: Phase 2 


```bash
# Phase가 끝났으니 팀원들에게 아래 명령어를 입력하라 하세요.
git fetch origin # remote 변경사항 체크
git checkout dev # 브랜치 변경
git pull origin dev # remote dev 변경사항을 다운로드(pull)
```

1. testPrint()에 대한 issue와 hotfix branch(이름: hotfix-testPrint)를 main에서 만들어주세요.
2. add, sub, mul, div에 대한 issue와 branch(이름: feat-basic)를 만들어주세요.
> 팀원에게 `git fetch origin`, `git checkout {branch}`를 치라고 하세요.
> 
> 이거 왜 해야되냐고 물어보면 remote에서 만들어진 branch를 local로 가져온 뒤 체크아웃하는거라 알려주세요. 

3. pow, abs, mod에 대한 issue와 branch(이름: feat-special)를 만들어주세요.
4. 팀원에게 hotfix, features branch 에서 기능 구현을 요청하세요.
5. `hotfix branch`에서 작업이 끝나면 dev, main으로 PR을 보내라고 하세요.
6. dev, main에서 merge 한 뒤 issue를 닫으세요.

👉: `branch 생성`, `fetch`, `checkout`, `issue`, `PR`

---

# :pushpin: Phase 3 

```bash
# Phase가 끝났으니 팀원들에게 아래 명령어를 입력하라 하세요.
git fetch origin # remote 변경사항 체크
git checkout dev # 브랜치 변경
git pull origin dev # remote dev 변경사항을 다운로드(pull)
```


1. feat-basic branch의 PR을 확인 후 dev로 merge를 진행하세요.
2. dev에서 배포 준비를 위한 release branch를 만들어 주세요.
3. local에서 rel branch를 만든 경우 `git push -u origin release`, remote에서 만든 경우는 `git fetch origin`을 쳐주세요.

> `git fetch origin`, `git checkout {branch}`를 치라고 하세요.
> 
> 이거 왜 해야되냐고 물어보면 remote에서 만들어진 branch를 local로 가져오는거라고 알려주세요.

4. release branch에서 bug를 발견했다는 issue를 작성하세요.
5. release branch에서 calculator.py 안에 아무 곳이나 Enter를 두 번 쳐서 코드를 수정하고 commit 하세요.
6. dev와 main에 merge 하세요.
7. main branch에 새로운 태그(v1.0)를 달아주세요. 
8. pow, abs, mod에 대한 branch(이름: feat-special-additional)를 추가로 만들어주세요.
9. 다른 팀원에게 추가로 feat-special-additional branch에서 pow, abs, mod의 작성을 요청하세요.

👉: `branch 생성`, `push --set-upstream`, `merge`, `PR`, `tag`

---

# :pushpin: Phase 4


```bash
# Phase가 끝났으니 팀원들에게 아래 명령어를 입력하라 하세요.
git fetch origin # remote 변경사항 체크
git checkout dev # 브랜치 변경
git pull origin dev # remote dev 변경사항을 다운로드(pull)
```

1. special_functions.py를 작성한 두 명에게 PR은 dev로 보내달라고 말해주세요.
2. 먼저 온 PR을 merge하세요.
3. 팀장의 판단하에 기존 코드와 두 번째 PR 의 Conflict를 해결하세요.
4. calculator.py 의 line 1에서 '#'만 지워 import special_functions.py 만 남게 해주세요.

👉: `conflict`, `merge`

---


# :pushpin: Phase 5
```bash
# Phase가 끝났으니 팀원들에게 아래 명령어를 입력하라 하세요.
git fetch origin # remote 변경사항 체크
git checkout dev # 브랜치 변경
git pull origin dev # remote dev 변경사항을 다운로드(pull)
```

1. 팀원들과 회의하여 workflow를 직접 작성하고 스터디장에게 알려주세요.
2. 실행하고 `git log --oneline --graph --all`로 결과를 보여주세요.

👉: `git workflow`, `log`

---

### 여기까지 따라오시느라 고생 많으셨습니다. 

### 감사합니다.