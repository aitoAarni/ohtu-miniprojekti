import unittest
from unittest.mock import Mock, ANY
from services.reference_service import ReferenceService


class TestReferenceService(unittest.TestCase):
    def test_save_reference_calls_repository_with_correct_parameters(self):
        reference_repository_mock = Mock()
        reference_mock = Mock()
        reference_service = ReferenceService(reference_repository_mock)

        reference_service.save_reference(reference_mock)

        reference_repository_mock.add_reference.assert_called_with(reference_mock)