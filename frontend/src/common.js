import Vue from 'vue'
import App from './Main.vue'
import ProductApp from './Product.vue'
import ProdCatApp from './ProductCategories.vue'

var app5 = new Vue({
  el: '#MenuApp',
  render: h => h(App)
})

var app2 = new Vue({
  el: '#ProductApp',
  render: h => h(ProductApp),
})

var app3 = new Vue({
  el: '#ProdCatApp',
  render: h => h(ProdCatApp),
})