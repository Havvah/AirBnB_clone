#!/usr/bin/python3
""""
Module for BaseModel unittest
"""
import unittest
from models.base_model import BaseModel

class TestBase(unittest.Testcase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.update_at)

    def test_save(self):
         my_model = BaseModel()

         initial_updated_at =  my_model.updated_at

         current_updated_at =  my_model.save()

         self.assertNOtEqual(initial_updated_at, current_updated_at)

    def test_dict(self):
        my_model = BaseModel()

        my_model_dict =my_model.to_dict()

        self.assertIsInstance(my_model_dict,dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model_dict.id)
        self.assertEqual(my_model_dict["created_at"], my_model_dict.created_at.isoformat)
        self.assertEqual(my_model_dict["update_at"], my_model_dict.updated_at.isoformat)

    def test_str(self):
        my_model = BaseModel()
        
        self.assertTrue(str(my_model).startswith('[BaseModel] '))

        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


    if __name__ == "__main__":
        unittest.main()
