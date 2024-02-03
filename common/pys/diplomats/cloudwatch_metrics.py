

class MetricsDiplomat(object):

    def __init__(self, cloudwatch):
        self.cloudwatch = cloudwatch

    def safe_push_metric(self, time, ns, metric, val, unit):
        try:
            self.cloudwatch.put_metric_data(
                Namespace=ns,
                MetricData=[{
                    'MetricName': metric,
                    'Timestamp': int(time),
                    'Value': val,
                    'Unit': unit,
                }])
            print("Pushed metric to cloudwatch")
        except Exception:
            print("Failed to push metric to cloudwatch")


class MockMetricsDiplomat(object):
    def __init__(self):
        self.metrics = {}

    def safe_push_metric(self, time, ns, metric_name, val, unit):
        key = "{}/{}".format(ns, metric_name)
        self.metrics[key] = metric = self.metrics.get(key, [])
        metric.append({
            'MetricName': metric_name,
            'Timestamp': int(time),
            'Value': val,
            'Unit': unit,
        })
