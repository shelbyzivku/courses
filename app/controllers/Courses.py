from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        print self.models['Course'].get_courses()
        if not 'counter' in session:
            session['counter'] = 0
        return self.load_view('index.html')

    def process(self):

        session['counter'] += 1

        data = {
            'course_name': request.form['course_name'],
            'course_des': request.form['course_des'],
        }


        self.models['Course'].add_course(data)
     
        return redirect('/result')

    def result(self):
        data = self.models['Course'].get_courses()
        return self.load_view('result.html', courses=data, counter=session['counter'])
