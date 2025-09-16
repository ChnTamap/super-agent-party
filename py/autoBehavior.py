from py.get_setting import load_settings

async def auto_behavior(behaviorType="delay", time="00:00:00",prompt=""):
    # Load settings
    settings = await load_settings()
    if behaviorType == "time":
        settings["behaviorSettings"]["behaviorList"].append(
            {
                "enabled": True,
                "trigger": {
                    "type": "time",
                    "time":{
                        "timeValue": time, 
                        "days": [] 
                    },
                    "noInput":{
                        "latency": 30, 
                    },
                    "cycle":{
                        "cycleValue": "00:00:30", 
                        "repeatNumber": 1, 
                        "isInfiniteLoop": False, 
                    }
                },
                "action": {
                    "type": "prompt",
                    "prompt": prompt, 
                    "random":{
                        "events":[""],
                        "type":"random",
                        "orderIndex":0,
                    }
                }
            }
        )
    elif behaviorType == "delay":
        settings["behaviorSettings"]["behaviorList"].append(
            {
                "enabled": True,
                "trigger": {
                    "type": "cycle",
                    "time":{
                        "timeValue": "00:00:00", 
                        "days": [] 
                    },
                    "noInput":{
                        "latency": 30, 
                    },
                    "cycle":{
                        "cycleValue": time, 
                        "repeatNumber": 1, 
                        "isInfiniteLoop": False, 
                    }
                },
                "action": {
                    "type": "prompt",
                    "prompt": prompt, 
                    "random":{
                        "events":[""],
                        "type":"random",
                        "orderIndex":0,
                    }
                }
            }
        )
    settings["behaviorSettings"]['enabled'] = True
    return settings


auto_behavior_tool = {
    "type": "function",
    "function": {
        "name": "auto_behavior",
        "description": "当用户需要你在特定时间或隔一段时间自动执行某些行为时，你可以使用这个工具。例如，你可以设置在每天的特定时间自动发送问候语，或者设置在特定时间之后自动执行某些任务。",
        "parameters": {
            "type": "object",
            "properties": {
                "behaviorType": {
                    "type": "string",
                    "description": "行为类型，可选值为time或delay；time表示在特定时间执行，例如：三点钟提醒我开会；delay表示隔一段时间执行的任务，例如：五分钟后提醒我开会",
                    "enum": ["time", "delay"],
                },
                "time": {
                    "type": "string",
                    "description": "时间，格式为HH:MM:SS，24小时制，time类型下表示在这个时间点执行，delay类型下表示隔多久时间执行",
                },
                "prompt": {
                    "type": "string",
                    "description": "任务描述，例如：请立刻提醒用户开会、请立刻向用户发送问候语",
                }
            },
            "required": ["prompt", "behaviorType", "time"],
        },
    },
}

    