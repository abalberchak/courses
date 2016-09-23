"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        # name = request.form['name']
        # description = request.form['description']
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        course = self.models['Course'].show_all_courses()
        
        return self.load_view('index.html', courses=course)

    # def show(self):




    def add(self):

        data = {
            'title' : request.form['title'],
            'description' : request.form['description']
        }

        self.models['Course'].add_course(data)
        return redirect('/')

    def remove(self, id):
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('delete.html', courses=course)

    def cancel(self):
        return redirect('/')


    def remove_confirmation(self, id):
        course = self.models['Course'].remove_course(id)
        print course
        return redirect('/')
