# README_FRONT 🖥️

⚠️ - 오류 / 💫 - 새로운 기능

### ⚠️ ~ is not a function

- script 태그 안에서 methods를 method로 써서 생긴 오류

### ⚠️ headers? header?

- store에서 headers를 header라고 써서 인증 오류가🥲

#### ➡️ 휴먼에러를 조심하자

### 💫 fontawesome 라이브러리

1. 라이브러리 설치

   ```
   $ npm i --save @fortawesome/fontawesome-svg-core
   $ npm i --save @fortawesome/free-solid-svg-icons
   $ npm i --save @fortawesome/free-regular-svg-icons
   ```

2. main.js에 등록

   ```
   import { library } from '@fortawesome/fontawesome-svg-core'
   import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
   Vue.component("font-awesome-icon", FontAwesomeIcon);
   
   ```

3. main.js에 사용할 아이콘 등록

   ```
   import { faHeart, faStar } from '@fortawesome/free-solid-svg-icons'
   library.add( faHeart, faStar, farHeart )
   ```

4. HTML에서 사용

   ```
   <font-awesome-icon icon="fa-solid fa-heart"></font-awesome-icon>
   ```

5. 한 아이콘의 solid와 regular 모두 사용하고 싶을 때, 이름이 동일해서 오류 발생할 경우

   ```
   import { faHeart as farHeart } from '@fortawesome/free-regular-svg-icons'
   ```

   ✏️ solid와 regular 중 하나를 as ㅇㅇㅇ을 통해 새로운 이름으로 가져온 후 library에 추가

### 💫 Vue Carousel

- Vue bootstrap carousel로 시작했으나 화면 꽉차게 너비 조정 실패, 슬라이드가 넘어갈 때 이미지 크기가 커지는 등의 해결할 수 없는 문제 발생
- Vue Carousel 라이브러리로 대체

1. Vue Carousel 라이브러리 설치

   ```
   npm install -S vue-carousel
   ```

2. main.js에 등록

   ```
   import VueCarousel from 'vue-carousel';
   Vue.use(VueCarousel);
   ```

3. html에서 사용

   ```
   <carousel>
   	<slide></slide>
   </carousel>
   ```

4. 슬라이드 하나씩 띄우기

   ```
   <carousel :perPage="1">
   ```

5. 슬라이드 자동으로 넘기기

   ```
   <carousel v-bind:autoplay="true" v-bind:loop="true">
   ```

### 💫 Pagination

- Vue Bootstrap의 pagination 컴포넌트 사용

  ```
  <b-pagination
        class="moviePaging"
        v-model="currentPage"
        pills
        :total-rows="rows"
        :per-page="perPage"
      ></b-pagination>
  ```

  ```
  data(){
  	return{
  		perPage:8,
        	currentPage:1
  	}
  },
  computed:{
  	Movies(){
        	const movies = this.$store.getters.movies
        	return movies.slice(
          	(this.currentPage -1)*this.perPage,
          	this.currentPage*this.perPage
        )
      },
  }
  ```

### 💫 모달에서 좋아요 비동기 구현

- Back에서 시리얼라이저 반환
- 모달은 선택한 영화의 정보를 modalData로 보여줌 ➡️ 좋아요 눌렀을 경우 비동기로 구현 불가능

#### ⚒️ 그래서...

- checkLike 생성 ➡️ 영화를 선택하여 모달이 열렸을 때 영화를 좋아요 한 적 있는지 유무에 따라 아이콘을 다르게 보여줌
- Back에서 isLike로 True나 False 반환하는 것으로 수정 ➡️ 좋아요 눌렀을 때 비동기로 반응 가능

### ⚠️ currentUser를 찾을 수 없습니다

- fetchCurrentUser()를 실행하지 않아서 발생
- created()로 페이지 열면 fetchCurrentUser 실행, ...mapGetters(['currentUser'])로 currentUser 불러와서 해결

### 💫 영화 별점 입력

- Vue Bootstrap의 b-form-rating 사용

  ```
  <b-form-rating class="starRating" v-model="score" variant="warning" show-value show-value-max size="lg" no-border></b-form-rating>
  ```

### ⚠️ 영화 리뷰 수정 불가능

- 영화 리뷰의 스코어 데이터를 넘겨주지 않아 발생
- Vue에서 영화 스코어를 함께 넘겨주어 해결
