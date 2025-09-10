![image](static/source/agent_party.png)

<div align="center">
  <a href="./README_ZH.md">简体中文</a> |
  <a href="./README.md">English</a>
</div>

####

<div align="center">
  <a href="https://space.bilibili.com/26978344">B站</a> ·
  <a href="https://www.youtube.com/@LLM-party">youtube</a> ·
  <a href="https://gcnij7egmcww.feishu.cn/wiki/DPRKwdetCiYBhPkPpXWcugujnRc">中文文档</a> ·
  <a href="https://temporal-lantern-7e8.notion.site/super-agent-party-211b2b2cb6f180c899d1c27a98c4965d">English doc</a> ·
  <a href="https://pan.baidu.com/share/init?surl=VBSnq4Ga3fRX_NcyPwsV7Q&pwd=2333">网盘下载</a> · 
  <a href="#quick-start">Quick Start</a>
</div>

## Introduction

### 🚀 **A 3D AI desktop companion with endless possibilities!**  

- ✅ Seamless capability enhancement: It is possible to achieve an enterprise-level upgrade of the LLM API without code modification, seamlessly integrating knowledge bases, real-time networking, permanent memory, compatible SillyTavern Character Card, code execution, multimodal capabilities (vision/drawing/audition/speech), Automation capabilities (controlling smart homes, controlling browsers), deep thinking control and research, and other modular functions into the existing model interface, creating a pluggable LLM enhancement platform.

- ✅ One-click deployment across all channels: It supports the rapid deployment of intelligent agents to multiple types of terminals, and is compatible with scenarios such as classic chat interfaces, QQ official robots, Bilibili live interaction, and VRM virtual desktop pets, ready to use out of the box.

- ✅ Ecological tool interconnection: It can freely access third-party intelligent entities and workflows as a tool chain (already adapted to systems such as Dify/ComfyUI/MCP/A2A), and achieve cross-platform capability aggregation through the agent-party architecture.

- ✅ Standardized interface opening: Provide OpenAI API-compatible interfaces and MCP protocol support, making it easy for developers to directly connect to external systems and achieve rapid transfer and secondary development of the agent's capabilities.

- ✅ Compatible and adaptable across all platforms: It covers the native running environments of Windows/macOS/Linux, supports Docker containerized deployment and web-based cloud services, and meets the needs of multi-scene technology stacks.

## Quick Start

### Cloud disk download

  👉 [Click Baidu Cloud to download](https://pan.baidu.com/share/init?surl=VBSnq4Ga3fRX_NcyPwsV7Q&pwd=2333)
  
  👉 [Click Google Cloud to download](https://drive.google.com/drive/folders/1xu8U1FCIZ5iqWpmf1w3TLX8AqGWft3zg?usp=sharing)

### Windows portable package (Recommended! Installation-free source version, support one-click synchronization to the latest version of the warehouse, no need to wait for the desktop version to be packaged)

  👉 [Click to download](https://github.com/heshengtao/super-agent-party/releases/download/v0.2.8/super-agent-party-v0.2.8.zip)

⭐Attention! You can double-click `一键更新(update).bat` to update the software, or you can double-click `一键启动(start).bat` to start the software.

### Windows Desktop Installation

  👉 [Click to download](https://github.com/heshengtao/super-agent-party/releases/download/v0.2.8/Super-Agent-Party-Setup-0.2.8.exe)

⭐ Note! Choose to install only for the current user during installation, otherwise, administrator privileges will be required to start.

### MacOS Desktop Installation (Currently only M chips are supported.)

  👉 [Click to download](https://github.com/heshengtao/super-agent-party/releases/download/v0.2.8/Super-Agent-Party-0.2.8-Mac.dmg)

⭐Attention! After downloading, drag the app file of the dmg file into the `/Applications` directory, then open end point, execute the following command and enter the root password to remove the attached Quarantine attribute from the network download:

  ```shell
  sudo xattr -dr com.apple.quarantine /Applications/Super-Agent-Party.app
  ```

### Linux Desktop Installation

We provide two mainstream Linux installation package formats for your convenience in different scenarios.

#### 1. Install using `.AppImage`

`.AppImage` is a Linux application format that does not require installation and can be used immediately. Suitable for most Linux distributions.

  👉 [Click to download](https://github.com/heshengtao/super-agent-party/releases/download/v0.2.8/Super-Agent-Party-0.2.8-Linux.AppImage)

#### 2. Install using `.deb` package (Suitable for Ubuntu/Debian systems)

  👉 [Click to download](https://github.com/heshengtao/super-agent-party/releases/download/v0.2.8/Super-Agent-Party-0.2.8-Linux.deb)

### Docker Deployment (This version of the table pet can only be viewed through the browser.)

- Two commands to install this project:
  ```shell
  docker pull ailm32442/super-agent-party:latest
  docker run -d -p 3456:3456 -v ./super-agent-data:/app/data ailm32442/super-agent-party:latest
  ```

- ⭐Note! `./super-agent-data` can be replaced with any local folder, after Docker starts, all data will be cached in this local folder and will not be uploaded anywhere.

- Plug and play: access http://localhost:3456/

### Source Code Deployment

- Windows:
  ```shell
  git clone https://github.com/heshengtao/super-agent-party.git
  cd super-agent-party
  uv sync
  npm install
  start_with_dev.bat
  ```

- Linux or Mac:
  ```shell
  git clone https://github.com/heshengtao/super-agent-party.git
  cd super-agent-party
  uv sync
  npm install
  chmod +x start_with_dev.sh
  ./start_with_dev.sh
  ```

## Software Screenshots

### Multi-Service Provider Support: Supports both locally deployed engines (e.g., Ollama, Dify) and cloud service provider APIs.
![image](doc/image/model1.jpeg)

### Extensive Tool Integration: Built-in various tools (e.g., knowledge base, web search, smart home control, browser automation), supporting asynchronous invocation without blocking agent responses.
![image](doc/image/HA2.jpeg)

### VRM Desktop Pet: Supports uploading custom VRM models to create a personalized desktop companion.
![image](doc/image/vrmbot3.jpeg)

### Tavern Character Cards: Supports Tavern character cards with long-term memory capabilities.
![image](doc/image/card4.jpeg)

### QQ Bot: Supports one-click deployment to the official QQ bot platform, enabling users to access the agent anytime, anywhere.
![image](doc/image/qqbot6.jpeg)

### Developer-Friendly: Provides open OpenAI API and MCP interfaces, allowing the agent to be exposed externally.
![image](doc/image/API7.jpeg)

### ComfyUI Integration: Converts ComfyUI workflows into agent tools with load balancing across multiple ComfyUI servers.
![image](doc/image/comfyui8.jpeg)

## Hardware requirements

- CPU: 2 cores or more
- Memory: 2GB or more

**Because all models are optional, you can access the local deployment engine, or you can all use the Cloud as a Service provider interface, so there are few hardware requirements. Test the docker version on the 2-core 2G Cloud as a Service server and it will work fine**

## Usage

- Desktop: Click the desktop icon to use immediately.

- Web or docker: Access http://localhost:3456/ after startup.

- API call: Developer-friendly, perfectly compatible with OpenAI format, can output in real-time, and does not affect the original API's response speed. No need to modify the calling code:

  ```python
  from openai import OpenAI
  client = OpenAI(
    api_key="super-secret-key",
    base_url="http://localhost:3456/v1"
  )
  response = client.chat.completions.create(
    model="super-model",
    messages=[
        {"role": "user", "content": "What is Super Agent Party?"}
    ]
  )
  print(response.choices[0].message.content)
  ```

- MCP call: After starting, you can invoke the local MCP service by writing the following content in the configuration file:

  ```json
  {
    "mcpServers": {
      "super-agent-party": {
        "url": "http://127.0.0.1:3456/mcp",
      }
    }
  }
  ```

## Features

Please refer to the following document for the main functions:
  - 👉 [Chinese document](https://gcnij7egmcww.feishu.cn/wiki/DPRKwdetCiYBhPkPpXWcugujnRc)
  - 👉 [English document](https://temporal-lantern-7e8.notion.site/super-agent-party-211b2b2cb6f180c899d1c27a98c4965d)

## Disclaimer:
This open-source project and its content (hereinafter referred to as the "project") are for reference only and do not imply any explicit or implicit warranties. The project contributors do not assume any responsibility for the completeness, accuracy, reliability, or applicability of the project. Any behavior that relies on the project content shall be at the user's own risk. In any case, the project contributors shall not be liable for any indirect, special, or incidental losses or damages arising from the use of the project content.

## License Agreement

This project uses a dual licensing model:
1. By default, this project follows the **GNU Affero General Public License v3.0 (AGPLv3)** license agreement
2. If you need to use this project for closed-source commercial purposes, you must obtain a commercial license from the project administrator. Business cooperation: hst97@qq.com

Using this project for closed-source commercial purposes without written authorization is considered a violation of this agreement. The complete text of AGPLv3 can be found in the LICENSE file in the project root directory or at [gnu.org/licenses](https://www.gnu.org/licenses/agpl-3.0.html).

## Support:

### Please star us!
⭐Your support is the driving force for us to move forward!

<div align="center">
  <img src="doc/image/star.gif" width="400" alt="star">
</div>

### Follow us
<div align="center">
  <a href="https://space.bilibili.com/26978344">
    <img src="doc/image/B.png" width="100" height="100" style="border-radius: 80%; overflow: hidden;" alt="octocat"/>
  </a>
  <a href="https://www.youtube.com/@agentParty">
    <img src="doc/image/YT.png" width="100" height="100" style="border-radius: 80%; overflow: hidden;" alt="octocat"/>
  </a>
</div>

<div align="center">
  <a href="https://www.youtube.com/watch?v=fIzlQOsuhZE" target="_blank">
    <img src="https://img.youtube.com/vi/fIzlQOsuhZE/0.jpg" 
         width="600" 
         alt="YouTube Video Thumbnail"
         style="border-radius: 8px; border: 1px solid #eee;">
  </a>
</div>

### Join the Community
If you have any questions or issues with the project, you are welcome to join our community.

1. QQ Group: `931057213`

<div style="display: flex; justify-content: center;">
    <img src="doc/image/Q群.jpg" style="width: 48%;" />
</div>

2. WeChat Group: `we_glm` (add the assistant's WeChat and join the group)

3. Discord: [Discord link](https://discord.gg/f2dsAKKr2V)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=heshengtao/super-agent-party&type=Date)](https://www.star-history.com/#heshengtao/super-agent-party&Date)