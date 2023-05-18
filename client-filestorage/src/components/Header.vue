<template>
  <div class="header">
    <div class="left">
      <div class="logo">
        <h1>
          <span><i class="fas fa-house"></i> /cloud</span>
        </h1>
      </div>
      <div class="search">
        <form action="" class="form-search">
          <input
            class="search-bar form-control"
            type="search"
            placeholder="Search my cloud"
          />
        </form>
      </div>
    </div>
    <div class="center">
      <div class="list-apps">
        <ul>
          <li class="app">
            <a href="#cloud"
              ><div><i class="fa-solid fa-cloud icon-app"></i></div>
              <span>cloud</span></a
            >
          </li>
          <li class="app">
            <a href="#music"
              ><div><i class="fa-solid fa-music icon-app"></i></div>
              <span>music</span></a
            >
          </li>
          <li class="app">
            <a href="#books"
              ><div><i class="fa-solid fa-book icon-app"></i></div>
              <span>books</span></a
            >
          </li>
          <li class="app">
            <a href="#video"
              ><div><i class="fa-solid fa-video icon-app"></i></div>
              <span>video</span></a
            >
          </li>
        </ul>
      </div>
    </div>
    <div class="right">
      <div class="user-info">
        <a href=""><i class="fa-solid fa-gear"></i><span></span></a>
        <a href=""><i class="fa-solid fa-circle-user"></i><span></span></a>
      </div>
    </div>
  </div>
</template>
<script setup></script>
<style scoped>
.header {
  height: 70px;
  display: flex;
}
.header .left {
  display: flex;
  align-items: center;
  justify-content: left;
  flex: 1 1 30%;
  padding-right: 20px;
}
.header .center {
  display: flex;
  flex: 0 1 30%;
  justify-content: center;
}
.header .right {
  display: flex;
  justify-content: right;
  align-items: center;
  flex: 1 1 40%;
  padding-left: 20px;
}

.logo {
  font-size: 20px;
  margin-top: 10px;
  margin-left: 20px;
}
.search {
  margin-left: 40px;
}

.search input {
  border-radius: 30px;
  box-shadow: 0 0 1px 0 white inset, 0 0 1px 0 white;
  transition: 0.2s ease;
}
.search input:focus {
  transition: 0.2s ease;
  width: 150%;
  box-shadow: none;
  outline: none;
}

.icon-app {
  font-size: 25px;
}
.list-apps ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.list-apps li {
  margin: 10px;
  display: inline-block;
}
.list-apps a {
  text-decoration: none;
  display: block;
  text-align: center;
  color: black;
}
.list-apps a:hover {
  color: var(--accent-header-color);
  text-decoration: dotted underline;
}
.list-apps span {
  font-size: 12px;
}

.user-info {
  margin-right: 20px;
  font-size: 30px;
}
.user-info a {
  color: black;
  padding: 10px;
}
.user-info a:hover {
  color: var(--accent-header-color);
}
</style>
