const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const ARTICLES = 'articles/'

export default{
  accounts:{
    login:() => HOST+ACCOUNTS+'login/',
    logout:() => HOST+ACCOUNTS+'logout/',
    signup:() => HOST+ACCOUNTS+'signup/',
    currentUserInfo:() => HOST+ACCOUNTS+'user/'
  },
  movies:{
    movies:() => HOST+MOVIES,
    movie:(moviePk) => HOST+MOVIES+`${moviePk}/`,
    createMovieComment:(moviePk) => HOST+MOVIES+`${moviePk}/`+'create_comment/',
    editMovieComment:(moviePk, commentPk) => HOST+MOVIES+`${moviePk}/`+'edit_comment/'+`${commentPk}/`,
    deleteMovieComment:(moviePk, commentPk) => HOST+MOVIES+`${moviePk}/`+'delete_comment/'+`${commentPk}/`,
    likeMovie:(moviePk) => HOST+MOVIES+`${moviePk}/`+'like_movie/',
    checkLike:(moviePk) => HOST+MOVIES+`${moviePk}/`+'check_like/',
    comments:(moviePk) => HOST+MOVIES+`${moviePk}/`+'get_comment/',
    recoMovie:() => HOST+MOVIES+'reco_movie/'
  },
  articles:{
    articles:() => HOST+ARTICLES,
    article:(articlePk) => HOST+ARTICLES+`${articlePk}/`,
    createArticle:() => HOST+ARTICLES+'create_article/',
    editArticle:(articlePk) => HOST+ARTICLES+`${articlePk}/`+'edit_article/',
    deleteArticle:(articlePk) => HOST+ARTICLES+`${articlePk}/`+'delete_article/',
    likeArticle:(articlePk) => HOST+ARTICLES+`${articlePk}/`+'like_article/',
    createArticleComment:(articlePk) => HOST+ARTICLES+`${articlePk}/`+'create_comment/',
    editArticleComment:(articlePk, commentPk)=> HOST+ARTICLES+`${articlePk}/`+'edit_comment/'+`${commentPk}/`,
    deleteArticleComment:(articlePk, commentPk) => HOST+ARTICLES+`${articlePk}/`+'delete_comment/'+`${commentPk}/`
  }
}

