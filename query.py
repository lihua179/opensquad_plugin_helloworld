# -*- coding: utf-8 -*-
"""
query.py - launcher data/action interface for opensquad_plugin_helloworld.

launcher 调用约定：
  query_data(project_root: str, params: dict) -> dict
  handle_action(project_root: str, action: str, payload: dict) -> dict
"""

import time

_state = {
    "message": "Hello from OpenSquad!",
    "last_interaction": None,
    "counter": 0,
}


def query_data(project_root: str, params: dict) -> dict:
    """返回插件当前状态，供 GenericPluginView 展示。"""
    return {
        "summary": {
            "counter": _state["counter"],
            "message": _state["message"],
            "last_interaction": _state["last_interaction"] or "Never",
        }
    }


def handle_action(project_root: str, action: str, payload: dict) -> dict:
    """处理来自前端的操作。"""
    if action == "update_counter":
        _state["counter"] += 1
        _state["last_interaction"] = time.strftime("%H:%M:%S")
        _state["message"] = f"You clicked! Counter: {_state['counter']}"
        return {"ok": True, "new_counter": _state["counter"]}
    return {"ok": False, "error": f"Unknown action: {action}"}
