from common.pys.diplomats.cloudwatch_metrics import MockMetricsDiplomat
from hamcrest import assert_that, equal_to
import unittest


class MockMetricsDiplomatTests(unittest.TestCase):
    def test_push_a_metric(self):
        mmd = MockMetricsDiplomat()

        mmd.safe_push_metric(1000, "foo", "bar", 100, 'Count')

        assert_that(
            mmd.metrics,
            equal_to({
                'foo/bar': [{
                    'MetricName': 'bar',
                    'Timestamp': 1000,
                    'Value': 100,
                    'Unit': 'Count',
                }]
            }))
