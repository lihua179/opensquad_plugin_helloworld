# -*- coding: utf-8 -*-
import time
from opensquad.plugin_api import register, Context, Plugin

_state = {
    "message": "Hello from OpenSquad!",
    "last_interaction": None,
    "counter": 0,
}


@register(
    name="opensquad_plugin_helloworld",
    display_name="Hello World",
    author="lihua179",
    description="一个简单的 Hello World 演示插件，展示基础的 Web UI 交互。",
    version="1.0.0",
    contributes={
        "views": [
            {
                "name": "main",
                "title": "Hello World",
                "icon": "Smile",
                "data_endpoint": "/api/plugins/opensquad_plugin_helloworld/data",
            }
        ]
    },
    tags=["demo"],
)
class HelloWorldPlugin(Plugin):
    def __init__(self, context: Context):
        super().__init__(context)

    def query_data(self, params: dict) -> dict:
        return {
            "message": _state["message"],
            "counter": _state["counter"],
            "last_interaction": _state["last_interaction"] or "Never",
        }

    def handle_action(self, action: str, payload: dict) -> dict:
        if action == "update_counter":
            _state["counter"] += 1
            _state["last_interaction"] = time.strftime("%H:%M:%S")
            _state["message"] = f"You clicked! Counter: {_state['counter']}"
            return {"ok": True, "new_counter": _state["counter"]}
        return {"ok": False, "error": f"Unknown action: {action}"}
