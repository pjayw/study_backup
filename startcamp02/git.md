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
 
>git config --global user.name : 이름 추가
 
>목록 확인 : git config --global --list

>git log : 로그를 보여준다

>git commit --amend : 수정 , insert키로 수정 

> 수정페이지 탈출 -> :wq

## 로컬저장소

- git add . 을 하면 현재 폴더의 변동사항을 한번에 추가
- 깃 허브 업로드 : git remote add 지정할이름 **{깃허브주소}**
- 깃 허브 수정: git push origin master
- 연결된 저장소 확인 : git remote -v 
- shift + insert 또는 우클릭 시 복사 가능
- git clone **{저장소 주소}** 집컴과 강의실 저장소 일치시킴
> 클론은 최초로 받을때만 쓰고, 다음부터는 git에 대한 정보가 있기때문에 
git remote 정보를 받을 수 있다.

## 강의 및 집에서 파일 저장 루틴
1. 강의장에서 (academy폴더에) 새 파일 생성
2. add commit push (gitlab으로 푸시) *push -> (업로드)
3. 집(home 폴더에서) git pull
4. 집에서 새 파일 생성
5. add commit push (gitlab으로 푸시) 
6. 강의장에서 git pull gitlab master

## 집에서 강의장에 있는 파일 저장
1. gitlab에서 clone 복사
2. git clone 주소
3. cd 내려받은폴더이름/ -> 마스터가 떠야됨
*주소 이름 바꾸기*
- git remote rename 원래이름 바꿀이름
- 새 파일 생성 -> touch 만들파일이름.확장자

## 자주 하는 실수 
- 강의장에서 저장한 것을 원격 저장소에 push하지 않고 집에서 수정 후 push 한 후 강의장에서 pull해서 받았더니 버전이 안맞아서 merge가 일어남 