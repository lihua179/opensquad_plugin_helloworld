from opensquad.launcher import register
import time

# 存储一个简单的内存状态，模拟数据更新
_state = {
    "welcome_msg": "Hello from OpenSquad!",
    "last_interaction": None,
    "counter": 0
}

@register(view="HelloWorldView", metadata={"title": "Hello World", "icon": "Smile"})
def get_hello_data():
    """返回给前端展示的数据"""
    return {
        "message": _state["welcome_msg"],
        "counter": _state["counter"],
        "last_interaction": _state["last_interaction"] or "Never"
    }

@register(action="update_counter")
def handle_interaction(payload: dict):
    """处理前端按钮点击的交互逻辑"""
    _state["counter"] += 1
    _state["last_interaction"] = time.strftime("%H:%M:%S")
    _state["welcome_msg"] = f"You clicked the button! Counter is now {_state['counter']}."
    
    return {
        "ok": True,
        "new_counter": _state["counter"],
        "toast": "Counter updated successfully!"
    }
