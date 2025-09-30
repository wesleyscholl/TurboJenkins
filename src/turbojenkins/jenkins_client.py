"""Minimal Jenkins client wrapper for POC."""
import os
from typing import List

try:
    import jenkins  # type: ignore
except Exception:  # pragma: no cover - allow tests without installing
    jenkins = None


class JenkinsClient:
    def __init__(self):
        url = os.getenv("JENKINS_URL")
        user = os.getenv("JENKINS_USER")
        token = os.getenv("JENKINS_TOKEN")
        if not (url and user and token):
            raise EnvironmentError("JENKINS_URL, JENKINS_USER, JENKINS_TOKEN must be set")
        if jenkins is None:
            raise RuntimeError("python-jenkins package not installed")
        # server may raise on bad creds/URL
        self.server = jenkins.Jenkins(url, username=user, password=token)

    def get_job_config(self, job_name: str) -> str:
        return self.server.get_job_config(job_name)

    def get_recent_build_numbers(self, job_name: str, n: int = 10) -> List[int]:
        info = self.server.get_job_info(job_name)
        builds = info.get("builds", [])[:n]
        return [b["number"] for b in builds]

    def get_avg_build_time_minutes(self, job_name: str, n: int = 10) -> float:
        nums = self.get_recent_build_numbers(job_name, n)
        if not nums:
            return 0.0
        durations = []
        for num in nums:
            try:
                b = self.server.get_build_info(job_name, num)
                durations.append(b.get("duration", 0) / 1000.0 / 60.0)
            except Exception:
                # skip builds we couldn't fetch
                continue
        return sum(durations) / len(durations) if durations else 0.0
