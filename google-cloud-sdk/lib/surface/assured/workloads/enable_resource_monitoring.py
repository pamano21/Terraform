# -*- coding: utf-8 -*- #
# Copyright 2023 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to enable resource violation monitoring for a workload."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.assured import endpoint_util
from googlecloudsdk.api_lib.assured import workloads as apis
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope.base import ReleaseTrack
from googlecloudsdk.command_lib.assured import flags

_DETAILED_HELP = {
    'DESCRIPTION': 'Enable resource violation monitoring for a workload.',
    'EXAMPLES': """ \
        To enable resource violation monitoring for a workload in the
        us-central1 region, belonging to an organization with ID 123, with
        workload ID 456, run:

          $ {command} organizations/123/locations/us-central1/workloads/456
        """,
}


@base.ReleaseTracks(ReleaseTrack.GA, ReleaseTrack.BETA, ReleaseTrack.ALPHA)
class EnableResourceMonitoring(base.UpdateCommand):
  """Enables Resource Monitoring for an Assured Workloads environment."""

  detailed_help = _DETAILED_HELP

  @staticmethod
  def Args(parser):
    flags.AddEnableResourceMonitoringFlags(parser)

  def Run(self, args):
    """Run the enables resource monitoring  command."""
    workload_resource = args.CONCEPTS.workload.Parse()
    region = workload_resource.Parent().Name()
    workload = workload_resource.RelativeName()

    with endpoint_util.AssuredWorkloadsEndpointOverridesFromRegion(
        release_track=self.ReleaseTrack(), region=region
    ):
      client = apis.WorkloadsClient(release_track=self.ReleaseTrack())
      self.resource_name = workload
      return client.EnableResourceMonitoring(name=self.resource_name)
