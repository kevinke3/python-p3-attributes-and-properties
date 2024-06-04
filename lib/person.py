#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name):
        self.name = name
        self.job = ''
    
    def get_job(self):
        return self.job

   
    def set_job(self, job):
        if (job in APPROVED_JOBS):
            self.job = job.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def get_name(self):
        return self._name

    
    def set_name(self, value):
        if not isinstance(value, str) or len(value) > 25:
            print("Name must be a string under 25 characters.")
            return
        self._name = value.title()