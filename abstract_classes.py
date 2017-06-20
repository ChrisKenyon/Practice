import abc


class Person(object):
    __metaclass__ = abc.ABCMeta

    def species(self):
        """Return your species"""
        return "Homo Sapien"

    @abc.abstractmethod
    def speak(self):
        """Say what you are"""
        return

class Student(Person):
    def speak(self):
        print "I am a student"
        return

if __name__=="__main__":
    import pdb
    pdb.set_trace()
    student1 = Student()
    print student1.species()
    student1.speak()
