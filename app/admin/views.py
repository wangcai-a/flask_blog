from . import admin


@admin.route('/')
def admin():
    return 'this is admin'