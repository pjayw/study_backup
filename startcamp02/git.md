# GIT

**분산** 버전 관리 시스템

## 버전관리 예시
- google docs - 현재 버전 이름 저장
- 파일명에 날짜와 시간 기록하기 -> 파일간의 차이를 기억할 수 없음
- 위의 문제를 해결하려면 수정사항만 기록한 파일이 필요함
- git이 분산해서 관리해준다

> 중앙 집중식 : 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드

> 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리

---
---

## git의 역할
- 코드의 버전(히스토리)를 관리
- 코드의**변경 이력**을 기록하고 **협업**을 원활하게 하는 도구

---

### git의 3가지 영역
1. working directory
   - 작업 진행 공간
2. staging area
   - 변경을 기록할 파일을 업로드 해둠
3. repository
   - 버전 이력과 파일들이 영구적으로 저장되는 공간
   - 모든 버전과 변경 이력이 기록됨

> git init : 이 폴더를 깃이 관리하고있다.

> git status : 깃이 관리하는 파일을 알 수 있다

> git add 파일명 : 깃이 파일을 추적하도록 설정(staging area 등록)
> git commit -m {이름} : repository에 저장

>git config --global user.eamil : 이메일 추가
 git config --global user.name : 이름 추가
 목록 확인 : git config --global --list
