# extensions.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import json
from py.get_setting import EXT_DIR
router = APIRouter(prefix="/api/extensions", tags=["extensions"])

class Extension(BaseModel):
    id: str
    name: str
    description: str = "无描述"
    version: str = "1.0.0"
    author: str = "未知"

class ExtensionsResponse(BaseModel):
    extensions: List[Extension]

@router.get("/list", response_model=ExtensionsResponse)
async def list_extensions():
    """获取所有可用的扩展列表"""
    try:
        extensions_dir = EXT_DIR
        
        # 确保扩展目录存在
        if not os.path.exists(extensions_dir):
            os.makedirs(extensions_dir, exist_ok=True)
            return ExtensionsResponse(extensions=[])
        
        # 读取扩展目录
        extensions = []
        for dir_name in os.listdir(extensions_dir):
            dir_path = os.path.join(extensions_dir, dir_name)
            if os.path.isdir(dir_path):
                ext_id = dir_name
                index_path = os.path.join(dir_path, "index.html")
                
                # 检查index.html是否存在
                if os.path.exists(index_path):
                    # 尝试读取扩展的package.json获取元数据
                    package_path = os.path.join(dir_path, "package.json")
                    if os.path.exists(package_path):
                        try:
                            with open(package_path, 'r', encoding='utf-8') as f:
                                package_data = json.load(f)
                                
                            extensions.append(Extension(
                                id=ext_id,
                                name=package_data.get("name", ext_id),
                                description=package_data.get("description", "无描述"),
                                version=package_data.get("version", "1.0.0"),
                                author=package_data.get("author", "未知"),
                                systemPrompt = package_data.get("systemPrompt", ""),
                            ))
                        except json.JSONDecodeError:
                            # package.json解析失败，使用默认值
                            extensions.append(Extension(
                                id=ext_id,
                                name=ext_id
                            ))
                    else:
                        # 没有package.json，使用默认值
                        extensions.append(Extension(
                            id=ext_id,
                            name=ext_id
                        ))
        
        return ExtensionsResponse(extensions=extensions)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取扩展列表失败: {str(e)}")
