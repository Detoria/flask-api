from app.libs.redprint import Redprint

api = Redprint('book')

@api.route('/get')
def get_book():
    return 'diao ni mie'