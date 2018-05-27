from django.test import TestCase
from trimet_stop_event_api.models import TrimetStopEvents
from rest_framework.test import APIClient, RequestsClient

class TrimetStopEventsTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class TrimetStopEventsListEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/transportation_systems_2018/trimet_stop_events/TrimetStopEvents/')
        assert response.status_code == 200
