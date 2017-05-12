from django.shortcuts import render, redirect

class APP:

    @classmethod
    def public(cls, view):
        def render_app(request):
            template = view(request)
            app = template + '.html'
            return render(request, app)
        return render_app

    @classmethod
    def entry(cls, view):
        def render_app(request):
            templates = view(request)
            if request.user.is_authenticated():
                template = templates['protected']
            else:
                template = templates['public']
            app = template + '.html'
            return render(request, app)
        return render_app

    @classmethod
    def user(cls, view):
        def render_app(request):
            if request.user.is_authenticated():
                template = view(request)
                app = template + '.html'
                return render(request, app)
            return redirect('get_home')
        return render_app

    @classmethod
    def admin(cls, view):
        def render_app(request):
            if request.user.is_superuser:
                template = view(request)
                app = template + '.html'
                return render(request, app)
            return redirect('get_home')
        return render_app
