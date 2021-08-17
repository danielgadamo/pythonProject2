
from objects.worker import Worker
from unittest import TestCase
from unittest.mock import patch
class TestWorker(TestCase):

    # @mock.patch("objects.worker.full_name", returnvalue="yoni mosbi")

    def setUp(self):
       print("setup")
       # month=int(input("enter month"))
       self.yoni=Worker("yoni", "mosbi",1980, 3, 2, "jerusalem", "israel")
       self.dani=Worker("dani", "mosbi",'1980', 2, 3, "jerusalem", "israel")

    def tearDown(self):
        print("teardown")


    def test_full_name(self):
        self.assertTrue(self.yoni.full_name()=="yoni mosbi")
        self.assertTrue(self.dani.full_name() == "dani mosbi")

    def test_age(self):
        age=input("enter some age")
        self.assertIn(age,self.yoni.age())


    def test_days_to_birthday(self):
      days=input("enter days to birth")
      days1 = input("enter days to birth")
      dani = Worker("dani", "mosbi", '1980', 5, 3, "jerusalem", "israel")
      self.assertIn(days,self.yoni.days_to_birthday())
      self.assertIn(days1,dani.days_to_birthday())
    def test_greet(self):

       self.assertIn('hello', self.yoni.greet(self.dani))

    def test_location(self):
        with patch("worker.requests.get")as mocked_get:

         mocked_get.assert_called_with(f'https://geocode.xyz/?locate=2jerusalem,israel&json=1')
         mocked_get.return_value.ok =True
         mocked_get.return_value.text = "success"
         res=self.yoni.location()
         self.assertEqual(res, "success")

         mocked_get.return_value.ok = False
         res = self.yoni.location()
         self.assertEqual(res, "Bad response!")