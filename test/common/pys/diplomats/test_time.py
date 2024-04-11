import common.pys.diplomats.time as sut
import hamcrest as h
import unittest
import time


class TestTime(unittest.TestCase):

    def test_getting_time(self):
        t = sut.Time()
        h.assert_that(
            t.now(),
            h.is_(float)
        )

    def test_continuance(self):
        t = sut.Time()
        t1 = t.now()
        time.sleep(0.001)
        t2 = t.now()

        h.assert_that(
            t2,
            h.greater_than(t1)
        )

    def test_simple_timer(self):
        t = sut.Time()

        start = t.start_timer("foo")
        time.sleep(1.4)
        elapsed = t.stop_timer("foo")
        stop = t.now()

        h.assert_that(
            elapsed,
            h.greater_than_or_equal_to(1.4)
        )
        h.assert_that(
            stop - start - elapsed,
            h.close_to(0, 0.1)
        )

    def test_cannot_stop_unstarted_timer(self):
        t = sut.Time()

        h.assert_that(
            h.calling(t.stop_timer).with_args("foo"),
            h.raises(ValueError)
        )

    def test_cannot_stop_twice(self):
        t = sut.Time()

        t.start_timer("foo")
        t.stop_timer("foo")
        h.assert_that(
            h.calling(t.stop_timer).with_args("foo"),
            h.raises(ValueError)
        )

    def test_mock_advance(self):
        t = sut.MockTime()
        t.set_time(10)
        t.advance(1)

        h.assert_that(
            t.time,
            h.equal_to(11)
        )

    def test_mock_advance_without_initial(self):
        realnow = time.time()
        t = sut.MockTime()
        t.advance(1)

        h.assert_that(
            t.time,
            h.greater_than_or_equal_to(realnow)
        )

    def test_timers_with_mock_time(self):
        t = sut.MockTime()

        t.set_time(1000)
        start = t.start_timer("foo")
        t.set_time(2000)
        elapsed1 = t.elapsed_timer("foo")
        t.advance(1000)
        elapsed2 = t.stop_timer("foo")

        h.assert_that(start, h.close_to(1000, 0.2))
        h.assert_that(elapsed1,  h.close_to(1000, 0.2))
        h.assert_that(elapsed2,  h.close_to(2000, 0.2))
