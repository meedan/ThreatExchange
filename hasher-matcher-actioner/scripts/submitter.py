#! /usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

import os
import time
import threading
import uuid
import datetime
import typing as t
from submit_content_test import DeployedInstanceTestHelper


class Submitter(threading.Thread):
    def __init__(
        self,
        helper: DeployedInstanceTestHelper,
        batch_size: int,
        seconds_between_batches: int,
        filepaths: t.List[str] = [],
        **kwargs,
    ):
        super(Submitter, self).__init__(**kwargs)
        self.daemon = True
        self._stop_signal = threading.Event()
        self._lock = threading.Lock()
        self.helper = helper
        self.batch_size = batch_size
        self.seconds_between_batches = seconds_between_batches
        self.filepaths = filepaths
        self.total_submitted = 0

    def stop(self):
        self._stop_signal.set()

    def stopped(self):
        return self._stop_signal.is_set()

    def run(self):
        while not self.stopped() and self._lock.acquire():
            if self.stopped():
                self._lock.release()
                return
            try:
                batch_prefix = f"soak-test-{str(uuid.uuid4())}"
                for i in range(self.batch_size):
                    content_id = f"{batch_prefix}{i}-time-{datetime.datetime.now().isoformat()}-time-"
                    if self.filepaths:
                        self.helper.submit_test_content(
                            content_id, filepath=self.filepaths[i % len(self.filepaths)]
                        )
                    else:
                        self.helper.submit_test_content(content_id)
                    self.total_submitted += 1
            finally:
                self._lock.release()
            time.sleep(self.seconds_between_batches)
            self.helper.refresh_api_token()

    def get_total_submit_count(self) -> int:
        with self._lock:
            return self.total_submitted

    def get_current_values(self) -> t.Tuple[int, int, int]:
        with self._lock:
            return (self.batch_size, self.seconds_between_batches, self.total_submitted)

    def set_batch_size(self, batch_size: int):
        with self._lock:
            self.batch_size = batch_size

    def set_seconds_between_batches(self, seconds_between_batches: int):
        with self._lock:
            self.seconds_between_batches = seconds_between_batches


if __name__ == "__main__":

    API_URL = ""
    REFRESH_TOKEN = ""
    CLIENT_ID = ""

    api_url = os.environ.get(
        "HMA_API_URL",
        API_URL,
    )
    refresh_token = os.environ.get(
        "HMA_REFRESH_TOKEN",
        REFRESH_TOKEN,
    )
    client_id = os.environ.get(
        "HMA_COGNITO_USER_POOL_CLIENT_ID",
        CLIENT_ID,
    )
    helper = DeployedInstanceTestHelper(api_url, "", client_id, refresh_token)

    submitter = Submitter(helper, batch_size=5, seconds_between_batches=5)
    submitter.start()

    cmd = ""
    while cmd != "q":
        cmd = input("Enter 'q' to shutdown: ")

    submitter.stop()
