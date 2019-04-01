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


class PubSubTopicTest(BaseTest):

    def test_pubsub_topic_query(self):
        project_id = 'cloud-custodian'
        pubsub_topic_name = 'projects/cloud-custodian/topics/custodian'
        session_factory = self.replay_flight_data(
            'pubsub-topic-query', project_id=project_id)

        policy = self.load_policy(
            {'name': 'gcp-pubsub-topic-dryrun',
             'resource': 'gcp.pubsub-topic'},
            session_factory=session_factory)

        pubsub_topic_resources = policy.run()
        self.assertEqual(pubsub_topic_resources[0]['name'], pubsub_topic_name)

    def test_pubsub_topic_get(self):
        project_id = 'cloud-custodian'
        pubsub_topic_name = 'projects/cloud-custodian/topics/custodian'
        session_factory = self.replay_flight_data(
            'pubsub-topic-get', project_id=project_id)

        policy = self.load_policy(
            {'name': 'gcp-pubsub-topic-dryrun',
             'resource': 'gcp.pubsub-topic'},
            session_factory=session_factory)

        pubsub_topic_resource = policy.resource_manager.get_resource(
            {'project_id': project_id, 'topic_id': pubsub_topic_name})
        self.assertEqual(pubsub_topic_resource['name'], pubsub_topic_name)

    def test_pubsub_topic_iam_policy_get(self):
        resource = 'projects/cloud-custodian/topics/custodian'
        etag = 'ACAB'
        session_factory = self.replay_flight_data(
            'pubsub-topic-iam-policy-get')

        policy = self.load_policy(
            {'name': 'pubsub-topic-iam-policy-dryrun',
             'resource': 'gcp.pubsub-topic-iam-policy'},
            session_factory=session_factory)

        pubsub_topic_iam_policy_resource = policy.resource_manager.get_resource(
            {'resource': resource})
        self.assertEqual(pubsub_topic_iam_policy_resource['etag'], etag)


class PubSubSubscriptionTest(BaseTest):

    def test_pubsub_subscription_query(self):
        project_id = 'cloud-custodian'
        pubsub_subscription_name = 'projects/cloud-custodian/subscriptions/custodian'
        session_factory = self.replay_flight_data(
            'pubsub-subscription-query', project_id=project_id)

        policy = self.load_policy(
            {'name': 'gcp-pubsub-subscription-dryrun',
             'resource': 'gcp.pubsub-subscription'},
            session_factory=session_factory)

        pubsub_subscription_resources = policy.run()
        self.assertEqual(pubsub_subscription_resources[0]['name'], pubsub_subscription_name)

    def test_pubsub_subscription_get(self):
        project_id = 'cloud-custodian'
        pubsub_subscription_name = 'projects/cloud-custodian/subscriptions/custodian'
        session_factory = self.replay_flight_data(
            'pubsub-subscription-get', project_id=project_id)

        policy = self.load_policy(
            {'name': 'gcp-pubsub-subscription-dryrun',
             'resource': 'gcp.pubsub-subscription'},
            session_factory=session_factory)

        pubsub_subscription_resource = policy.resource_manager.get_resource(
            {'project_id': project_id, 'name': pubsub_subscription_name})
        self.assertEqual(pubsub_subscription_resource['name'], pubsub_subscription_name)

    def test_pubsub_subscription_iam_policy_get(self):
        resource = 'projects/cloud-custodian/subscriptions/custodian'
        etag = 'ACAB'
        session_factory = self.replay_flight_data(
            'pubsub-subscription-iam-policy-get')

        policy = self.load_policy(
            {'name': 'pubsub-subscription-iam-policy-dryrun',
             'resource': 'gcp.pubsub-subscription-iam-policy'},
            session_factory=session_factory)

        pubsub_subscription_iam_policy_resource = policy.resource_manager.get_resource(
            {'resource': resource})
        self.assertEqual(pubsub_subscription_iam_policy_resource['etag'], etag)


class PubSubSnapshotTest(BaseTest):

    def test_pubsub_snapshot_query(self):
        project_id = 'cloud-custodian'
        pubsub_snapshot_name = 'projects/cloud-custodian/snapshots/custodian'
        session_factory = self.replay_flight_data(
            'pubsub-snapshot-query', project_id=project_id)

        policy = self.load_policy(
            {'name': 'gcp-pubsub-snapshot-dryrun',
             'resource': 'gcp.pubsub-snapshot'},
            session_factory=session_factory)

        pubsub_snapshot_resources = policy.run()
        self.assertEqual(pubsub_snapshot_resources[0]['name'], pubsub_snapshot_name)

    def test_pubsub_subscription_iam_policy_get(self):
        resource = 'projects/cloud-custodian/snapshots/custodian'
        etag = 'ACAB'
        session_factory = self.replay_flight_data(
            'pubsub-snapshot-iam-policy-get')

        policy = self.load_policy(
            {'name': 'pubsub-snapshot-iam-policy-dryrun',
             'resource': 'gcp.pubsub-snapshot-iam-policy'},
            session_factory=session_factory)

        pubsub_snapshot_iam_policy_resource = policy.resource_manager.get_resource(
            {'resource': resource})
        self.assertEqual(pubsub_snapshot_iam_policy_resource['etag'], etag)
