# Copyright 2016-2017 Capital One Services, LLC
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
from gcp_common import BaseTest, event_data


class TestAMI(BaseTest):

    def test_role_query(self):
        project_id = "mythic-tribute-232915"

        session_factory = self.replay_flight_data(
            'ami-role-query', project_id)

        policy = {
            'name': 'ami-role-query',
            'resource': 'gcp.role'
        }

        policy = self.load_policy(
            policy,
            session_factory=session_factory)

        resources = policy.run()
        self.assertEqual(len(resources), 322)
