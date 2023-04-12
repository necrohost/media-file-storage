<template>
    <header>
        <input type="text" value="search" class="search-bar">
        <input type="button" value="upgrade">
        <i class="fas fa-bell"></i>
        <div>image</div>
    </header>
</template>

<script>
export default {
    name: "Header"
}
</script>

<style scoped>
header {
    margin: 10px;
    display: flex;
    height: 50px;
}
.search-bar {
    width: 50%;
}
</style>