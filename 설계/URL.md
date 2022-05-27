# URL

### Movies

api/v1/movies/

- 영화 전체 조회
  - ''

- 특정 영화 조회 (디테일)
  - moviePk

- 평점&한줄평 생성
  - moviePk/create_comment
- 평점&한줄평 수정
  - moviePk/edit_comment/commentPk

- 평점&한줄평 삭제
  - moviePk/delete_comment/commentPk

- 영화 좋아요
  - moviePk/like_movie

- 영화 추천
  - reco_movie


### Accounts

- 로그인/로그아웃
- 회원가입

### Article

api/v1/articles/

- 전체 글 조회
  - ''
- 특정 글 조회
  -  articlePk
- 글 생성
  -  create_article
- 글 수정
  -  articlePk/edit_article
- 글 삭제
  -  articlePk/delete_article
- 글 좋아요
  -  articlePk/like_article
- 댓글 생성
  -  articlePk/create_comment
- 댓글 수정
  -  articlePk/edit_comment/commentPk
- 댓글 삭제
  -  articlePk/delete_comment/commentPk