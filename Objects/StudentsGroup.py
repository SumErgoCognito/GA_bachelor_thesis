class StudentsGroup:
    def __init__(self, Id, name, numberOfStudents):
        self.Id = Id
        self.Name = name
        self.NumberOfStudents = numberOfStudents
        self.CourseClasses = []

    def addClass(self, course_class):
        self.CourseClasses.append(course_class)

    def __hash__(self):
        return hash(self.Id)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (self == other)
