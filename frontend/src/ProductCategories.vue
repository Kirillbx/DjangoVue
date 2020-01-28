<template>
  <div id="ProdCatApp">
    <Menu/>
    <a v-bind:href="'/productcategories/create/'">Добавить новую категорию</a>
    <ul>
      <li v-for="prodcat in prodcatdataa.items">
        <p>ID: {{prodcat.id}}</p>
        <p>Наименование: {{prodcat.name}}</p>
        <p>Дата создания: {{prodcat.created}}</p>
        <a v-bind:href="'/productcategories/?id=' + prodcat.id">Обновить категорию</a>
        <a v-bind:href="'/productcategories/?id=' + prodcat.id">Удалить категорию</a>
        <br>
      </li>
    </ul>
  </div>
</template>

<script>
import Menu from './Main.vue'

export default {
  name: 'ProdCatApp',
  data () {
    return {
      prodcatdataa: { items: JSON.parse(prodcatdata) }
    }
  },
  components: {
    Menu
  }
}

</script>

<style lang="scss">
#ProdCatApp {
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
