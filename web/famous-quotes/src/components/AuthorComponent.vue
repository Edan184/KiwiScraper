<template>
<div>
    <h1>Quotes for {{author}}</h1>
    <button @click='toggleQuotesVisibility'>{{ quotesAreVisible? 'Hide' : 'Show' }}</button>
    <quotes-list v-if="quotesAreVisible" :quotes="quotes" />
</div>
</template>

<script>
import QuotesList from './QuotesList.vue'

export default{
    components: {
        QuotesList
    },
    props:['author', 'quotes'],
    data(){
        return{
            quotesAreVisible: false,
        }
    },
    methods:{
        toggleQuotesVisibility(){
            this.quotesAreVisible = !this.quotesAreVisible;
        }
    }

}
</script>
