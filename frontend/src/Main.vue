<template>
  <div id="MenuApp">
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <h2>Меню сайта</h2>
    <ul>
      <li><a href="/" >Главная</a></li>
      <li><a href="/productcategories/">Категории продуктов</a></li>
      <li><a href="/product/">Продукты</a></li>
      <li><a href="">Прочее...</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'MenuApp',
  data () {
    return {
      msg: 'Каталог товаров'
    }
  }
}

</script>

<style lang="scss">
#MenuApp {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
