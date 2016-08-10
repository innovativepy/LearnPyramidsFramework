from pyramid.paster import get_app, setup_logging

ini_path = "/web/LearnPyramidsFramework/Lesson_1/serve_them/production.ini"
setup_logging(ini_path)
application = get_app(ini_path, 'main')
