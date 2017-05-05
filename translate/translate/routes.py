def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('html', 'html', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('chameleon', '/chameleon')
    config.add_route('login', '/login')
    config.add_route('register', '/register')
