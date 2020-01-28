<template>
  <div id="ProductApp">
    <Menu/>
    <a v-bind:href="'/product/create/'">Добавить новый товар</a>
    <ul>
      <li v-for="product in productdataa.items">
        <p>ID: {{product.id}}</p>
        <p>Наименование: {{product.name}}</p>
        <p>Артикул: {{product.vendorcode}}</p>
        <p>Описание: {{product.description}}</p>
        <p>Категории: {{product.prodcat}}</p>
        <p>Дата создания: {{product.created}}</p>
        <br>
      </li>
    </ul>
  </div>
</template>

<script>
import Menu from './Main.vue'

export default {
  name: 'ProductApp',
  data () {
    return {
      productdataa: { items: JSON.parse(productdata) }
    }
  },
  components: {
    Menu
  }

}
</script>

<style lang="scss">
#ProductApp {
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
