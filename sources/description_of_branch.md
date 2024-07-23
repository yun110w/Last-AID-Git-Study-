## 브랜치 명령어

```bash
# '{', '}'는 입력하지 마세요

git branch # 현재 생성되어 있는 branch 출력
git branch {new_branch} # HEAD에서 new_branch 생성 **checkout은 안 함**
git checkout -b {new_branch} # HEAD에서 new_branch 생성 이후 checkout까지 완료
git branch --delete {old_branch} # old_branch 삭제, -d로 대체, **branch의 추가 커밋이 없을 때만 삭제 가능** 
git branch --delete --force {old_branch} # old_branch 삭제, -D로 대체, **old_branch의 커밋 내용이 있어도 강제 삭제 가능**
```

## 각 브랜치 설명

|features|develop|release|hotfix|master(main)|
|:---:|:---:|:---:|:---:|:---:|
|파생|기반|파생|파생|기반|

#### Master(Main)
- 중심이 되는 2개의 branch 중 하나. 최종 릴리즈에 사용되는 branch로 태깅을 통해 버전관리

#### Develop
- 중심이 되는 또다른 branch. 차기 릴리즈를 위한 개발의 메인으로 추가 기능 개발시 Develop에서 Feature branch를 생성
- 개발이 완료된 기능은 Develop branch로 merge

#### Feature
- Feature branch는 origin에 반영되는게 아닌, 개발자의 repo에 존재
- Merge가 완료되면 branch는 삭제

#### Release
기능개발이 완료되어 차기 릴리즈를 위한 준비가 되면 Develop branch에서 생성
- 이 시점부터 Develop branch에는 차차기 릴리즈를 위한 개발이 가능
  
Release branch에는 버그픽스를 위한 수정만 커밋되고, __버그 픽스가 완료되면__ Master branch, Developer branch의 두곳에 merge (경우에 따라서는 develop branch에는 매 버그 픽스마다 merge 되기도 함.)

- Master branch에 tagging을 통해 릴리즈 버전을 기록

#### Hotfix
Production환경에서 버그가 발생하면 Master branch에서 생성.
수정 완료 후 Master branch, Developer branch의 두곳에 merge

- Master branch에 tagging을 통해 핫픽스 릴리즈버전을 기록
- Release branch가 있다면 해당 branch에도 merge 필요