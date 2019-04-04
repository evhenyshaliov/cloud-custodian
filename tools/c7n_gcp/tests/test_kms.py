# Copyright 2019 Capital One Services, LLC
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


class KmsLocationTest(BaseTest):
    def test_kms_location_query(self):
        project_id = 'mitraject'
        session_factory = self.replay_flight_data('kms-location-query', project_id=project_id)

        policy = {
            'name': 'all-kms-locations',
            'resource': 'gcp.kms-location'
        }

        policy = self.load_policy(
            policy,
            session_factory=session_factory)

        resources = policy.run()
        self.assertEqual(len(resources), 25)

    def test_kms_location_get(self):
        project_id = 'mitraject'
        session_factory = self.replay_flight_data('kms-location-get', project_id=project_id)

        policy = {
            'name': 'one-kms-location',
            'resource': 'gcp.kms-location'
        }

        policy = self.load_policy(
            policy,
            session_factory=session_factory)

        location = policy.resource_manager.get_resource(
            {'name': 'projects/mitraject/locations/asia'})

        self.assertEqual(
            location['labels']['cloud.googleapis.com/location'],
            'asia'
        )
