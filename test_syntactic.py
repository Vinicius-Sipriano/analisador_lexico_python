#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from syntacticAnalyser import parse_source
from lexicalAnalyser import LexicalAnalyser


test_code = """
int main() {
    int x;
    x = 5;
    return;
}
"""

print("Testando analisador sintático...\n")

try:
    parse_source(test_code)
except Exception as e:
    print(f"Erro: {type(e).__name__}: {e}")
