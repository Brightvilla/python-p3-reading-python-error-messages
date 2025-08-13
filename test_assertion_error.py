#!/usr/bin/env python3

import subprocess
import sys

def test_assertion_passes():
    """Test that the assertion in an_assertion_error.py passes"""
    result = subprocess.run([sys.executable, 'lib/an_assertion_error.py'], 
                          capture_output=True, text=True)
    assert result.returncode == 0
    assert "Assertion passed!" in result.stdout