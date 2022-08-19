from timeit import default_timer as timer


class Compete:
    @staticmethod
    def compare_methods(compete_class: object, *args, repeat=100) -> None:
        best_time = float("inf")
        best_method = None
        methods = Compete._get_methods(compete_class)
        for method in methods:
            time = Compete._time_method(repeat, getattr(compete_class, method), *args)
            print(f"\"{method}\": {time}s (in {repeat} repetitions), average: {time/repeat}s")
            if time < best_time:
                best_time = time
                best_method = method

        print(f"\nBest method: \"{best_method}\""
              f"\nElapsed time: {best_time}ms (in {repeat} repetitions)"
              f"\nAverage time: {best_time / repeat}s")

    @staticmethod
    def estimate_method(method: object, *args, repeat=100) -> None:
        time = Compete._time_method(repeat, method, *args)
        print(f"\"{method.__name__}\": {time}s (in {repeat} repetitions)"
              f"\nAverage time: {time/repeat}")

    @staticmethod
    def _get_methods(compete_class):
        return [attr for attr in dir(compete_class)
                if callable(getattr(compete_class, attr)) and not attr.startswith("_")]

    @staticmethod
    def _time_method(repeat, method, *args):
        start = timer()
        for _ in range(repeat):
            method(*args)
        end = timer()
        return end - start
