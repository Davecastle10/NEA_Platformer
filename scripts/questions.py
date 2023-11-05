# all of the code in this file is mine unless otherwise stated

import pygame
import glob
import os
import json

# I learnt how to use docstrings before making this file, so everything in this file will have docstrings in it



# creating a list of the file locations of the maps


















class Question:
    """The class for a question, that supports the question itself alongside one correct and three incorrect answers
    """    
    def __init__(self, question_input, answer_correct, answer_false_1, answer_false_2, answer_false_3, question_difficulty):
        """the constructor function that takes in the questionn and the answers

        Args:
            question (string): _description_
            answer_correct (string): the correct answer
            answer_false_1 (string): an incorrrect answer
            answer_false_2 (string): an incorrrect answer
            answer_false_3 (string): an incorrrect answer
            question_difficulty (int): a rating of the difficulty of the question with 1 being the lowest difficulty level
        """        
        self.question = question_input
        self.correct_answer = answer_correct
        self.incorrect_answer_1 = answer_false_1
        self.incorrect_answer_2 = answer_false_2
        self.incorrect_answer_3 = answer_false_3
        self.question_difficulty = question_difficulty

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
    

class Question_set:
    """A class that inherits from Question, to make a an object for a set of questions, where each question is another object of the Question class
    """    
    def __init__(self, Question, desired_question_set):
        """The constructor function for the Question_set class

        Args:
            Question (Inheritance): The inheritance from the Question class
            desired_question_set (int): the index from 0 of the question json file in the Questions folder
        """        
        self.question_sets_list = []# a list that will contingt the names of the json files that the question sts are in
        self.questions_path = 'data/questions'# the path to the folder containing the question set json files
        for filename in glob.iglob(f'{self.questions_path}/*'):# adds the names of the json files to the question_sets_list list
            self.question_sets_list.append(filename)

        self.question_sets_list_index = desired_question_set# a poonter/index used to choose which question set to open

        f = open(self.question_sets_list[self.question_sets_list_index])
        self.question_set = json.load(f)

        #for i in self.question_set['question_set']:
        #    print(i["question"])

        self.question_list = []

        for i in self.question_set['question_set']:
            self.question_list.append(Question(i['question'], i['correct_answer'], i['incorrect_answer_1'], i['incorrect_answer_2'], i['incorrect_answer_3']), i['question_difficulty'])

        

    def get_question(self, question_index):
        """method that returns the question string for a question

        Args:
            question_index (int): index from  of the question that you want from the list of questions in the question set

        Returns:
            string: a string that contains the question
        """        
        return self.question_list[question_index].question




