# all of the code in this file is mine unless otherwise stated

import pygame

# I learnt how to use docstrings before makig this file, so everything in this file will have docstrings in it

class Question:
    """The class for a question, that supports the question itself alongside one correct and three incorrect answers
    """    
    def __init__(self, question_input, answer_correct, answer_false_1, answer_false_2, answer_false_3):
        """the constructor function that takes in the questionn and the answers

        Args:
            question (string): _description_
            answer_correct (string): the correct answer
            answer_false_1 (string): an incorrrect answer
            answer_false_2 (string): an incorrrect answer
            answer_false_3 (string): an incorrrect answer
        """        
        self.question = question_input
        self.correct_answer = answer_correct
        self.incorrect_answer_1 = answer_false_1
        self.incorrect_answer_2 = answer_false_2
        self.incorrect_answer_3 = answer_false_3

    def answer_attempt(self, selected_answer):
        """takes the the string of the answer chosen and return True if the answer is correct 
        and Flase if the answer is incorrect

        Args:
            selected_answer (string): the answer the player selected

        Returns:
            Bool: True if the answer is correct and False if the answer is incorrect
        """        
        if selected_answer == self.correct_answer:
            return True
            
        else:
            return False
        

    def give_correct_answer(self):
        """Returns the correct answer for the question

        Returns:
            string: the correct answer
        """        
        return self.correct_answer