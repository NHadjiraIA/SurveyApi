class QuestionResponseUser(object):
    def __init__(self, id_question=None, id_response=None, id_user=None, date_reponse=None,hour_response=None):
        self.id_question= id_question
        self.id_response = id_response
        self.id_user = id_user
        self.date_reponse = date_reponse
        self.hour_response = hour_response