import logging
import os
import time
from concurrent.futures import Future, ProcessPoolExecutor

from mypy_extensions import i32

from primes.utils import get_primes, split_number

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger()


def main():
    # max workers is number of cores
    max_workers = min(32, (os.cpu_count() or 1) + 4)

    # Splits numbers range by number of cores
    workers = split_number(200000, max_workers)

    primes: list[i32] = []
    futures: list[Future] = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for start, end in workers:
            future = executor.submit(get_primes, start=start, limit=end)
            futures.append(future)

        start = time.monotonic()

        for future in futures:
            # Blocking operation.
            # Waits untill all futures are done.
            primes.extend(future.result())

        end = int((time.monotonic() - start) * 1000)

        if len(primes) > 0:
            logger.info("Last prime %d | Took %d ms", primes[-1], end)
        else:
            logger.error("No primes were calculated")
