# Copyright 2018 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from gcp_common import BaseTest


class LogProjectSinkTest(BaseTest):

    def test_query(self):
        project_id = 'test-project-232910'
        factory = self.replay_flight_data('log-projects-sink-query', project_id)
        p = self.load_policy({
            'name': 'log-projects-sink',
            'resource': 'gcp.log-projects-sink'},
            session_factory=factory)
        resource = p.run()
        self.assertEqual(len(resource), 1)

    def test_get_project_sink(self):
        project_id = 'test-project-232910'
        sink_name = "storage"
        factory = self.replay_flight_data(
            'log-projects-sink-resource', project_id)
        p = self.load_policy({'name': 'log-projects-sink', 'resource': 'gcp.log-projects-sink'},
                             session_factory=factory)
        sink = p.resource_manager.get_resource({
            "name": sink_name,
            "project_id": project_id,
        })
        self.assertEqual(sink['name'], sink_name)


class LogSinkTest(BaseTest):

    def test_query(self):
        project_id = 'test-project-232910'
        factory = self.replay_flight_data('logsink', project_id)
        p = self.load_policy({
            'name': 'logsink',
            'resource': 'gcp.logsink'},
            session_factory=factory)
        resource = p.run()
        self.assertEqual(len(resource), 2)

    def test_get_log_sink(self):
        project_id = 'test-project-232910'
        sink_name = "storage"
        factory = self.replay_flight_data(
            'log-sink-resource', project_id)
        p = self.load_policy({'name': 'logsink', 'resource': 'gcp.logsink'},
                             session_factory=factory)
        sink = p.resource_manager.get_resource({
            "name": sink_name,
            "project_id": project_id,
        })
        self.assertEqual(sink['name'], sink_name)


class LogProjectMetricsTest(BaseTest):

    def test_query(self):
        project_id = 'test-project-232910'
        factory = self.replay_flight_data('log-projects-metric-get', project_id)
        p = self.load_policy({
            'name': 'log-projects-metric',
            'resource': 'gcp.log-projects-metric'},
            session_factory=factory)
        resource = p.run()
        self.assertEqual(len(resource), 1)

    def test_get_projects_metric(self):
        project_id = 'test-project-232910'
        metric_name = "test"
        factory = self.replay_flight_data(
            'log-projects-metric-query', project_id)
        p = self.load_policy({'name': 'log-projects-metric', 'resource': 'gcp.log-projects-metric'},
                             session_factory=factory)
        metric = p.resource_manager.get_resource({
            "name": metric_name,
            "project_id": project_id,
        })
        self.assertEqual(metric['name'], metric_name)
