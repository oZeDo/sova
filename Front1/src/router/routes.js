
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: 'login', component: () => import('pages/Log.vue') },
      { path: 'cuisine', component: () => import('pages/Cuisine.vue') },
      { path: 'dishes', component: () => import('pages/Dishes.vue') },
      { path: 'otzyv', component: () => import('pages/Otzyv.vue') },
      { path: 'final', component: () => import('pages/Final.vue') }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
