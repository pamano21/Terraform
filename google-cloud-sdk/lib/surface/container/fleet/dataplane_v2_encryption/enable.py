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
"""The command to enable Dataplane V2 Encryption Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.command_lib.container.fleet.features import base


class Enable(base.EnableCommand):
  """Enables the Dataplane V2 Encryption Feature.

  This command enables the Dataplane V2 Encryption Feature in a fleet.

  ## EXAMPLES

  To enable the Dataplane V2 Encryption Feature, run:

    $ {command}
  """

  feature_name = 'dataplanev2'

  def Run(self, args):
    """Runs the command. No args."""
    f = self.messages.Feature(
        spec=self.messages.CommonFeatureSpec(
            dataplanev2=self.messages.DataplaneV2FeatureSpec(
                enableEncryption=True
            )
        )
    )
    self.Enable(f)
