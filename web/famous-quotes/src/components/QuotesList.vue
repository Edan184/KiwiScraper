<template>
<ul>
    <li v-for="quote in quotes" :key="quote">{{quote}}</li>
</ul>
</template>

<script>

export default{ props:['quotes']}
</script>