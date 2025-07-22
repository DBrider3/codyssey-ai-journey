# 과제

## 1. 기초 git 환경 구축
Git의 설정을 전역 범위로 아래와 같이 적용.
- 개행문자 설정 맥 input 값으로 지정
`git config --global core.autocrlf input`

- 사용자 이름과 이메일 주소를 설정
`git config --global user.name "DAEBEOM CHO"`
`git config --global user.email "tmdgns743@gmail.com"`

- 전역 기본 브랜치명을 main으로 설정
`git config --global init.defaultBranch main`

- 추가 팁: 기존 저장소에서 브랜치 이름 변경
기본 브랜치 `master` -> `main`으로 바꾸기
```bash
# 브랜치 이름 변경
git branch -m master main

# 원격에 새 브랜치 push
git push -u origin main

# 마지막으로 GitHub Repository Settings에서 기본 브랜치 설정도 변경해줘야 함

# 원격 저장소에서 master 브랜치 삭제
git push origin --delete master

# 최종 확인
git branch      # 로컬 브랜치 목록
git branch -r   # 원격 브랜치 목록
```

- 전역 설정 확인
`git config --global --list`

- 편집기로 열어서 수동으로 확인하기
`vi ~/.gitconfig`