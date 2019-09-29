<template>
  <div id="app">
    <template v-if="!$route.meta.allowAnonymous">
      <v-app id="inspire">
        <div class="app-container">
          <toolbar @toggleNavigationBar="drawer = !drawer"/>
          <navigation :toggle="drawer"/>
          <v-content>
            <breadcrumbs />
            <router-view/>
            <page-footer />
          </v-content>
        </div>
      </v-app>
    </template>
    <template v-else>
      <transition>
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </transition>
    </template>
  </div>
</template>

<script>
import Toolbar from '@/admin_components/core/Toolbar'
import Breadcrumbs from '@/admin_components/core/Breadcrumbs'
import NavigationDrawer from '@/admin_components/core/NavigationDrawer'
import PageFooter from '@/admin_components/core/PageFooter'


export default {
  name: 'App',
  data() {
    return {
      drawer: true
    }
  },
  components: {
    'toolbar': Toolbar,
    'breadcrumbs': Breadcrumbs,
    'navigation-drawer': NavigationDrawer,
    'page-footer': PageFooter
  },
  mounted(){
    debugger
  }
}
</script>

<style>
</style>
