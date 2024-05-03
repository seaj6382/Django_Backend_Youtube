# Django_backend_youtube
# 1일차

## 프로젝트 세팅

### 1. Github

- 레포지토리 생성 => 명령어 그대로 복붙
- 로컬에 있는 내 컴퓨터 폴더와 깃헙의 Remote 공간 연결
- git clone https://github.com/seopftware/django-backend-youtube
- 깃헙 데스크탑 프로그램 다운받기

### 2. Docker Hub

- 회원가입
- 나의 컴퓨터에 가상환경을 구축 (윈도우, 맥 -> 리눅스 환경 구축(MySQL, Python, Redis))
- AccessToken값을 Github 레포지토리에 등록 => 빌드목적

### 3. 장고 프로젝트 세팅

- 실제 배포 환경
- requirments.txt => 실제 배포할 때 사용
- requirments.dev.txt => 개발하고 연습할 때 사용 (파이썬 패키지 관리) DRF 버전업 해볼까?
- 실전: 패키지 의존성 관리 => 버전관리, 패키지들 간의 관계 관리

- docker-compose run --rm sh -c 'python manage.py runserver'

주말 공부

- 도커 배운 것 정리 => 나중에 배포까지 전체 프로세스를 한번 경험해보시면.

  - Redis / FastAPI

## Youtube API 개발

### 1. 모델(테이블) 구조

(1) User => O

- email
- password
- nickname
- is_bussiness: personal, business
<!-- - 구독자? 내가 구독한 사람도 있고, 나를 구독한 사람.
- 알림? -->

(2) Video => -ing

- title
- description
- link
- category
- views_count
- thumbnail
- User: FK

(3) Reaction

- User: FK
- Video: Fk
- reaction (like, dislike, cancel)

1 1 like
1 2 dislike

(5) Comment

- User: FK
- Video: FK
- content
- like
- dislike

(6) Subscription (채널 구독 관련)

- User: FK => subscriber (내가 구독한 사람)
- User: FK => subscribed_to (나를 구독한 사람)

(5) Common =>

- created_at
- updated_at

### Custom User Model Create

- TDD => 개발 및 디버깅 시간을 엄청나게 줄일 수 있습니다. PDB(Python Debugger)

# DRF 세팅

- DjangoRestframework
- drf-spectacular / swagguer-ui, redoc / requirements.txt 추가
- docker-compose build

# 슈퍼유저 만드는 방법

docker-compose run --rm app sh -c 'python manage.py createsuperuser'

# 서버실행

docker-compose up
docker-compose up --build

# 서버종료

docker-compose down

# migration
docker-compose run --rm app sh -c 'python manage.py makemigrations'
docker-compose run --rm app sh -c 'python manage.py migrate'