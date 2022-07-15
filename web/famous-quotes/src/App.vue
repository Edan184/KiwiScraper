<template>

  <ul v-if="loadedAuthors">
    <author-component 
      v-for="author in authorToQuotesIter"
      :key="author"
      :author="author"
      :quotes="authorToQuotes[author]" />
  </ul>
  <div v-else>
    Loading authors...
  </div>
</template>

<script>
import AuthorComponent from './components/AuthorComponent.vue'

export default {
  components: {AuthorComponent},
  name: 'App',
  async mounted() {
    // simulate a server fetch
    setTimeout( async () =>{
      const res = await fetch('https://type.fit/api/quotes')
      this.parseQuotesData( await res.json() )
    }, 1000)
  },
  data() {
    return {
      authorToQuotes: {}
    }
  },
  computed: {
    authorToQuotesIter(){
      console.log(Object.keys(this.authorToQuotes))
      return Object.keys(this.authorToQuotes)
    },
    loadedAuthors(){
      return Object.keys(this.authorToQuotes).length > 0
    }
  }, 
  methods: {
    parseQuotesData(data){
      for(const {author, text} of data){
        
        if(!this.authorToQuotes[author]){
          this.authorToQuotes[author] = []
        }
        this.authorToQuotes[author].push(text)
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
