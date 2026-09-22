"""Smoke tests for modern_website_builder core (stdlib-only modules).

Runnable with pytest, or directly:  python3 tests/test_smoke.py
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.engine import Block, Website
from core.state import ProjectState
from templates.registry import get_template, REGISTRY


def test_block_roundtrip():
    b = Block("hero", {"title": "Hello"})
    d = b.to_dict()
    b2 = Block.from_dict(d)
    assert b2.id == b.id and b2.type == "hero"
    assert b2.content["title"] == "Hello"


def test_website_add_remove_block():
    site = Website("Demo", "business_modern")
    b = Block("cta", {})
    site.add_block(b)
    assert len(site.blocks) == 1
    site.remove_block(b.id)
    assert len(site.blocks) == 0
    d = site.to_dict()
    assert d["name"] == "Demo" and d["template"] == "business_modern"


def test_template_registry():
    assert len(REGISTRY) >= 1
    t = get_template("business_modern")
    assert t is not None and t.name == "Modern Business"
    assert get_template("no_such_template") is None


def test_project_state_save_load():
    state = ProjectState()
    path = os.path.join(tempfile.mkdtemp(), "proj.json")
    assert state.save_project(path) is not False
    state2 = ProjectState()
    assert state2.load_project(path) is True
    assert state2.current_project["name"] == "Untitled Project"
    assert state2.load_project("/nonexistent/xyz.json") is False


if __name__ == "__main__":
    test_block_roundtrip()
    test_website_add_remove_block()
    test_template_registry()
    test_project_state_save_load()
    print("smoke test: 4 passed")
