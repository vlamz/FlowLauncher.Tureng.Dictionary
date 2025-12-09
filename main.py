# -*- coding: utf-8 -*-
"""
Tureng Dictionary in Flowlauncher.

This plugin allows searching words in Tureng dictionary and opening results in browser.
"""

import os
import sys
import json

try:
    # add plugin to local PATH
    parent_folder_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(parent_folder_path)
    sys.path.append(os.path.join(parent_folder_path, 'lib'))
    sys.path.append(os.path.join(parent_folder_path, 'plugin'))

    from plugin.Tureng import TurengSearch

    if __name__ == "__main__":
        TurengSearch()
except Exception as e:
    # Handle import or initialization errors
    # Return empty result with error message in FlowLauncher JSON-RPC format
    error_response = {
        "result": [],
        "debugMessage": f"Tureng plugin initialization error: {str(e)}"
    }
    print(json.dumps(error_response))
    sys.exit(1)

