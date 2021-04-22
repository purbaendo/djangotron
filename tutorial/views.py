from django.shortcuts import render
from .models import Page, Post

def index(request):
    html_posts = Post.objects.filter(category='html')
    css_posts = Post.objects.filter(category='css')
    bootstrap_posts = Post.objects.filter(category='bootstrap')
    sass_posts = Post.objects.filter(category='sass')
    flexbox_posts = Post.objects.filter(category='flexbox')
    javascript_posts = Post.objects.filter(category='javascript')
    jquery_posts = Post.objects.filter(category='jquery')
    ajax_posts = Post.objects.filter(category='ajax')
    json_posts = Post.objects.filter(category='json')
    react_posts = Post.objects.filter(category='react')
    angular_posts = Post.objects.filter(category='angular')
    nodejs_posts = Post.objects.filter(category='nodejs')
    vuejs_posts = Post.objects.filter(category='vuejs')
    graphql_posts = Post.objects.filter(category='graphql')
    php_posts = Post.objects.filter(category='php')
    laravel_posts = Post.objects.filter(category='laravel')
    codeigniter_posts = Post.objects.filter(category='codeigniter')
    asp_posts = Post.objects.filter(category='asp')
    python_posts = Post.objects.filter(category='python')
    django_posts = Post.objects.filter(category='django')
    flask_posts = Post.objects.filter(category='flask')
    numpy_posts = Post.objects.filter(category='numpy')
    scipy_posts = Post.objects.filter(category='scipy')
    pandas_posts = Post.objects.filter(category='pandas')
    matplotlib_posts = Post.objects.filter(category='matplotlib')
    tensorflow_posts = Post.objects.filter(category='tensorflow')
    pytorch_posts = Post.objects.filter(category='pytorch')
    scikitlearn_posts = Post.objects.filter(category='scikitlearn')
    keras_posts = Post.objects.filter(category='keras')
    opencv_posts = Post.objects.filter(category='opencv')
    tkinter_posts = Post.objects.filter(category='tkinter')
    qt_posts = Post.objects.filter(category='qt')
    pygame_posts = Post.objects.filter(category='pygame')
    kivy_posts = Post.objects.filter(category='kivy')
    sql_posts = Post.objects.filter(category='sql')
    mysql_posts = Post.objects.filter(category='mysql')
    postgresql_posts = Post.objects.filter(category='postgresql')
    java_posts = Post.objects.filter(category='java')
    git_posts = Post.objects.filter(category='git')
    android_posts = Post.objects.filter(category='android')
    ios_posts = Post.objects.filter(category='ios')

    context = {
        'html_counter' : html_posts.count(),
        'css_counter' : css_posts.count(),
        'bootstrap_counter' : bootstrap_posts.count(),
        'sass_counter' : sass_posts.count(),
        'flexbox_counter' : flexbox_posts.count(),
        'javascript_counter' : javascript_posts.count(),
        'jquery_counter' : jquery_posts.count(),
        'ajax_counter' : ajax_posts.count(),
        'json_counter' : json_posts.count(),
        'react_counter' : react_posts.count(),
        'angular_counter' : angular_posts.count(),
        'nodejs_counter' : nodejs_posts.count(),
        'vuejs_counter' : vuejs_posts.count(),
        'graphql_counter' : graphql_posts.count(),
        'php_counter' : php_posts.count(),
        'laravel_counter' : laravel_posts.count(),
        'codeigniter_counter' : codeigniter_posts.count(),
        'asp_counter' : asp_posts.count(),
        'python_counter' : python_posts.count(),
        'django_counter' : django_posts.count(),
        'flask_counter' : flask_posts.count(),
        'numpy_counter' : numpy_posts.count(),
        'scipy_counter' : scipy_posts.count(),
        'pandas_counter' : pandas_posts.count(),
        'matplotlib_counter' : matplotlib_posts.count(),
        'tensorflow_counter' : tensorflow_posts.count(),
        'pytorch_counter' : pytorch_posts.count(),
        'scikitlearn_counter' : scikitlearn_posts.count(),
        'keras_counter' : keras_posts.count(),
        'opencv_counter' : opencv_posts.count(),
        'tkinter_counter' : tkinter_posts.count(),
        'qt_counter' : qt_posts.count(),
        'pygame_counter' : pygame_posts.count(),
        'kivy_counter' : kivy_posts.count(),
        'sql_counter' : sql_posts.count(),
        'mysql_counter' : mysql_posts.count(),
        'postgresql_counter' : postgresql_posts.count(),
        'java_counter' : java_posts.count(),
        'git_counter' : git_posts.count(),
        'android_counter' : android_posts.count(),
        'ios_counter' : ios_posts.count(),
        'page':'html',
    }
    return render(request, 'index.html', context)

def topic(request, pagename):

    if pagename == 'editor':
        return render(request, 'tutorial/editor.html')
    elif pagename == '/':
        return render(request, 'index.html')
    else:
        context = {
            'content_list':Post.objects.filter(category=pagename),
            'first':Post.objects.filter(category=pagename).first(),
            'topic':Page.objects.get(permalink=pagename),
        }
        return render(request, 'topic.html', context)

def post_detail(request, pagename, title_post):
    context = {
        'content_list':Post.objects.filter(category=pagename),
        'article':Post.objects.get(slug=title_post),
    }
    return render(request, 'witheditor.html', context)


def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "400.html", {})